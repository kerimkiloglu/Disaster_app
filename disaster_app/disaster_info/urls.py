from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import DisasterViewSet, LocationViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'disasters', DisasterViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'locations',LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("home/", views.disaster_info, name="disaster-info-home"),
    path("about/", views.about, name="disaster-info-about"),
    path('', views.disaster_list, name='disaster_list'),
    path('disaster/<int:pk>/', views.disaster_detail, name='disaster_detail'),
    path('alerts/', views.alert_list, name='alert_list'),
]
