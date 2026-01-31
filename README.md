# Portfolio & TaskSync Pro

A professional portfolio and service management application built with Django, featuring real-time chat, order management, and a fully editable portfolio site.

## 🚀 Features
- **Portfolio Website**: Modern, responsive portfolio with editable content.
- **Admin Management**: **Edit 100% of the website text** and images via the Admin Panel.
- **Service Management**: Customers can view services and place orders.
- **Real-time Chat**: WebSocket-powered chat between customers and admin.
- **PostgreSQL Ready**: Configured for high-performance production databases.
- **Cloudinary Integration**: Persistent storage for images and media files.

## 🛠️ Local Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Initialize Database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **Load Initial Data** (Crucial Step):
    This command creates the admin user, sets up the editable content, and populates sample skills/projects.
    ```bash
    python manage.py loadinitialdata
    ```
    *Default Login:* `admin` / `admin123` (or check the command output)

4.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

5.  **Access the App**:
    -   **Frontend**: `http://127.0.0.1:8000`
    -   **Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## 🌍 Production Deployment (Render/Heroku)

This project is configured to auto-deploy using **Render.com** (recommended).

### 1. Prerequisites
You need the following services on your platform:
- **Web Service** (Python 3.12+)
- **PostgreSQL Database** (Free tier available on Render/Neon)
- **Cloudinary Account** (Free tier for images)

### 2. Environment Variables
Set these variables in your hosting dashboard:

| Variable | Value | Description |
|----------|-------|-------------|
| `PYTHON_VERSION` | `3.12.0` | Python runtime version |
| `Use_Postgres` | `true` | (Optional) |
| `DATABASE_URL` | `postgres://...` | Provided automatically by Render/Heroku when you link a DB |
| `SECRET_KEY` | (Random String) | Security key for Django |
| `DEBUG` | `False` | Turn off debug mode in production |
| `CLOUDINARY_CLOUD_NAME` | `your_cloud_name` | From Cloudinary Dashboard |
| `CLOUDINARY_API_KEY` | `your_api_key` | From Cloudinary Dashboard |
| `CLOUDINARY_API_SECRET` | `your_api_secret` | From Cloudinary Dashboard |
| `PORTFOLIO_ADMIN_NAME` | `admin` | Username for the auto-created admin |
| `PORTFOLIO_ADMIN_PASSWORD` | `your_secure_password` | Password for the admin user |

### 3. Build & Start Commands
- **Build Command**:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate && python manage.py loadinitialdata
  ```
- **Start Command**:
  ```bash
  daphne -b 0.0.0.0 -p $PORT tasksync.asgi:application
  ```

---

## 👑 Managing the Database & Content

You do not need to writ SQL or code to manage the website. Everything is controlled via the **Admin Panel**.

### How to Edit "Editable Text"
1.  Go to `/admin` and log in.
2.  Look for **Site Content** under the **Portfolio** section.
3.  Click on **Site Content**.
4.  You will see tabs for every section (Navigation, Hero, About, Skills, etc.).
5.  Change the text and click **Save**. The website updates immediately.
    *(Note: Images uploaded here will also be saved permanently to Cloudinary)*

### How to Add Projects/Skills
1.  Go to `/admin`.
2.  Click **Projects** or **Skills**.
3.  Click **Add Project** button.
4.  Fill in the details. Cloudinary will handle the image upload automatically.

### How to Manage Messages
1.  Go to `/admin` -> **Contact Messages**.
2.  You can read new inquiries here.
3.  Type a reply in the "Admin Reply" box and save. The system will **automatically email the client** your reply.
