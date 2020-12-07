from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bicycle_server.app1.serializers import PlayerSerializer, EntrySerializer, ResultSerializer, MatchSerializer, ScehduleSerializer
from bicycle_server.app1.models import Player, Schedule, Entry, Result, Match
from django.http import JsonResponse

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

def results(request, page):
    
    queryset = Result.objects.all()[(page-1)*20:page*20]
    serializer = ResultSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )


def entries(request, page):
    
    queryset = Entry.objects.all()[(page-1)*20:page*20]
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

