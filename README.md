
# VYBE

VYBE is a party planning and ticketing application built with Django. It provides users with an easy platform to create events, sell tickets, and manage guest lists. Whether you're hosting a small gathering or a large event, VYBE streamlines the planning process.

## Features

- Event creation and management
- Ticket purchasing and tracking
- Guest list management
- User authentication
- Responsive design for mobile and desktop

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vybe.git
   cd vybe
   ```

2. Set up a virtual environment:
   - **Windows:**
     ```bash
     env\Scriptsctivate
     ```
   - **Linux/Mac:**
     ```bash
     source env/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration

1. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

2. Create a superuser (optional but recommended for accessing the admin interface):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Server

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

## Testing

To run tests, use the following command:
```bash
python manage.py test
```


