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

def player_no(request, player_nm, player_no):

    # permission_classes = [permissions.IsAuthenticated]
    
    q_sum = Q(racer_no=player_no) & Q(racer_nm=player_nm)

    queryset = Player.objects.filter(q_sum)
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )

def player_name(request, player_nm):

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Player.objects.filter(racer_nm=player_nm)
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

def results(request, year, month, day, race_no):
    
    queryset = Result.objects.filter(
        Q(stnd_year=year) & 
        Q(race_day=f'{month.zfill(2)}{day.zfill(2)}') & 
        Q(race_no=race_no)).all()

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


def matches(request, player_no_1, player_no_2):
    
    q1 = Q(player_no=player_no_1) & Q(partn_player_no=player_no_2)
    q2 = Q(player_no=player_no_2) & Q(partn_player_no=player_no_1)
    
    queryset = Match.objects.filter(q1 | q2).all()
    serializer = MatchSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )