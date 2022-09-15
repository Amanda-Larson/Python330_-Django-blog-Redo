###To run the server: 
python manage.py runserver

###To make migration:
python manage.py makemigrations 
(This lets django know that a new table has been made, or if there are new fields)

###To migrate:
python manage.py migrate

###To run tests:
python manage.py test blogging


###Notes:

- Model View Template (MVT) is a software pattern. Routing determines which view matches with request. The view gets data from the model. The model is independent from the view. The view uses the template to display information from the model.
- 