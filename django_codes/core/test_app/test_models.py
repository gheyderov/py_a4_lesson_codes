from core.models import Contact
from django.test import TestCase


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data = {
            'first_name': 'John',
            'email' : 'admin@google.com',
            'subject': 'test',
            'message': 'test message'
        }
        cls.contact = Contact.objects.create(**cls.data)

    def test_create_method(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    @classmethod
    def tearDownClass(cls) -> None:
        pass