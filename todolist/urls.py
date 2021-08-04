from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('delete/<list_id>', views.delete.as_view(), name="delete"),
    path('cross_off/<list_id>', views.cross_off.as_view(), name="cross_off"),
    path('uncross/<list_id>', views.uncross.as_view(), name="uncross"),
    path('edit/<list_id>', views.edit.as_view(), name="edit"),
]

