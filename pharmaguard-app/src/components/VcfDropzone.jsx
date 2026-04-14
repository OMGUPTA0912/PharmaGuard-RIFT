import { UploadCloud } from 'lucide-react';

export default function VcfDropzone() {
  return (
    <div 
      style={{
        border: '2px dashed var(--border-color)',
        borderRadius: '0.75rem',
        padding: '3rem 2rem',
        textAlign: 'center',
        backgroundColor: 'rgba(15, 23, 42, 0.4)',
        cursor: 'pointer',
        transition: 'all var(--transition-fast)'
      }}
      onMouseOver={(e) => {
        e.currentTarget.style.borderColor = 'var(--accent-primary)';
        e.currentTarget.style.backgroundColor = 'rgba(59, 130, 246, 0.05)';
      }}
      onMouseOut={(e) => {
        e.currentTarget.style.borderColor = 'var(--border-color)';
        e.currentTarget.style.backgroundColor = 'rgba(15, 23, 42, 0.4)';
      }}
    >
      <UploadCloud size={48} color="var(--accent-primary)" style={{ margin: '0 auto 1rem auto' }} />
      <p style={{ fontWeight: 500, marginBottom: '0.5rem' }}>
        Drag & drop patient VCF file here
      </p>
      <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
        Supports .vcf, .vcf.gz up to 5MB
      </p>
    </div>
  );
}
