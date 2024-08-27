import time
from django.test import SimpleTestCase
from django.urls import reverse

class OtherTests(SimpleTestCase):
    def test_404_error_for_nonexistent_pages(self):
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)

from django.urls import reverse

class HomePageViewTests(SimpleTestCase):
    
    def test_home_page_accessible(self):
        """Test if the home page is accessible"""
        response = self.client.get(reverse('home'))
        assert response.status_code == 200

    def test_home_page_title(self):
        """Test title"""
        response = self.client.get(reverse('home'))
        assert b'<title>Her New Melbourne</title>' in response.content

    def test_seo_elements_present(self):
        """Test if there are SEO elements"""
        response = self.client.get(reverse('home'))
        assert b'<meta name="description"' in response.content
        assert b'<meta name="keywords"' in response.content

    def test_page_load_time(self):
        """Test how long the page takes to load"""
        start_time = time.time()
        response = self.client.get(reverse('home'))
        end_time = time.time()
        assert response.status_code == 200
        assert end_time - start_time < 2

    def test_responsiveness(self):
        """Test if the home page can run on other devices"""
        response = self.client.get(reverse('home'), HTTP_USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X)')
        assert response.status_code == 200
        assert b'<meta name="viewport"' in response.content 

    def test_home_page_status_code(self):
        """Test if the home page returns a status code 200."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        """Test if the correct template is used for the home page."""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'HomePage.html')


class LandingPageViewTests(SimpleTestCase):
    def test_landing_page_accessible(self):
        """Test if the landing page is accessible"""
        response = self.client.get('/')
        assert response.status_code == 200

    def test_landing_page_title(self):
        """Test title"""
        response = self.client.get('/')
        assert b'<title>Her New Melbourne</title>' in response.content

    def test_seo_elements_present(self):
        """Test if there are SEO elements"""
        response = self.client.get('/')
        assert b'<meta name="description"' in response.content
        assert b'<meta name="keywords"' in response.content

    def test_page_load_time(self):
        """Test how long the page takes to load"""
        start_time = time.time()
        response = self.client.get('/')
        end_time = time.time()
        assert response.status_code == 200
        assert end_time - start_time < 2

    def test_responsiveness(self):
        """Test if the landing page can run on other websites"""
        response = self.client.get('/', HTTP_USER_AGENT='Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X)')
        assert response.status_code == 200
        assert b'<meta name="viewport"' in response.content 

    def test_landing_page_status_code(self):
        """Test if the landing page returns a status code 200."""
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)

    def test_landing_page_template_used(self):
        """Test if the correct template is used for the landing page."""
        response = self.client.get(reverse('landing'))
        self.assertTemplateUsed(response, 'LandingPage.html')