# Pur Beurre
This application is the eighth project of the OpenClassrooms' Python developer course.

## Application description
The application aims to allow a user to find products with a better nutrition grade than a chosen product.

### Features
* Account creation
* Login / Logout
* Search and display a product or products from a category by entering a name
* Display a product details (nutrition grade, nutrient intake, link to the Openfoodfacts page)
* Display substitutes list (products with a better nutrition grade than a chosen product)
* Save a substitute as favorite
* Display favorites
* Delete substitute from favorites

### Technologies
* Python / Django
* PostgreSQL
* Media Wiki API

## Getting started
1. Clone the repository:
```
git clone https://github.com/flodelage/pur-beurre.git
```

2. Create virtual environnement:
```
python3 -m venv env
```

3. Activate virtual environnement:
```
source env/bin/activate
```

4. Install requirements:
```
pip install -r requirements.txt
```

5. Update config.py:
MAPS_GEOCODING_KEY = "your_google_maps_geocoding_key"
MAPS_JS_KEY = "your_google_maps_js_key"
FLASK_KEY = "your_flask_personal_key"

6. Run the project in local:
```
python manage.py runserver
```

7. Go to your browser in order to access the localhost at the URL (by default):
```
http://127.0.0.1:8000/
```

## Running tests
```
python manage.py test
```
