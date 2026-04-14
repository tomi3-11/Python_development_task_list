# Python Development Task List

This repository contains beginner-to-intermediate Python tasks organized by level.

## Requirements

- Python 3.14+
- uv

## Setup

From the project root:

```bash
uv sync
```

## Project Structure

### Level 1

- `number_quessing_game.py`: Number guessing game.
- `simple_calculator.py`: Basic calculator for arithmetic operations.

### Level 2

- `api_integration.py`: Weather API integration using OpenWeather.
- `data_scraper.py`: Scrapes book title, price, and availability into CSV.

### Level 3

- `basic_file_encryption.py`: Caesar cipher file encryption/decryption.
- `django_project/`: Django task manager web app with authentication.

## Run Scripts

From the project root:

```bash
uv run python level1/simple_calculator.py
uv run python level1/number_quessing_game.py
uv run python level2/api_integration.py
uv run python level2/data_scraper.py
uv run python level3/basic_file_encryption.py
```

## Django App

Location: `level3/django_project`

Features:

- User registration
- Login/logout
- Password reset (console email backend)
- Role-based access (admin and regular user)
- Task creation and status toggle

Run Django app:

```bash
cd level3/django_project
uv run python manage.py migrate
uv run python manage.py runserver
```

Optional admin setup:

```bash
cd level3/django_project
uv run python manage.py createsuperuser
```
