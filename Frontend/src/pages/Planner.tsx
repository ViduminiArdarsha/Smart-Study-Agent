import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { Input } from '../components/ui/Input'
import { Label } from '../components/ui/Label'

export default function Planner() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-8">Study Planner</h2>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Add New Study Session */}
        <div className="lg:col-span-1">
          <Card>
            <div className="p-6">
              <h3 className="text-lg font-semibold mb-4">Add Study Session</h3>
              <div className="space-y-4">
                <div>
                  <Label htmlFor="subject">Subject</Label>
                  <Input id="subject" placeholder="e.g., Mathematics" />
                </div>
                <div>
                  <Label htmlFor="duration">Duration (minutes)</Label>
                  <Input id="duration" type="number" placeholder="e.g., 60" />
                </div>
                <div>
                  <Label htmlFor="date">Date</Label>
                  <Input id="date" type="date" />
                </div>
                <Button className="w-full">Add Session</Button>
              </div>
            </div>
          </Card>
        </div>

        {/* Study Schedule */}
        <div className="lg:col-span-2">
          <Card>
            <div className="p-6">
              <h3 className="text-lg font-semibold mb-4">This Week's Schedule</h3>
              <div className="space-y-3">
                <div className="flex justify-between items-center p-3 bg-muted rounded-lg">
                  <div>
                    <p className="font-medium">Mathematics</p>
                    <p className="text-sm text-muted-foreground">Monday, 2:00 PM - 3:30 PM</p>
                  </div>
                  <Button variant="outline" size="sm">Edit</Button>
                </div>
                <div className="flex justify-between items-center p-3 bg-muted rounded-lg">
                  <div>
                    <p className="font-medium">Physics</p>
                    <p className="text-sm text-muted-foreground">Wednesday, 3:00 PM - 4:00 PM</p>
                  </div>
                  <Button variant="outline" size="sm">Edit</Button>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  )
}
