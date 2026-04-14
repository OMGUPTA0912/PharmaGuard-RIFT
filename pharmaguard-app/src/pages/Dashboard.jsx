import { AlertTriangle, CheckCircle, Info, Copy, Download } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip, ResponsiveContainer } from 'recharts';

const dummyPkData = [
  { time: '0h', standard: 0, patient: 0 },
  { time: '2h', standard: 50, patient: 90 },
  { time: '4h', standard: 80, patient: 140 },
  { time: '8h', standard: 60, patient: 180 },
  { time: '12h', standard: 30, patient: 160 },
  { time: '24h', standard: 5, patient: 120 },
];

export default function Dashboard() {
  return (
    <div className="animate-fade-in" style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
      
      {/* Header section */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div>
          <h2 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Risk Assessment Report</h2>
          <p style={{ color: 'var(--text-secondary)' }}>Generated from uploaded VCF for Patient ID: 1948-2849</p>
        </div>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button className="btn btn-secondary"><Download size={18} /> Export JSON</button>
        </div>
      </div>

      {/* Main Alert Card */}
      <div className="glass-panel" style={{ borderLeft: '4px solid var(--status-ineffective)' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '1.5rem' }}>
          <AlertTriangle color="var(--status-ineffective)" size={32} />
          <div>
            <h3 style={{ fontSize: '1.5rem' }}>CLOPIDOGREL</h3>
            <span className="badge badge-toxic" style={{ backgroundColor: 'transparent', border: '1px solid var(--status-ineffective)', color: 'var(--status-ineffective)'}}>INEFFECTIVE (HIGH RISK)</span>
          </div>
        </div>
        
        <div style={{ padding: '1.5rem', backgroundColor: 'rgba(15, 23, 42, 0.4)', borderRadius: '0.5rem', marginBottom: '1.5rem' }}>
          <h4 style={{ marginBottom: '0.5rem', color: 'var(--text-secondary)' }}>Pharmacogenomic Profile:</h4>
          <p style={{ fontSize: '1.1rem', marginBottom: '0.5rem' }}><strong>CYP2C19 *2/*3</strong> (Poor Metabolizer)</p>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>Detected variants: rs4244285, rs4986894</p>
        </div>

        <h4 style={{ fontSize: '1.1rem', marginBottom: '0.5rem' }}>CPIC Clinical Recommendation</h4>
        <p style={{ marginBottom: '1.5rem', lineHeight: 1.6 }}>Avoid standard dose clopidogrel. Consider alternative antiplatelet therapy (e.g., prasugrel or ticagrelor). Clopidogrel is a prodrug requiring activation by CYP2C19; therefore, this patient will have significantly reduced active metabolite formation.</p>

        {/* PK Curve Visualization */}
        <div style={{ height: '300px', marginTop: '2rem' }}>
          <h4 style={{ marginBottom: '1rem', textAlign: 'center', color: 'var(--text-secondary)' }}>Predicted Active Metabolite Concentration vs Standard</h4>
          <ResponsiveContainer width="100%" height="80%">
            <LineChart data={dummyPkData} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" />
              <XAxis dataKey="time" stroke="var(--text-secondary)" />
              <YAxis stroke="var(--text-secondary)" />
              <RechartsTooltip contentStyle={{ backgroundColor: 'var(--panel-bg)', border: 'none', borderRadius: '0.5rem' }} />
              <Line type="monotone" dataKey="standard" stroke="var(--status-safe)" strokeWidth={2} name="Standard Patient" />
              <Line type="monotone" dataKey="patient" stroke="var(--status-ineffective)" strokeWidth={3} name="This Patient (Predicted)" activeDot={{ r: 8 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* EHR & Equity Insights Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        <div className="glass-panel" style={{ display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
            <Copy color="var(--accent-primary)" size={20} />
            <h3>FHIR EHR Note</h3>
          </div>
          <p style={{ fontFamily: 'monospace', fontSize: '0.9rem', backgroundColor: 'rgba(0,0,0,0.2)', padding: '1rem', borderRadius: '0.5rem', flexGrow: 1, marginBottom: '1.5rem' }}>
            PHARMACIST/PGX CONSULT NOTE:<br/><br/>Patient identified as a CYP2C19 Poor Metabolizer (*2/*3). Clopidogrel therapy flagged as INEFFECTIVE due to reduced active metabolite formation. <br/><br/>RECOMMENDATION: Switch to alternative antiplatelet (Prasugrel/Ticagrelor).
          </p>
          <button className="btn btn-primary" style={{ width: '100%' }}>Copy to Clipboard</button>
        </div>

        <div className="glass-panel" style={{ borderTop: '4px solid #8b5cf6' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem' }}>
            <Info color="#8b5cf6" size={20} />
            <h3>Health Equity Insight</h3>
          </div>
          <p style={{ lineHeight: 1.6 }}>
            The <strong>CYP2C19 *2</strong> allele detected is highly prevalent in populations of East Asian descent (up to 30%). 
            <br/><br/>
            Utilizing this PGx-guided dosing neutralizes standard empirical prescribing bias for this patient, preventing adverse cardiovascular events that a "one-size-fits-all" dose would have caused.
          </p>
        </div>
      </div>

    </div>
  );
}
