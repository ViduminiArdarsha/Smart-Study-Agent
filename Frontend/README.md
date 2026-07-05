# Smart Study Planner - Frontend

Modern React + TypeScript frontend for the Smart Study Planner application.

## Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first styling
- **Radix UI** - Headless UI components
- **React Router** - Client-side routing

## Project Structure

```
src/
├── components/        # Reusable React components
│   └── ui/           # Radix UI-based UI components
├── pages/            # Page components for routes
├── services/         # API and external service integration
├── hooks/            # Custom React hooks
├── utils/            # Utility functions
├── styles/           # Global styles
├── App.tsx           # Main app component
└── main.tsx          # Entry point
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Create `.env.local` file:
```
VITE_API_BASE_URL=http://localhost:5000/api
```

3. Start the development server:
```bash
npm run dev
```

The app will open at `http://localhost:3000`

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run type-check` - Run TypeScript type checking

## Features

### Dashboard
- Overview of study progress
- Task management
- Quick access to upcoming events

### Planner
- Create and manage study sessions
- Schedule study activities
- View weekly schedule

### Settings
- Profile configuration
- Notification preferences
- Theme and language settings

## UI Components

All UI components are built using Radix UI primitives and styled with Tailwind CSS:

- **Button** - Interactive button component
- **Card** - Container component for content grouping
- **Input** - Form input field
- **Label** - Form label component

## API Integration

The frontend communicates with the backend via the `apiService` in `src/services/api.ts`. Update the `VITE_API_BASE_URL` environment variable to point to your backend API.

## Development

### Adding New Pages

1. Create a new file in `src/pages/`
2. Add the route in `App.tsx`

### Adding New Components

1. Create component files in `src/components/`
2. Import and use in pages or other components

### Styling

The project uses Tailwind CSS with custom theme variables. Modify `tailwind.config.ts` to customize the design system.

## Build & Deployment

```bash
npm run build
```

This creates an optimized production build in the `dist/` folder.

## License

MIT
