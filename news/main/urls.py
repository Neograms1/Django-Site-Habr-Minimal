from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = 'home'),
    path('about',views.about,name = 'about'),
    path('<int:pk>',views.NewsDetaiView.as_view(),name = 'news'),
    path('create',views.about)

]