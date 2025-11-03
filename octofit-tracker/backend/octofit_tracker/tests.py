from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', team='Marvel')
        self.assertEqual(user.name, 'Test User')

    def test_team_creation(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Push Ups', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
