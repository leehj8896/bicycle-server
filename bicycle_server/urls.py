from django.urls import include, path
from rest_framework import routers
from bicycle_server.app1 import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('players/<int:page>/', views.players),
    path('schedules/<int:page>/', views.schedules),
    path('entries/<int:page>/', views.entries),
    path('results/<int:page>/', views.results),
    path('matches/<int:page>/', views.matches),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
