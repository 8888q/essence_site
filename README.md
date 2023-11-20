# Essence
Ever read a passage in a book that felt especially poignant, or have a part of a song that really stands out?
Essence is a website built to save and remember the essence of media like those.
Currently, you can save a moment as a text quote or a video/audio quote via youtube with a start and end time.  

### Packages used:
```
google-api-python-client
isodate
Django
django-debug-toolbar
bootstrap5
```

### How to use:
This repo is the entire web server used to run Essence. If you would like to try it yourself:
1. Make sure you have installed the required packages
2. In your terminal, navigate to the project directory and type:
```
\> py manage.py runserver
```
Essence will be running at `http://127.0.0.1:8000/essence/` by default

If you want to see an already populated user experience, the test dev user is:

```
username: littl
password: admin
```
