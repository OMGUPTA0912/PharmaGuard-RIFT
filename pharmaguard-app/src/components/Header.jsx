import { Activity } from 'lucide-react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header style={{
      padding: '1.5rem 0',
      borderBottom: '1px solid var(--border-color)',
      backgroundColor: 'rgba(15, 23, 42, 0.8)',
      backdropFilter: 'blur(12px)',
      position: 'sticky',
      top: 0,
      zIndex: 50
    }}>
      <div className="container" style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
        <Activity color="var(--accent-primary)" size={32} />
        <Link to="/" style={{ textDecoration: 'none' }}>
          <h1 style={{ margin: 0, fontSize: '1.5rem', letterSpacing: '-0.02em', color: 'var(--text-primary)' }}>
            PharmaGuard
          </h1>
        </Link>
      </div>
    </header>
  );
}
