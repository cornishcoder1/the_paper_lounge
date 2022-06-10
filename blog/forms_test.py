from django.test import TestCase
from .forms import ReviewForm, CommentForm
from contactus.forms import ContactForm


class TestAddReviewForm(TestCase):
    """ Unit test for Add Review Form """
    def test_book_title_is_required(self):
        """book title field"""
        form = ReviewForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_book_author_is_required(self):
        """book author field"""
        form = ReviewForm(({'author': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_genre_is_required(self):
        """genre field"""
        form = ReviewForm(({'genre': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('genre', form.errors.keys())
        self.assertEqual(form.errors['genre'][0], 'This field is required.')

    def test_rating_is_required(self):
        """rating field"""
        form = ReviewForm(({'rating': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_content_is_required(self):
        """Write your Review Here field"""
        form = ReviewForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')


class TestCommentForm(TestCase):
    """Unit test for comment form"""
    def test_body_is_required(self):
        """comment body field"""
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """fields metaclass"""
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )


class TestContactForm(TestCase):
    """Unit test for contact form"""
    def test_first_name_is_required(self):
        """first name field"""
        form = ContactForm(({'fname': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('fname', form.errors.keys())
        self.assertEqual(form.errors['fname'][0], 'This field is required.')

    def test_last_name_is_required(self):
        """last name field"""
        form = ContactForm(({'lname': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('lname', form.errors.keys())
        self.assertEqual(form.errors['lname'][0], 'This field is required.')

    def test_email_is_required(self):
        """email field"""
        form = ContactForm(({'email': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_body_is_required(self):
        """message field"""
        form = ContactForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """fields metaclass"""
        form = ContactForm()
        self.assertEqual(
            form.Meta.fields, ('fname', 'lname', 'email', 'body',)
        )
        