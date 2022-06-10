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

# User Story Testing 

## Admin 

- As a site admin I can access the admin panel from the navigation when logged in so that I don't have to manually type the URL each time. 

When the admin is logged in, a link to the Admin Panel is present on the nav bar. When clicked this takes the admin straight to the admin panel. This link only shows for the admin, and is not accessible to any other user. 

![User Story testing](./static/user_story_test_screenshots/admin_panel_UStesting.png)

<br>

- As a site admin I can approve reviews and comments so that suitability of content can be ensured.

Within the admin panel, the admin can select Reviews or Comments:
![User Story testing](./static/user_story_test_screenshots/approve_comments_reviews_1_UStesting.png)

Comments can be selected and then approval can be performed via the dropdown menu:
![User Story testing](./static/user_story_test_screenshots/approve_comments_reviews_2_UStesting.png)

Reviews can be selected, and then approved and published: 
![User Story testing](./static/user_story_test_screenshots/approve_comments_reviews_3_UStesting.png)

Once approved and published, reviews and comments will become visible to all users on the site. 

<br>

- As a site admin/user I can create book reviews to share with other users.

Within the admin panel, the admin can select Reviews:
![User Story testing](./static/user_story_test_screenshots/create_reviews_admin_UStesting.png)

'Add Review' can then be selected:
![User Story testing](./static/user_story_test_screenshots/create_reviews_admin_2_UStesting.png)

The review can then be submitted via the form. It still needs to be approved and published before it appears on the site: 
![User Story testing](./static/user_story_test_screenshots/create_reviews_admin_4_UStesting.png)

<br>

- As a site admin/user I can update and delete reviews written by me so that I can manage my own content.

Within the admin panel, the admin can select Reviews:
![User Story testing](./static/user_story_test_screenshots/create_reviews_admin_UStesting.png)

Here, the admin can edit or delete their review: 
![User Story testing](./static/user_story_test_screenshots/edit_reviews_admin_UStesting.png)

![User Story testing](./static/user_story_test_screenshots/edit_reviews_admin_2_UStesting.png)

![User Story testing](./static/user_story_test_screenshots/edit_reviews_admin_3_UStesting.png)

<br>

- As a site admin I can manage genres so that I can add to, modify or remove them

Within the admin panel, the admin can select Genres:
![User Story testing](./static/user_story_test_screenshots/manage_genres_admin_UStesting.png)

Here, new genres can be added or existing genres can be edited or deleted:
![User Story testing](./static/user_story_test_screenshots/manage_genres_admin_2_UStesting.png)

<br>

- As a site admin I can view messages submitted via the contact form so that I can communicate with site users.

Within the admin panel, the admin can select Contacts:
![User Story testing](./static/user_story_test_screenshots/view_messages_admin_UStesting.png)

Here, the admin can click into messages to read them: 
![User Story testing](./static/user_story_test_screenshots/view_messages_admin_2_UStesting.png)

![User Story testing](./static/user_story_test_screenshots/view_messages_admin_3_UStesting.png)

<br>

- As a site admin I can remove users so that they will no longer be able to post unsuitable content.

Within the admin panel, the admin can select Users: 
![User Story testing](./static/user_story_test_screenshots/manage_users_admin_UStesting.png)

Here, the admin can select users to delete: 
![User Story testing](./static/user_story_test_screenshots/manage_users_admin_2_UStesting.png)

The admin is then informed that all objects related to that user will also be deleted, and they are asked to confirm they are sure they want to delete that user:
![User Story testing](./static/user_story_test_screenshots/manage_users_admin_3_UStesting.png)


## Site User

- As a site user I can register for an account to be able to post reviews and comments.

The user can select 'register' from either the navigation or the homepage header:
![User Story testing](./static/user_story_test_screenshots/register_user_UStesting.png)

The user can then fill out the register form and click 'Register': 
![User Story testing](./static/user_story_test_screenshots/register_user_2_UStesting.png)

The user is then redirected to the homepage, where a pop-up message informs them that they are logged in successfully. The 'Add Review" button also appears in header:
![User Story testing](./static/user_story_test_screenshots/register_user_3_UStesting.png)

<br>

- As a returning site user I can login to the website so that I can post reviews and comments.

The user can select 'log in' from either the navigation or the homepage header:
![User Story testing](./static/user_story_test_screenshots/register_user_UStesting.png)

The user can log in via the form: 
![User Story testing](./static/user_story_test_screenshots/login_user_UStesting.png)

The user is then redirected to the homepage, where a pop-up message informs them that they are logged in successfully. The 'Add Review" button also appears in header:
![User Story testing](./static/user_story_test_screenshots/register_user_3_UStesting.png)

Once a user is registered and/or logged in, the comments form also becomes available in the review detail: 
![User Story testing](./static/user_story_test_screenshots/login_user_3_UStesting.png)

<br>

- As a returning user I can log out my account to ensure security on any shared devices I may use.

The logged in user can select 'log out' from the navigation:
![User Story testing](./static/user_story_test_screenshots/logout_user_UStesting.png)

Here, the user is asked if they are sure they want to log out: 
![User Story testing](./static/user_story_test_screenshots/logout_user_2_UStesting.png)

The user is then redirected to the homepage, where a pop-up message informs them that they are logged out successfully: 
![User Story testing](./static/user_story_test_screenshots/logout_user_3_UStesting.png)

<br>

- As a site admin/user I can create book reviews to share with other users.

The logged in user can select 'Add review here' from the header:
![User Story testing](./static/user_story_test_screenshots/add_review_user_UStesting.png)

The user can then fill out and submit a form, which is then sent to the admin for approval:
![User Story testing](./static/user_story_test_screenshots/add_review_user_2_UStesting.png)

Upon submitting, the user is redirected to the homepage, where a pop-up message informs them that their review has been submitted for approval:
![User Story testing](./static/user_story_test_screenshots/add_review_user_3_UStesting.png)

<br>

- As a site admin/user I can update and delete reviews written by me so that I can manage my own content.



