import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'

export default function Dashboard() {
  return (
    <div className="space-y-8">
      <section className="rounded-3xl border border-sky-100 bg-white p-8 shadow-[0_24px_80px_rgba(15,23,42,0.08)]">
        <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-sky-600">
              Today
            </p>
            <h2 className="mt-3 text-4xl font-bold tracking-tight text-slate-950">
              Stay on top of your study plan.
            </h2>
            <p className="mt-4 text-base leading-7 text-slate-600">
              Track tasks, review progress, and jump into the next study session
              without losing focus.
            </p>
          </div>

          <div className="flex flex-wrap gap-3">
            <Button>Open Planner</Button>
            <Button variant="outline">Review Progress</Button>
          </div>
        </div>
      </section>

      <div className="grid gap-6 md:grid-cols-3">
        <Card className="border-sky-100 bg-white/95">
          <div className="p-6">
            <p className="text-sm font-medium text-sky-600">Today&apos;s Tasks</p>
            <h3 className="mt-2 text-3xl font-bold text-slate-950">5</h3>
            <p className="mt-2 text-sm text-slate-500">Tasks remaining for today</p>
          </div>
        </Card>

        <Card className="border-sky-100 bg-white/95">
          <div className="p-6">
            <p className="text-sm font-medium text-sky-600">Study Progress</p>
            <h3 className="mt-2 text-3xl font-bold text-slate-950">75%</h3>
            <p className="mt-2 text-sm text-slate-500">Complete this week</p>
          </div>
        </Card>

        <Card className="border-sky-100 bg-white/95">
          <div className="p-6">
            <p className="text-sm font-medium text-sky-600">Upcoming Events</p>
            <h3 className="mt-2 text-3xl font-bold text-slate-950">2</h3>
            <p className="mt-2 text-sm text-slate-500">Exams scheduled this month</p>
          </div>
        </Card>
      </div>

      <div className="grid gap-6 lg:grid-cols-3">
        <Card className="lg:col-span-2 border-slate-200/80 bg-white">
          <div className="p-6">
            <h3 className="text-xl font-semibold text-slate-950">Recent Activity</h3>
            <div className="mt-4 space-y-3">
              <p className="text-sm text-slate-500">No recent activity</p>
            </div>
          </div>
        </Card>

        <Card className="border-slate-200/80 bg-slate-950 text-white">
          <div className="p-6">
            <p className="text-sm font-medium text-sky-300">Next Session</p>
            <h3 className="mt-2 text-2xl font-semibold">Physics review</h3>
            <p className="mt-3 text-sm leading-6 text-slate-300">
              Wednesday, 3:00 PM - 4:00 PM
            </p>
            <Button className="mt-6 w-full bg-white text-slate-950 hover:bg-slate-100">
              Start Session
            </Button>
          </div>
        </Card>
      </div>
    </div>
  )
}
