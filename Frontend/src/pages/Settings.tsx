import { Card } from '../components/ui/Card'
import { Button } from '../components/ui/Button'
import { Input } from '../components/ui/Input'
import { Label } from '../components/ui/Label'

export default function Settings() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-8">Settings</h2>
      
      <div className="max-w-2xl">
        {/* Profile Settings */}
        <Card className="mb-6">
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-4">Profile Settings</h3>
            <div className="space-y-4">
              <div>
                <Label htmlFor="name">Full Name</Label>
                <Input id="name" placeholder="Enter your full name" />
              </div>
              <div>
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" placeholder="Enter your email" />
              </div>
              <div>
                <Label htmlFor="timezone">Timezone</Label>
                <Input id="timezone" placeholder="Select your timezone" />
              </div>
              <Button>Save Changes</Button>
            </div>
          </div>
        </Card>

        {/* Notification Settings */}
        <Card className="mb-6">
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-4">Notifications</h3>
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span>Email Notifications</span>
                <input type="checkbox" defaultChecked />
              </div>
              <div className="flex items-center justify-between">
                <span>Study Reminders</span>
                <input type="checkbox" defaultChecked />
              </div>
              <div className="flex items-center justify-between">
                <span>Weekly Summary</span>
                <input type="checkbox" />
              </div>
            </div>
          </div>
        </Card>

        {/* Preferences */}
        <Card>
          <div className="p-6">
            <h3 className="text-lg font-semibold mb-4">Preferences</h3>
            <div className="space-y-4">
              <div>
                <Label htmlFor="theme">Theme</Label>
                <select id="theme" className="w-full px-3 py-2 border border-border rounded-md">
                  <option>Light</option>
                  <option>Dark</option>
                  <option>Auto</option>
                </select>
              </div>
              <div>
                <Label htmlFor="language">Language</Label>
                <select id="language" className="w-full px-3 py-2 border border-border rounded-md">
                  <option>English</option>
                  <option>Spanish</option>
                  <option>French</option>
                </select>
              </div>
              <Button>Save Preferences</Button>
            </div>
          </div>
        </Card>
      </div>
    </div>
  )
}
