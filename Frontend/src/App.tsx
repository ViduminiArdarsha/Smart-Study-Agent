import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Planner from './pages/Planner'
import Settings from './pages/Settings'
import './App.css'

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-background">
        {/* Sidebar Navigation */}
        <nav className="w-64 bg-white border-r border-border shadow-sm">
          <div className="p-6">
            <h1 className="text-2xl font-bold text-primary mb-8">Study Planner</h1>
            <ul className="space-y-2">
              <li>
                <Link
                  to="/"
                  className="block px-4 py-2 rounded-lg hover:bg-secondary/20 text-foreground transition-colors"
                >
                  Dashboard
                </Link>
              </li>
              <li>
                <Link
                  to="/planner"
                  className="block px-4 py-2 rounded-lg hover:bg-secondary/20 text-foreground transition-colors"
                >
                  Planner
                </Link>
              </li>
              <li>
                <Link
                  to="/settings"
                  className="block px-4 py-2 rounded-lg hover:bg-secondary/20 text-foreground transition-colors"
                >
                  Settings
                </Link>
              </li>
            </ul>
          </div>
        </nav>

        {/* Main Content */}
        <main className="flex-1 overflow-auto">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/planner" element={<Planner />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
