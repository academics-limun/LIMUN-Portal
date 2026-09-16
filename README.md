# LIMUN-Portal
Repository for all code and other documents relating to the 2027/First Edition of the LIMUN Portal

## Setup
### 1. Clone the repository
```bash
git clone <repository-url>
cd LIMUN-portal
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create environment file
```bash
cp .default.env .env
```

### 5. Start PostgreSQL
```bash
docker compose up -d
```

### 6. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Start
Start the Django development server:
```bash
python manage.py runserver
```

The application will be available at:
```text
http://localhost:8000
```

To stop PostgreSQL:
```bash
docker compose down
```

