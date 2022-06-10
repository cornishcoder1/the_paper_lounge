from django.test import TestCase

# Unit Testing - Views


class TestIndexView(TestCase):
    "Unit test for home page"
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class TestAboutView(TestCase):
    "Unit test for about page"
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


class TestAddReviewView(TestCase):
    "Unit test for add review page"
    def test_add_review_page(self):
        response = self.client.get('/add-review/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')


