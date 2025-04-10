from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        User.objects.create(email='john.doe@example.com', name='John Doe', age=25)
        User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=30)

        # Create test teams
        Team.objects.create(name='Team Alpha', members=['john.doe@example.com', 'jane.smith@example.com'])

        # Create test activities
        Activity.objects.create(user=User.objects.get(email='john.doe@example.com'), type='Running', duration=30)
        Activity.objects.create(user=User.objects.get(email='jane.smith@example.com'), type='Cycling', duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(user=User.objects.get(email='john.doe@example.com'), score=100)
        Leaderboard.objects.create(user=User.objects.get(email='jane.smith@example.com'), score=150)

        # Create test workouts
        Workout.objects.create(name='Push-ups', description='Do 20 push-ups')
        Workout.objects.create(name='Sit-ups', description='Do 30 sit-ups')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
