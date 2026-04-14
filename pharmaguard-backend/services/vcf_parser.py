import re
import gzip
import io

TARGET_GENES = {"CYP2D6", "CYP2C19", "CYP2C9", "SLCO1B1", "TPMT", "DPYD"}

def parse_vcf(file_bytes: bytes, filename: str) -> list:
    """
    Parses a raw VCF file (in memory) and applies a regex heuristic to
    find specific PGx markers.
    """
    variants_found = []
    
    # Simple regex heuristic to look for GENE=... and STAR=... or RS=... inside INFO fields
    gene_pattern = re.compile(r"GENE=([A-Za-z0-9]+)")
    star_pattern = re.compile(r"STAR=(\*[0-9A-Za-z/]+)")
    rs_pattern = re.compile(r"RS=(rs\d+)")

    # Decode properly based on gz
    text_content = ""
    if filename.endswith(".gz"):
        with gzip.GzipFile(fileobj=io.BytesIO(file_bytes)) as gz:
            text_content = gz.read().decode('utf-8', errors='ignore')
    else:
        text_content = file_bytes.decode('utf-8', errors='ignore')

    lines = text_content.splitlines()
    for line in lines:
        if line.startswith("#"):
            continue
        
        # A standard VCF has at least 8 columns: CHROM POS ID REF ALT QUAL FILTER INFO
        parts = line.split('\t')
        if len(parts) < 8:
            continue
            
        info_col = parts[7]
        
        gene_match = gene_pattern.search(info_col)
        if gene_match:
            gene_candidate = gene_match.group(1).upper()
            if gene_candidate in TARGET_GENES:
                star_match = star_pattern.search(info_col)
                rs_match = rs_pattern.search(info_col)
                
                # If we lack an explicit STAR, fallback to RS or raw ALT
                variants_found.append({
                    "gene": gene_candidate,
                    "star": star_match.group(1) if star_match else None,
                    "rs_id": rs_match.group(1) if rs_match else parts[2] if parts[2] != "." else None,
                    "ref": parts[3],
                    "alt": parts[4]
                })

    # Deduplicate and consolidate into the profile structure
    profile_map = {}
    for var in variants_found:
        gene = var["gene"]
        if gene not in profile_map:
            profile_map[gene] = {
                "gene": gene,
                "star_allele": var["star"] or "*1",
                "rs_ids_detected": []
            }
        
        if var["rs_id"] and var["rs_id"] not in profile_map[gene]["rs_ids_detected"]:
            profile_map[gene]["rs_ids_detected"].append(var["rs_id"])
            
        # Very crude mock logic: If a new star is found, combine them e.g. *2/*3
        if var["star"] and var["star"] not in profile_map[gene]["star_allele"]:
            if profile_map[gene]["star_allele"] == "*1":
                profile_map[gene]["star_allele"] = var["star"]
            else:
                profile_map[gene]["star_allele"] += f"/{var['star'].replace('*', '')}"
                
    return list(profile_map.values())
