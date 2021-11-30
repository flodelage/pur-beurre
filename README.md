# Pur Beurre
This application is the eighth project of the OpenClassrooms' Python developer course.

## Application description
The application aims to allow a user to find products with a better nutrition grade than a chosen product.

### Page content
The user opens his browser and enter the URL address: https://gd-py-bot.herokuapp.com.
The web page should contain the following elements:
* header : logo with tagline
* main zone : zone for conversing with the application
* footer : firsname and lastname, link with github repository and other social networks links.

### User journey
* the user enters for example: "Hi GrandPy! Do you know the address of the eiffel tower?"
* the user's message is displayed
* a loader indicates that the bot is thinking
* then a new message appears, GrandPy answers "Here is the exact address: Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France!"
* below appears a map indicating the location of the Eiffel Tower
* Grandpy sends another message: "I know quite a few stories about this district, for example: The bust of Gustave Eiffel by Antoine Bourdelle is a gilded bronze bust representing Gustave Eiffel, made by Antoine Bourdelle and installed in 1929 at the foot of the Eiffel Tower."
* a new message appears again: "If you want to know more, don't hesitate to click on this link to Wikipedia". This link sends the user to a wikipedia page dedicated to the eiffel tower.

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

6. Set Flask environement variables:
```
export FLASK_APP=run.py
export FLASK_ENV=development
```

7. Run flask in local:
```
flask run
```

8. Go to your browser in order to access the localhost at the URL:
```
http://127.0.0.1:5000/
```

## Running tests
```
python manage.py test
```
