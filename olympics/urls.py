"""olympics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.views import (EventViewSet,
    NOCViewSet,
    SportViewSet,
    GameViewSet,
    AthleteViewSet,
    CompetitionViewSet,
    MedalViewSet)

# Instaciating Router and registering ViewSets
router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'nocs', NOCViewSet)
router.register(r'sports', SportViewSet)
router.register(r'games', GameViewSet)
router.register(r'athletes', AthleteViewSet)
router.register(r'competitions', CompetitionViewSet)
router.register(r'medals', MedalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
