## Table of contents
1. [Unit Testing](#unit-testing)
    - [Views](#views) 
    - [Forms](#forms)
- [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse)
    - [W3C Markup](#w3c-markup)
    - [W3C-CSS](#w3c-css) 
    - [PEP8](#pep8)
- [User Story Testing](#ser-story-testing)
    - [Admin](#admin)
    - [Site User](#site-user)
- [Responsive Testing](#Responsive-Testing)
***

# Unit Testing
I have performed unit tests for some page views, and all forms.

## Views
These views were tested to ensure the correct page is rendered back to the user. 

- Homepage

![Unit Test for Homepage](./static/unit_test_screenshots/home_test.png)

- About page 

![Unit Test for About page](./static/unit_test_screenshots/about_test.png)

- Add Review page

![Unit Test for Add Review page](./static/unit_test_screenshots/add_review_test.png)

Result: 

![Unit Test results](./static/unit_test_screenshots/views_unit_test_results.png)

## Forms
All forms were tested to ensure that mandatory fields are identified as such, and that data is submitted to the correct location. 

- Review Form

![Unit Test for Add Review form](./static/unit_test_screenshots/test_review_form_1.png)

![Unit Test for Add Review form](./static/unit_test_screenshots/test_review_form_2.png)

- Comment Form

![Unit Test for Comment form](./static/unit_test_screenshots/test_comment_form.png)

- Contact Form

![Unit Test for Contact form](./static/unit_test_screenshots/test_contact_form_1.png)

![Unit Test for Contact form](./static/unit_test_screenshots/test_contact_form_2.png)

Result: 

![Unit Test results](./static/unit_test_screenshots/forms_unit_test_results.png)

# Validator Testing 

## Lighthouse




## W3C Markup
All template files validate with no errors: 

- Home

![Validator results](./static/validation_test_screenshots/home_page_W3C_markup.png)

- About

![Validator results](./static/validation_test_screenshots/about_us_page_W3C_markup.png)

- Review detail 

![Validator results](./static/validation_test_screenshots/review_detail_page_W3C_markup.png)

- Login

![Validator results](./static/validation_test_screenshots/login_page_W3C_markup.png)

- Logout

![Validator results](./static/validation_test_screenshots/logout_page_W3C_markup.png)

- Register

![Validator results](./static/validation_test_screenshots/register_page_W3C_markup.png)

- Add review 

![Validator results](./static/validation_test_screenshots/add_review_page_W3C_markup.png)

- Edit review 

![Validator results](./static/validation_test_screenshots/edit_review_page_W3C_markup.png)

- Genre page

![Validator results](./static/validation_test_screenshots/genre_page_W3C_markup.png)

- Contact us 

![Validator results](./static/validation_test_screenshots/contact_us_page_W3C_markup.png)

## W3C CSS
No errors were found in the custom css. There were seven warnings raised, however these relate to Google Fonts and extensions. 

![Validator results](./static/validation_test_screenshots/css_validation_1.png)

![Validator results](./static/validation_test_screenshots/css_validation_2.png)

## PEP8 
No errors were found in the python code. In settings.py there were some long line errors which were unavoidable, and in models.py there were some continuation lines marked where I had resolved some long line errors. 

- admin.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/admin_contactus_PEP8.png)

- admin.py (Blog app)

![Validator results](./static/validation_test_screenshots/admin_PEP8.png)

- apps.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/apps_contactus_PEP8.png)

- apps.py (Blog app app)

![Validator results](./static/validation_test_screenshots/apps_PEP8.png)

- forms_test.py

![Validator results](./static/validation_test_screenshots/form_tests_PEP8.png)

- forms.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/forms_contactus_PEP8.png)

- forms.py (Blog app)

![Validator results](./static/validation_test_screenshots/forms_PEP8.png)

- manage.py

![Validator results](./static/validation_test_screenshots/manage_PEP8.png)

- models.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/models_contactus_PEP8.png)

- models.py (Blog app)

![Validator results](./static/validation_test_screenshots/models_PEP8.png)

- settings.py

![Validator results](./static/validation_test_screenshots/settings_PEP8.png)

- urls.py (Blog app)

![Validator results](./static/validation_test_screenshots/urls_blog_PEP8.png)

- urls.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/urls_contactus_PEP8.png)

- urls.py

![Validator results](./static/validation_test_screenshots/urls_PEP8.png)

- views.py (Contact Us app)

![Validator results](./static/validation_test_screenshots/views_contactus_PEP8.png)

- views.py (Blog app)

![Validator results](./static/validation_test_screenshots/views_PEP8.png)

- views_test.py

![Validator results](./static/validation_test_screenshots/views_tests_PEP8.png)

- wsgi.py

![Validator results](./static/validation_test_screenshots/wsgi_PEP8.png)