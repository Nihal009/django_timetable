# College Timetable Generator

## Overview

This is a Django-based web application designed to help college departments generate timetables for all 1st, 2nd, 3rd, and 4th-year classes. The application ensures that there are no conflicts in the schedules for professors across different years.

## Features

- Create and manage departments, professors, and courses.
- Automatically generate non-conflicting timetables for all classes.
- View and download timetables as PDF files.
- Separate timetable views for each year.

## Requirements

- Python 3.8+
- Django 4.2+
- ReportLab (for PDF generation)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/college-timetable-generator.git
   cd college-timetable-generator
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application:**

   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Admin Setup:**

   - Go to `http://127.0.0.1:8000/admin` and log in with your superuser credentials.
   - Add departments, professors, and courses through the Django admin interface.

2. **Generate Timetables:**

   - Visit `http://127.0.0.1:8000/ttgen/generate` to automatically generate and view timetables for all years.
   - Separate timetable tables are displayed for each year.

3. **Download Timetables:**

   - Click the "Download PDF" button to download the generated timetable as a PDF file.

## Project Structure

- `timetable/`: Contains the timetable generation app.
  - `models.py`: Defines the database models for departments, professors, courses, and timetable entries.
  - `views.py`: Handles the logic for generating and displaying timetables.
  - `urls.py`: Maps URLs to views.
  - `templates/`: Contains the HTML templates for the application.
  - `static/`: Contains static files (CSS, JS).
  - `pdf_utils.py`: Utility functions for generating PDF timetables.

- `ttgen/`: Main project directory.
  - `settings.py`: Project settings.
  - `urls.py`: Project URL configurations.

## Important Commands

- **Start the development server:**

  ```bash
  python manage.py runserver
  ```

- **Make migrations:**

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Create a superuser:**

  ```bash
  python manage.py createsuperuser
  ```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact `yourname@yourdomain.com`.

```

### `.gitignore`

Ensure your `.gitignore` file includes the following to avoid committing unnecessary files:

```plaintext
# Python
*.pyc
__pycache__/

# Environment
.env
env/
venv/

# Django
db.sqlite3

# OS
.DS_Store
Thumbs.db
```
