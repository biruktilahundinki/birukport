#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Checking migrations status..."
python manage.py showmigrations

echo "Running migrations..."
python manage.py migrate --verbosity 2

echo "Creating database backup..."
ls -lah db.sqlite3 || echo "No database file found"

echo "Build complete!"
