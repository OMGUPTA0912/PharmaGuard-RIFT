import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <Header />
      <main className="container" style={{ padding: '2rem 0' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
