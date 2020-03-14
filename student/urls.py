from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('add', views.add, name='add'),
	path('addNew', views.addNew, name='addNew'),
]
