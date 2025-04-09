from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@hmhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        db.users.insert_many([user.__dict__ for user in users])

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Avengers', members=[users[0]._id, users[1]._id]),
            Team(_id=ObjectId(), name='Hackers', members=[users[2]._id, users[3]._id]),
        ]
        db.teams.insert_many([team.__dict__ for team in teams])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0]._id, activity_type='Running', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[1]._id, activity_type='Cycling', duration=timedelta(minutes=45)),
        ]
        db.activity.insert_many([activity.__dict__ for activity in activities])

        # Create leaderboard
        leaderboard = [
            Leaderboard(_id=ObjectId(), user=users[0]._id, score=100),
            Leaderboard(_id=ObjectId(), user=users[1]._id, score=80),
        ]
        db.leaderboard.insert_many([entry.__dict__ for entry in leaderboard])

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Morning Yoga', description='A relaxing yoga session to start the day'),
            Workout(_id=ObjectId(), name='HIIT', description='High-intensity interval training for fat burning'),
        ]
        db.workouts.insert_many([workout.__dict__ for workout in workouts])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
