#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --verbosity 2

echo "Loading initial data (SiteContent, Skills, Services)..."
# This is critical for fresh Postgres databases
python manage.py loadinitialdata

echo "Build complete!"
