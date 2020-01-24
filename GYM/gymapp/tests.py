from django.test import TestCase, Client
from .models import Gym
from django.urls import reverse, resolve



# Create your tests here.
class ModelTestCase(TestCase):
    def test_uploadata_fields_blank(self):
        WO =Gym.objects.create(workoutname="muscles")
        self.assertTrue(WO.uploadata_fields_blank())


    def test_workOut_Len(self):
       WO =Gym.objects.create(workoutname="muscles")
       self.assertTrue(WO.TestWorkout())

    def test_Email_Valid(self):
       WO =Gym.objects.create(email="sandesh5432@gmail.com")
       self.assertTrue(WO.email_fields_blank())

    def test_valid_desc_len(self):
        WO =Gym.objects.create(workoutdesc="asasasa asasasa sasasasa aa aasasasasasa")
        self.assertTrue(WO.workoutdes_field_blank())
       