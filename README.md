# Flask Web Application

A simple **Flask web application** that displays student data, provides a JSON API, and allows users to add new students through a web form.

---

## Setup

Create the project and install Flask:

```bash
mkdir flask_app
cd flask_app
uv init
uv add flask
```

Create the main application file:

```
app.py
```

Run the application with:

```bash
uv run app.py
```

---

## Features

### Home Page

**Route:** `/`

The home page displays:

- Your **name**
- A **short description**
- Links to:
  - `/students`
  - `/about`

Example:

```
http://localhost:5000/
```

---

### About Page

**Route:** `/about`

This page contains:

- A heading **"About This App"**
- A short explanation of the project
- A link back to the home page

Example:

```
http://localhost:5000/about
```

---

### Students List

**Route:** `/students`

Displays a list of students using an **HTML template**.

Features:

- Student data stored in `app.py`
- Students displayed in an **HTML table**
- Table columns:
  - `#`
  - `Name`
  - `Score`
- Students sorted by **score (highest first)**

Example:

```
http://localhost:5000/students
```

---

### Individual Student Page

**Route:**

```
/student/<name>
```

Displays information about a specific student.

If the student exists:

- Show the **name**
- Show the **score**
- Display a **status message** based on score

| Score Range | Status |
|--------------|--------|
| 80+ | Excellent |
| 50–79 | Good |
| 1–49 | Needs improvement |
| 0 | No data |

If the student does not exist:

- Show **"Student not found"**
- Return **HTTP 404**

Examples:

```
/student/Timur
/student/Unknown
```

---

### JSON API

#### All Students

**Route:**

```
/api/students
```

Returns all student data as JSON.

Example:

```json
{
  "Abdul-Aziz": 77,
  "Timur": 89
}
```

---

#### Single Student

**Route:**

```
/api/student/<name>
```

Example response:

```json
{
  "name": "Timur",
  "score": 89,
  "status": "Excellent"
}
```

If the student does not exist:

```json
{
  "error": "Student not found"
}
```

Returns **status code 404**.

---

### Add Student Form

**Route:**

```
/add
```

Provides a form to add a new student.

Form inputs:

- **Student name** (text)
- **Score (0–100)** (number)
- **Submit button**

Validation:

- Name cannot be empty
- Score must be between **0 and 100**
- Student names must be **unique**

Behavior:

- If validation fails → show an **error message**
- If valid → add the student to `students_data`
- Redirect to `/students`

The route supports **GET and POST**.

---

### Styling

The project includes a CSS file:

```
static/style.css
```

Features:

- Shared stylesheet for all pages
- Styled tables with borders and padding
- Styled links
- Centered layout
- Styled form inputs and buttons

Add CSS in templates:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## Project Structure

```
flask_app/
│
├── app.py
├── pyproject.toml
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── students.html
│   ├── student.html
│   └── add.html
│
└── static/
    └── style.css
```

---

## Running the Project

```bash
cd flask_app
uv run app.py
```

The application will run at:

```
http://localhost:5000
```