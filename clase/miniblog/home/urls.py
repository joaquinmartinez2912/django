from django.urls import path

from home.views import (
    index_view,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('', index_view, name="index"), 
    path('login/', view=LoginView.as_view(), name="login"),
    path('logout/', view=LogoutView.as_view(), name="logout")
]

