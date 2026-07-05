import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'

export default function Dashboard() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-8">Dashboard</h2>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-2">Today's Tasks</h3>
            <p className="text-muted-foreground mb-4">5 tasks remaining</p>
            <Button variant="default">View Tasks</Button>
          </div>
        </Card>

        <Card>
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-2">Study Progress</h3>
            <p className="text-muted-foreground mb-4">75% complete this week</p>
            <Button variant="default">View Progress</Button>
          </div>
        </Card>

        <Card>
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-2">Upcoming Events</h3>
            <p className="text-muted-foreground mb-4">2 exams this month</p>
            <Button variant="default">View Calendar</Button>
          </div>
        </Card>
      </div>

      <div className="mt-8">
        <Card>
          <div className="p-6">
            <h3 className="text-xl font-semibold mb-4">Recent Activity</h3>
            <div className="space-y-3">
              <p className="text-sm text-muted-foreground">No recent activity</p>
            </div>
          </div>
        </Card>
      </div>
    </div>
  )
}
