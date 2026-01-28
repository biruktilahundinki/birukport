# TaskSync Pro (Django)

## Setup Instructions

Since Node.js/Python commands were unavailable during setup, the project files have been generated manually. You need to perform the following steps to run the application.

1.  **Install Python**: Ensure Python is installed and added to your PATH.
    -   Verify with: `python --version` or `py --version`

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: This now installs `channels` and `daphne` for real-time chat.*

3.  **Initialize Database**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create Admin User**:
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run Server**:
    ```bash
    python manage.py runserver
    ```
    *This will now launch the ASGI server (Daphne) automatically to support WebSockets.*

6.  **Access the App**:
    -   Open `http://127.0.0.1:8000` in your browser.
    -   Admin Panel: `http://127.0.0.1:8000/admin/`

## Features Implemented
### Core (Phase 1)
-   **User Auth**: Login, Register, Logout (Customer & Admin roles).
-   **Service Catalog**: View services (add via Admin panel).
-   **Ordering**: Place orders with requirements.
-   **Dashboards**: Customer & Admin order management.

### Real-time Chat (Phase 2)
-   **Live Chat**: Communication between Customer and Admin on specific orders.
-   **WebSockets**: Powered by Django Channels.
-   **Persistence**: Messages are saved to the database.
-   **UI**: Integrated chat window in the Order Detail view.
"# birukport" 
