from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings

@api_view(['GET'])
def api_root(request, format=None):
    base_url = "https://obscure-acorn-vrx9qqwrv5g3w67q-8000.app.github.dev" if settings.DEBUG else request.build_absolute_uri('/')
    return Response({
        'users': f"{base_url}api/users/",
        'teams': f"{base_url}api/teams/",
        'activities': f"{base_url}api/activities/",
        'leaderboard': f"{base_url}api/leaderboard/",
        'workouts': f"{base_url}api/workouts/",
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
