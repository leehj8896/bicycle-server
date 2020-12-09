from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bicycle_server.app1.serializers import PlayerSerializer, EntrySerializer, ResultSerializer, MatchSerializer, ScehduleSerializer, RaceSerializer
from bicycle_server.app1.models import Player, Schedule, Entry, Result, Match
from django.http import JsonResponse
from django.db.models import Q

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

def players(request, page):

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Player.objects.all()[(page-1)*20:page*20]
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def schedules(request, page):
    
    queryset = Schedule.objects.all()[(page-1)*20:page*20]
    serializer = ScehduleSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def results(request, year, month, day):
    
    queryset = Result.objects.filter(
        Q(stnd_year=year) & Q(race_day=f'{month.zfill(2)}{day.zfill(2)}')).all()

    serializer = ResultSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def races(request, year, month, day):
    
    date = f'{year}.{month.zfill(2)}.{day.zfill(2)}'
    
    queryset = Entry.objects.filter(race_dt=date).values(
        # 'id',
        # 'meet',
        # 'stnd_year',
        # 'tms',
        # 'day_ord',
        # 'race_dt',
        'race_no',
    ).distinct()
    serializer = RaceSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def entries(request, year, month, day, race_no):
    
    date = f'{year}.{month.zfill(2)}.{day.zfill(2)}'
    
    queryset = Entry.objects.filter(Q(race_dt=date) & Q(race_no=race_no)).all()
    serializer = EntrySerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def matches(request, page):
    
    queryset = Match.objects.all()[(page-1)*20:page*20]
    serializer = MatchSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

