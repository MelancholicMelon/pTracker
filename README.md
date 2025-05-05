# Urban Parking Tracker 🚗📍

A Django-based web application developed for the **PBL3 (Project-Based Learning 3)** course.  
**Urban Parking Tracker** helps users find, review, and manage urban parking locations through an interactive web interface.

## Features

- 🔐 **User Authentication**
  - User registration, login, and password recovery
- 🗺️ **Map Integration**
  - Interactive map to view available parking spots (`map_page.html`)
- ℹ️ **Parking Spot Details**
  - Individual parking pages with reviews and location data
- 📝 **User Reviews**
  - Users can submit and read reviews of parking spots
- 👤 **Account Management**
  - Edit user profile and view history of points earned
- 📄 **Responsive Templates**
  - Built using reusable and organized templates like `base.html`

## Folder Structure

- `templates/`
  - HTML templates for all pages, such as:
    - `index.html` – Home page
    - `map_page.html` – Interactive parking map
    - `parking_detail.html` – Parking spot details and reviews
    - `login.html`, `register.html`, `forgot_password.html` – Authentication
    - `account_manage.html`, `points_history.html` – User profile and activity

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/urban-parking-tracker.git
   cd urban-parking-tracker
 2. Set up virtual environment

```bash
python -m venv venv
```

**Activate the environment:**

<details>
<summary>Windows</summary>

```bash
venv\Scripts\activate
```

</details>

<details>
<summary>macOS / Linux</summary>

```bash
source venv/bin/activate
```

</details>

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py runserver
```

This project is for academic use only.
