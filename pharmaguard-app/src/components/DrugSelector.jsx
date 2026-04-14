import { useState } from 'react';
import { Search, X } from 'lucide-react';

export default function DrugSelector() {
  const [selected, setSelected] = useState(['Clopidogrel']);
  const [query, setQuery] = useState('');

  const suggestions = ['Warfarin', 'Codeine', 'Simvastatin', 'Azathioprine', 'Fluorouracil'].filter(d => !selected.includes(d));

  return (
    <div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
        {selected.map(drug => (
          <span key={drug} style={{
            display: 'inline-flex', alignItems: 'center', gap: '0.5rem',
            backgroundColor: 'rgba(59, 130, 246, 0.2)', color: 'var(--accent-primary)',
            padding: '0.25rem 0.75rem', borderRadius: '9999px', fontSize: '0.875rem', fontWeight: 500
          }}>
            {drug}
            <X size={14} style={{ cursor: 'pointer' }} onClick={() => setSelected(selected.filter(d => d !== drug))} />
          </span>
        ))}
      </div>
      <div style={{ position: 'relative' }}>
        <Search size={18} style={{ position: 'absolute', top: '0.85rem', left: '1rem', color: 'var(--text-secondary)' }} />
        <input 
          type="text" 
          className="input-field" 
          placeholder="Search for medications..." 
          style={{ paddingLeft: '2.5rem' }}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && query) {
              if(!selected.includes(query)) setSelected([...selected, query]);
              setQuery('');
            }
          }}
        />
      </div>
    </div>
  );
}
