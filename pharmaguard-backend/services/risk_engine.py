def map_phenotype(gene: str, star_allele: str):
    """
    Mocked CPIC Logic Mapper.
    """
    if "/*" in star_allele or star_allele in ["*2", "*3", "*2/*3", "*3/*3"]:
        return "Poor Metabolizer"
    if star_allele == "*1":
        return "Normal Metabolizer"
    if star_allele in ["*17", "*1/*17", "*17/*17"]:
        return "Ultrarapid Metabolizer"
    return "Unknown Phenotype"


def evaluate_risks(genetic_profile: list, requested_drugs: list) -> dict:
    for g in genetic_profile:
        g["phenotype"] = map_phenotype(g["gene"], g["star_allele"])

    risk_assessment = []
    clinical_rec = ""
    ehr_note = ""
    llm_exp = ""
    equity_insight = ""

    # Extremely simplistic mockup logic for MVP based on Clopidogrel and CYP2C19
    drugs_upper = [d.upper() for d in requested_drugs]
    
    # Check for Clopidogrel interacting with a detected CYP2C19 Poor Metabolizer
    cyp2c19_prof = next((p for p in genetic_profile if p["gene"] == "CYP2C19"), None)
    
    if "CLOPIDOGREL" in drugs_upper:
        if cyp2c19_prof and cyp2c19_prof["phenotype"] == "Poor Metabolizer":
            risk_assessment.append({"drug": "CLOPIDOGREL", "risk_category": "Ineffective"})
            clinical_rec = "Avoid standard dose clopidogrel. Consider alternative antiplatelet therapy (e.g., prasugrel or ticagrelor)."
            llm_exp = "The patient possesses loss-of-function alleles for the CYP2C19 gene, resulting in a Poor Metabolizer phenotype. Clopidogrel requires activation by CYP2C19; reduced active metabolite formation limits its antiplatelet efficacy."
            ehr_note = f"PHARMACIST/PGX CONSULT NOTE: Patient identified as a CYP2C19 Poor Metabolizer ({cyp2c19_prof['star_allele']}). Clopidogrel therapy flagged as INEFFECTIVE. RECOMMENDATION: Switch to alternative antiplatelet."
            if "2" in cyp2c19_prof["star_allele"]:
                equity_insight = "The CYP2C19 *2 allele detected is highly prevalent in populations of East Asian descent. Utilizing this PGx-guided dosing neutralizes standard empirical prescribing bias for this patient."
        else:
            risk_assessment.append({"drug": "CLOPIDOGREL", "risk_category": "Safe"})
            clinical_rec = "Standard CPIC dosing guidelines apply. Continue monitoring."
            llm_exp = "Normal CYP2C19 function expected based on baseline genetics."
            ehr_note = "PHARMACIST/PGX CONSULT NOTE: Patient identified as a Normal Metabolizer. Clopidogrel therapy is SAFE."
            equity_insight = "No specific demographic variance detected for this allele combination."
            
    if "CODEINE" in drugs_upper:
        risk_assessment.append({"drug": "CODEINE", "risk_category": "Unknown"})
        
    return {
        "pharmacogenomic_profile": genetic_profile,
        "risk_assessment": risk_assessment,
        "clinical_recommendations": clinical_rec,
        "llm_explanation": llm_exp,
        "ehr_clinical_note": ehr_note,
        "equity_insight": equity_insight,
        "quality_metrics": {
            "parse_status": "SUCCESS" if genetic_profile else "NO_TARGET_VARIANTS_FOUND"
        }
    }
