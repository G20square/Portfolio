# Portfolio Website
A modern, responsive personal portfolio website built with Django 5.0. This project features project showcases, skill set management, a secure contact system, and an administrative dashboard for easy content updates.
## 🚀 Features
- **Project Gallery**: Showcase your work with titles, descriptions, tech stacks, and direct links to GitHub and live demos.
- **Skill Proficiency**: Interactive skill bars to display your technical expertise.
- **Professional Profile**: Manage your bio, profile picture, and downloadable resume.
- **Contact System**:
  - Integrated contact form with database logging.
  - Automated email notifications to you (the admin).
  - Automated confirmation emails to the sender.
- **Admin Dashboard**: A secure, user-friendly interface to manage all portfolio content without touching the code.
- **REST API**: Built-in API support for future integrations using Django Rest Framework.
## 🛠️ Tech Stack
- **Backend**: Python 3.10+, Django 5.0
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Frontend**: HTML5, Vanilla CSS, JavaScript
- **Static Files**: Whitenoise for efficient static asset delivery.
- **API**: Django Rest Framework (DRF)
- **Deployment**: Docker, Vercel, Render
## ⚙️ Setup & Installation
### Prerequisites
- Python 3.10 or higher
- PostgreSQL (optional for local development, defaults to SQLite)
- Docker (optional)
### Local Development
1. **Clone the repository**:
   ```bash
   git clone https://github.com/G20square/Portfolio.git
   cd portfolio
Create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Configure environment variables: Create a .env file in the root directory based on .env.example:

DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/dbname  # Or leave empty for SQLite
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
Run migrations and start the server:

python manage.py migrate
python manage.py runserver
🐳 Docker Support
Run the entire stack using Docker Compose:

docker-compose up --build
The application will be available at http://localhost:8000.

🚢 Deployment
Vercel
This project is configured for Vercel deployment via vercel.json and vercel_app.py.

Connect your GitHub repository to Vercel.
Set the environment variables in the Vercel dashboard.
Deploy!
Render
A render.yaml file is included for easy deployment to the Render platform.

📁 Project Structure
portfolio/: Main application logic (models, views, forms).
config/: Project-wide settings and configuration.
templates/: HTML templates for the frontend and dashboard.
static/: CSS, JavaScript, and image assets.
media/: User-uploaded content (projects images, resumes).
