# Real-time Sensor Dashboard

A real-time dashboard built with FastAPI and Svelte that displays and monitors sensor data using Server-Sent Events (SSE).

![Dashboard Final](/docs/assets/dashboard-final.gif)
![Dashboard Interactive](/docs/assets/dashboard-interactive.png)

## Features

- Real-time sensor data monitoring
- Interactive temperature history chart
- Humidity gauge visualization
- System status indicators
- Configurable alert thresholds
- Mobile-responsive design

## Tech Stack

- **Frontend:**
  - Svelte v5.23.2
  - SvelteKit v2.19.0
  - Node v22.14.0
  - npm v11.2.0

- **Backend:**
  - FastAPI 0.115.11
  - Python 3.13.2
  - SSE-Starlette 2.2.1

## Prerequisites

- Node.js 22.14.0+
- Python 3.13.2+
- npm 11.2.0+

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/svelte-fastapi-dashboard.git
cd svelte-fastapi-dashboard
```

2. Set up the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
cd backend
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
python main.py
```

2. In a new terminal, start the frontend development server:
```bash
cd frontend
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Development

### Backend Development

The backend uses FastAPI to create a REST API with SSE support. The main components are:
- `main.py`: Application entry point
- `app/api.py`: API routes and SSE implementation
- `app/sensor.py`: Mock sensor data generation

### Frontend Development

The frontend is built with Svelte and includes:
- Real-time data visualization with Chart.js
- Component-based architecture
- TypeScript for type safety
- Responsive design with CSS Grid

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 