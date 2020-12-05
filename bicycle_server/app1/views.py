from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from bicycle_server.app1.serializers import UserSerializer, GroupSerializer, PlayerSerializer
from bicycle_server.app1.models import Player
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def players(request, page=1):

    # permission_classes = [permissions.IsAuthenticated]

    queryset = Player.objects.all()[(page-1)*10:page*10]
    serializer = PlayerSerializer(queryset, many=True)
    return JsonResponse(serializer.data, 
        safe=False, 
        json_dumps_params={'ensure_ascii': False}
    )