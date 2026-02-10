# Job Application Tracker
A lightweight job application tracker built with Flask and SQLite.
It allows users to record, update, and manage job applications through a simple web interface, with a focus on clean structure and safe backend logic.

This project was built to practise full-stack fundamentals: routing, form handling, validation, database operations, and templating.

---

## Features
- Add job applications with company name, role, date applied, and optional link
- Automatically sets application status to Applied on creation
- Edit existing applications, including status updates
- Delete applications with confirmation
- Validates input and restricts status values to predefined states
- Clean separation between list view and edit view

---

## Tech Stack
- Python 3
- Flask
- SQLite
- HTML / CSS (Jinja templates)

---

## How to run locally
1. Clone the repository  
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   ```bash
   python3 app.py
5. Open your browser and go to:
   ```cpp
   http://127.0.0.1.5000
The SQLite database (jobs.db) will be created automatically on first run.

---

## What I learned
- Building a complete CRUD application using Flask
- Handling form submissions and server-side validation
- Using SQLite with parameterised queries to avoid SQL injection
- Managing optional fields cleanly (NULL vs empty values)
- Enforcing data integrity using backend-defined allowed values
- Structuring templates with Jinja and separating concerns (index vs edit)
- Basic UI styling with CSS for usability
- Incremental development: building features step-by-step and fixing issues as they arise

---

## Possible Improvements
- Flash messages for validation and success feedback
- Inline status updates on the main table
- Basic authentication for multi-user support
- Automated tests
- UI polish and accessibility improvements
