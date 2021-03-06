from django.urls import include, path
from rest_framework import routers
from bicycle_server.app1 import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('players/<int:page>/', views.players),
    path('player/<str:player_nm>/', views.player_name),
    path('player/<str:player_nm>/<str:player_no>/', views.player_no),
    path('schedules/<int:page>/', views.schedules),
    path('races/<str:year>/<str:month>/<str:day>/', views.races),
    path('entries/<str:year>/<str:month>/<str:day>/<str:race_no>/', views.entries),
    path('results/<str:year>/<str:month>/<str:day>/<str:race_no>/', views.results),
    path('matches/<str:player_no_1>/<str:player_no_2>/', views.matches),
    
    path('player_prize_rate/<str:player_nm>/', views.player_prize_rate),
    path('match_graph/<str:player_nm_1>/<str:player_nm_2>/', views.match_graph),
    path('player_grade/<str:player_nm>/', views.player_grade),

]
