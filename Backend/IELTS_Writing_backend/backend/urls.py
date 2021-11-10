from django.urls import path, include
from .views import Acedamic_Writing_Task1_Viewset, General_Writing_Task1_Viewset, Academic_General_Writing_Task2_Viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'acedamic_task1', Acedamic_Writing_Task1_Viewset)
router.register(r'general_task1', General_Writing_Task1_Viewset)
router.register(r'aced_gen_task2', Academic_General_Writing_Task2_Viewset)


urlpatterns = [
    path('', include(router.urls))
]