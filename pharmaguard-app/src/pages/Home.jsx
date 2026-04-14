import VcfDropzone from '../components/VcfDropzone';
import DrugSelector from '../components/DrugSelector';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="animate-fade-in" style={{ maxWidth: '800px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Personalized Risk Prediction</h2>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem' }}>
          Upload patient genetic data (VCF) and select queried medications to discover CPIC-aligned dosing guidelines and health equity insights.
        </p>
      </div>

      <div className="glass-panel delay-100 animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
        <div>
          <h3 style={{ marginBottom: '1rem', fontSize: '1.25rem' }}>1. Genomic Data</h3>
          <VcfDropzone />
        </div>
        
        <div>
          <h3 style={{ marginBottom: '1rem', fontSize: '1.25rem' }}>2. Selected Medications</h3>
          <DrugSelector />
        </div>

        <button className="btn btn-primary" style={{ marginTop: '1rem', width: '100%', padding: '1rem', fontSize: '1.1rem' }} onClick={() => navigate('/dashboard')}>
          Analyze Pharmacogenomic Risks
        </button>
      </div>
    </div>
  );
}
