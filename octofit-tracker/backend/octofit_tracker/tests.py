from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        response = self.client.post('/users/', {'email': 'test@example.com', 'name': 'Test User', 'age': 25})
        self.assertEqual(response.status_code, 201)

class TeamTests(APITestCase):
    def test_create_team(self):
        response = self.client.post('/teams/', {'name': 'Team A', 'members': []})
        self.assertEqual(response.status_code, 201)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        response = self.client.post('/activity/', {'user': 1, 'type': 'Running', 'duration': 30})
        self.assertEqual(response.status_code, 201)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard_entry(self):
        response = self.client.post('/leaderboard/', {'user': 1, 'score': 100})
        self.assertEqual(response.status_code, 201)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        response = self.client.post('/workouts/', {'name': 'Push-ups', 'description': 'Do 20 push-ups'})
        self.assertEqual(response.status_code, 201)
