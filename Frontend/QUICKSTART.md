# Quick Start Guide

## Installation & Setup

### 1. Navigate to Frontend Directory
```bash
cd Frontend
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure Environment
Copy `.env.example` to `.env.local`:
```bash
cp .env.example .env.local
```

Update the API URL if needed (default points to `http://localhost:5000/api`).

### 4. Start Development Server
```bash
npm run dev
```

The app will automatically open at `http://localhost:3000`

---

## Project Structure

```
Frontend/
├── src/
│   ├── components/
│   │   └── ui/              # Radix UI-based reusable components
│   ├── pages/               # Page components for each route
│   ├── services/            # API service layer
│   ├── utils/               # Utility functions
│   ├── styles/              # Global styles
│   ├── App.tsx              # Main app component with routing
│   └── main.tsx             # React entry point
├── index.html               # HTML template
├── package.json             # Dependencies and scripts
├── tailwind.config.ts       # Tailwind CSS configuration
├── vite.config.ts           # Vite configuration
├── tsconfig.json            # TypeScript configuration
└── README.md                # Full documentation
```

---

## Available NPM Scripts

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server (port 3000) |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint |
| `npm run type-check` | Run TypeScript type checking |

---

## Pages

### Dashboard (`/`)
- Study progress overview
- Task summary
- Quick action cards

### Planner (`/planner`)
- Add new study sessions
- View weekly schedule
- Manage study activities

### Settings (`/settings`)
- Profile configuration
- Notification preferences
- Theme and language options

---

## UI Components

Built with Radix UI primitives and Tailwind CSS:

- **Button** - Various styles (default, destructive, outline, ghost, secondary)
- **Card** - Container with header, content, footer sections
- **Input** - Form input fields with validation styling
- **Label** - Accessible form labels

---

## Connecting to Backend

The frontend communicates with your Python backend via REST API calls in `src/services/api.ts`.

Update `VITE_API_BASE_URL` in `.env.local` to match your backend server address.

Example endpoints:
- `GET /api/sessions` - Get study sessions
- `POST /api/sessions` - Create study session
- `GET /api/syllabus` - Get syllabus
- `POST /api/feedback` - Submit feedback

---

## Styling & Customization

### Tailwind CSS
- Configuration: `tailwind.config.ts`
- Global styles: `src/styles/index.css`
- Theme variables defined in `src/App.css`

### Color Variables
- Primary, Secondary, Destructive colors
- Muted, Accent colors
- Background and Foreground colors

Modify CSS variables in `src/App.css` to customize the theme.

---

## Troubleshooting

### Port 3000 already in use
Modify `vite.config.ts` to use a different port:
```typescript
server: {
  port: 3001, // Change to any available port
}
```

### API connection errors
1. Verify backend is running (default: `http://localhost:5000`)
2. Check `VITE_API_BASE_URL` in `.env.local`
3. Check browser console for error details
4. Verify CORS is enabled on backend

### Dependencies not installing
```bash
rm -rf node_modules package-lock.json
npm install
```

---

## Next Steps

1. Start the development server: `npm run dev`
2. Begin customizing pages in `src/pages/`
3. Create additional components in `src/components/`
4. Connect API calls in `src/services/api.ts`
5. Build for production: `npm run build`

Happy coding! 🎓
