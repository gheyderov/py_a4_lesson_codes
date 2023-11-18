from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from stories.models import Category, Tag
import os
from django.conf import settings


class RecipeApiViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        cls.url = reverse_lazy('recipe-list')
        cls.response = client.get(cls.url)
        category = Category.objects.create(title = 'Category 1')
        tag = Tag.objects.create(title = 'Tag 1')
        file_path = os.path.join(settings.MEDIA_ROOT, 'recipe_images/recipe_1.jpeg')
        cls.data = {
            'title' : 'Recipe 1',
            'category' : category.id,
            'tags' : tag.id,
            'small_description' : 'some text',
            'description' : 'some text',
            'image' : (open(file_path, 'rb')),
            'cover_image' : (open(file_path, 'rb')),
        }
        cls.post_valid = client.post(cls.url, data=cls.data)

    def test_url(self):
        self.assertEqual(self.url, '/api/recipes/')

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_status_code(self):
        self.assertEqual(self.post_valid.status_code, 201)



    
    
    @classmethod
    def tearDownClass(cls) -> None:
        pass