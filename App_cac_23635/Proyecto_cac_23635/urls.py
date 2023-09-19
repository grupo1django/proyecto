from django.urls import path
from . import views


urlpatterns = [
      path("", views.index, name="index"),
      #path ("loging/ <str:usuarios>",views.loging, name = "loging_usuarios"),"""
      path ("loging",views.loging, name = "loging_usuarios"),
      path ("farmacia", views.farmacia, name="farmacia")


]