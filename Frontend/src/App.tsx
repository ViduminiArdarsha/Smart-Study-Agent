import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Planner from './pages/Planner'
import Settings from './pages/Settings'
import './App.css'

const navItems = [
  { to: '/', label: 'Dashboard' },
  { to: '/planner', label: 'Planner' },
  { to: '/settings', label: 'Settings' },
]

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-slate-950 text-slate-100">
        <div className="fixed inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-32 left-1/4 h-72 w-72 rounded-full bg-sky-500/20 blur-3xl" />
          <div className="absolute top-1/2 right-0 h-80 w-80 rounded-full bg-blue-600/10 blur-3xl" />
        </div>

        <div className="relative flex min-h-screen flex-col lg:flex-row">
          <aside className="hidden w-80 flex-col border-r border-white/10 bg-slate-950/90 px-6 py-8 backdrop-blur lg:flex">
            <div className="mb-10">
              <p className="text-xs font-semibold uppercase tracking-[0.3em] text-sky-300">
                Smart Study Planner
              </p>
              <h1 className="mt-3 text-3xl font-bold text-white">
                Plan better. Study smarter.
              </h1>
              <p className="mt-3 text-sm leading-6 text-slate-400">
                Keep sessions, tasks, and progress in one focused workspace.
              </p>
            </div>

            <nav className="space-y-2">
              {navItems.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  className={({ isActive }) =>
                    [
                      'flex items-center rounded-xl px-4 py-3 text-sm font-medium transition-colors',
                      isActive
                        ? 'bg-sky-500/15 text-white ring-1 ring-sky-400/30'
                        : 'text-slate-300 hover:bg-white/5 hover:text-white',
                    ].join(' ')
                  }
                >
                  {item.label}
                </NavLink>
              ))}
            </nav>

            <div className="mt-auto rounded-2xl border border-white/10 bg-white/5 p-4">
              <p className="text-sm font-medium text-white">Weekly focus</p>
              <p className="mt-2 text-sm leading-6 text-slate-400">
                Clear your next three study blocks to build momentum.
              </p>
            </div>
          </aside>

          <div className="flex min-h-screen flex-1 flex-col">
            <header className="border-b border-white/10 bg-slate-950/80 px-4 py-4 backdrop-blur lg:hidden">
              <p className="text-xs font-semibold uppercase tracking-[0.3em] text-sky-300">
                Smart Study Planner
              </p>
              <div className="mt-4 flex gap-2 overflow-x-auto pb-1">
                {navItems.map((item) => (
                  <NavLink
                    key={item.to}
                    to={item.to}
                    className={({ isActive }) =>
                      [
                        'whitespace-nowrap rounded-full px-4 py-2 text-sm font-medium transition-colors',
                        isActive
                          ? 'bg-sky-500 text-white'
                          : 'bg-white/5 text-slate-300 hover:bg-white/10 hover:text-white',
                      ].join(' ')
                    }
                  >
                    {item.label}
                  </NavLink>
                ))}
              </div>
            </header>

            <main className="relative flex-1 overflow-auto bg-[radial-gradient(circle_at_top,_rgba(14,165,233,0.12),_transparent_35%),linear-gradient(180deg,_rgba(248,250,252,1),_rgba(239,246,255,1))] text-slate-900">
              <div className="relative z-10 p-6 lg:p-10">
                <Routes>
                  <Route path="/" element={<Dashboard />} />
                  <Route path="/planner" element={<Planner />} />
                  <Route path="/settings" element={<Settings />} />
                </Routes>
              </div>
            </main>
          </div>
        </div>
      </div>
    </Router>
  )
}

export default App
