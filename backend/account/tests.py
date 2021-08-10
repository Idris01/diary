from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Todo

from .views import TodoView
# Create your tests here.
class AccountTest( APITestCase):
    
    def setUp(self):
        todo=Todo(title="Sleep", description="Sleep at 9pm", completed=True)
        todo.save()
    

    def test_initial_todo_is_one(self):
        count=Todo.objects.count()
        self.assertEqual(count,1)


    def test_post_data_created(self):
        data={
                "title": "Pray",
                "description":"Pray at Masjid",
                "completed":False,
                }
        url=reverse("task-list")
        response=self.client.post(url,data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(Todo.objects.count(),1)

