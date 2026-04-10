from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete individually for Djongo compatibility)
        for obj in Leaderboard.objects.all():
            obj.delete()
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 50 pushups', suggested_for='marvel')
        running = Workout.objects.create(name='Running', description='Run 5km', suggested_for='dc')

        # Activities
        Activity.objects.create(user=tony, activity_type='pushups', duration=10, date=date(2024, 1, 1))
        Activity.objects.create(user=steve, activity_type='running', duration=30, date=date(2024, 1, 2))
        Activity.objects.create(user=bruce, activity_type='pushups', duration=15, date=date(2024, 1, 3))
        Activity.objects.create(user=clark, activity_type='running', duration=25, date=date(2024, 1, 4))

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=150, rank=1)
        Leaderboard.objects.create(user=steve, score=120, rank=2)
        Leaderboard.objects.create(user=bruce, score=110, rank=3)
        Leaderboard.objects.create(user=clark, score=100, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
