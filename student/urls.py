from django.urls import path

from . import views

app_name = 'student'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/edit', views.edit, name='edit'),
	path('makeEdits', views.makeEdits, name='makeEdits'),
	path('add', views.add, name='add'),
	path('addNew', views.addNew, name='addNew'),
	path('<int:pk>/delete', views.delete, name='delete'),
	path('search', views.search, name='search'),
	path('ajax_searchsort', views.ajax_searchsort, name='ajax_searchsort'),
]
