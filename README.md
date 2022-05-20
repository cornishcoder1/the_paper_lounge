## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Development Planes](#Development-Planes)
    3. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features Left To Implement](#Features-Left-To-Implement)
4. [Bugs](#Bugs)
    1. [Fixed](#fixed)
    2. [Unfixed](#unfixed)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [User Story Testing](#User-Story-Testing)
     2. [Manual Testing](#Manual-Testing)
     3. [Automated Testing](#Automated-Testing)
        - [Validator](#validator)
        - [Browser](#browser)
     4. [User Testing](#User-Testing)
7. [Deployment](#Deployment)
     1. [Initial Deployment](#Initial-Deployment)

     2. [Final Deployment](#Final-Deployment)
     3. [Forking the Repository](#Forking-the-Repository)
     4. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
9. [Acknowledgements](#Acknowledgements)
***

# Introduction



# UX

## User Stories

## Development Planes

## Design



# Features

## Design Features

## Existing Features 

## Features Left to Implement




# Bugs

## Fixed
- Initial deployment to Heroku failed
    - Upon opening the app in Heroku for the first time after initial deployment, an Application Error was presented. By using the 'heroku logs --tail' command in the terminal, I was able to determine that I had written my application name in the wrong format in Line 1 of the Procfile (I had included underscores in the wsgi file name). I corrected the filename to 'thepaperlounge.wsgi' and upon re-opening the app after commiting the change, the Django successful install page was displayed. 

- Ability to like a review failed
    - Upon attempting to like a review, I was taken to an error page which stated that 'reverse' was an undefined variable. Upon checking the views.py file, I realised that I had forgotten to import the 'reverse' django shortcut. Once I had added the import to the top of the file (line 1), I was able to like a review without error. 

## Unfixed



# Technologies used

## Main Languages Used 

## Additional Languages Used

## Frameworks, Libraries and Programs Used



# Testing

## User Story Testing

## Manual Testing 

## Automated Testing
- Validator
- Browser 

## User Testing



# Deployment

## Initial Deployment
In Gitpod: 
1. Create a new repository from the CI full template 
2. To install Django, supporting libraries and dependencies, run the following commands in the terminal: 
    - Run command 'pip3 install 'django<4' gunicorn' to install Django and associated server
    - Run command 'pip3 install dj_database_url psycopg2' to install supporting libraries
    - Run command 'pip3 install dj3-cloudinary-storage' to install Cloudinary
    - Run command 'pip3 freeze --local > requirements.txt' to update requirements file
3. To create a new Django project and blog app, run the following commands in the terminal: 
    - Run command 'django-admin startproject thepaperlounge .' (The Paper Lounge is the name of my project) 
    - Run command 'python3 manage.py startapp blog' 
4. Add 'blog' to INSTALLED_APPS list in settings.py file
5. Migrate changes to the database with the following command in the terminal: 
    - 'python3 manage.py migrate'
6. Open project in the browser and check installation was successful with the following command in the terminal: 
    - 'python3 manage.py runserver' 

In Heroku: 
1. Create a new app in Heroku
2. Go to 'Resources' tab and add add-on 'Heroku Postgres' 
3. Go to 'Settings' tab and reveal config vars. Copy the DATABASE_URL

In Gitpod:
1. Create env.py file and paste DATABASE_URL: 
    - os.environ["DATABASE_URL"] = "your DATABASE_URL here"
2. Add SECRET_KEY to env.py:
    - os.environ["SECRET_KEY"] = "your SECRET_KEY here"
3. Configure database path and secret key in settings.py to be accessed from environment variables 
4. Migrate changes to the database with the following command in the terminal: 
    - 'python3 manage.py migrate'
5. Go to Heroku 'Resources' tab and click on 'Heroku Postgres' to see migrations
6. Perform a commit and push to GitHub 

In Cloudinary: 
1. Copy API Environment Variable from Cloudinary dashboard

In Gitpod
1. Paste API environment variable into env.py:
    - os.environ["CLOUDINARY_URL"] = "you API environment variable here"

In Heroku
1. Add a new config var in 'Settings'. Paste API environment variable into VALUE, and set KEY as CLOUDINARY_URL 

In Gitpod: 
1. In settings.py, add the following:
    - Cloudinary to the INSTALLED_APPS list
    - STATICFILE_STORAGE
    - STATICFILES_DIRS
    - STATIC_ROOT
    - MEDIA_URL
    - DEFAULT_FILE_STORAGE
    - TEMPLATES_DIR
    - Update DIRS in TEMPLATES with TEMPLATES_DIR
    - Update ALLOWED_HOSTS with ['the-paper-lounge.herokuapp.com', 'localhost']
2. Create 'media', 'static' and 'templates' folders, in the top level of file directory 
3. Create a 'Procfile' in the top level of the file directory 
4. In the Procfile, add the following code: 
    - web: gunicorn thepaperlounge.wsgi

**IMPORTANT - At the time of working on this project. Direct linkage of GitHub with Heroku was unavailable, due to a security attack on Heroku services. Therefore, the following steps were used as a work-around:**

5. Log into Heroku from the terminal with the following command: 
    - 'heroku login -i' (enter username and p/w as prompted)
6. Connect Heroku and Github by running the following command in the terminal:  
    - 'heroku git:remote -a the-paper-lounge' 
7. Confirm connection by running the following command in the terminal: 
    - 'git remote -v' (fetch and push should display for both heroku and origin/GitHub)
8. From this point forward, all commits should be pushed to both GitHub and Heroku with the following group of commands in the terminal:
    - 'git add .' 
    - 'git commit -m "commit message"' 
    - 'git push origin main' 
    - 'git push heroku main' 
9. Open app in Heroku once deployment is completed, to insure installation was successful 
    


## Final Deployment

## Forking the Repository

## Creating a Clone



# Credits 


## Content


## Media
1. Bookshelf icon by <a href="https://www.freepik.com" title="Freepik">Freepik</a> on <a href="https://www.flaticon.com/" title="Flaticon">Flaticon</a>

2. Placeholder image by <a href="https://www.pexels.com/@caio/" title="Caio">Caio</a> on <a href="https://www.pexels.com/" title="Pexels">Pexels</a>


# Acknowledgements

