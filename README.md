# infinitumtech-Website
infinitumtech-Website

## Installation

### creating a environment
```bash
python -m venv .venv 
```

### Activate the environment
```bash
source .venv/scripts/activate
or 
source .venv/bin/activate
```
### installing the packages

```bash
pip install -r requirements.txt

```

### Making the migrations
```bash
python manage.py makemigrations
```

### updating the migrations
```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```