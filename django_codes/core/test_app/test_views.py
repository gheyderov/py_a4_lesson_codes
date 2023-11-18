from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.forms import ContactForm


class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        client = Client()
        cls.url = reverse_lazy('contact')
        cls.response = client.get(cls.url)
        cls.data = {
            'first_name': 'John',
            'email' : 'admingoogle.com',
            'subject': 'test',
            'message': 'test message'
        }
        cls.post_invalid = client.post(cls.url, data=cls.data)
    
    def test_url(self):
        self.assertEqual(self.url, '/en/contact/')

    def test_response_status_code(self):
        
        self.assertEqual(self.response.status_code, 200)

    def test_response_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')     

    def test_response_context(self):
        self.form = self.response.context['form']
        self.assertIsInstance(self.form, ContactForm)

    def test_response_form_errors(self):
        form = self.post_invalid.context['form']
        self.assertFalse(form.is_valid())

    
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass