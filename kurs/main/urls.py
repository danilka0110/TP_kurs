from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project', views.project, name='project'),
    path('contacts', views.contacts, name='contacts'),
    path('create', views.create, name='create'),
    path('project/<int:pk>', views.LocsDetailView.as_view(), name='locs-detail'),
    path('project/<int:pk>/update', views.LocsUpdateView.as_view(), name='locs-update'),
    path('project/<int:pk>/delete', views.LocsDeleteView.as_view(), name='locs-delete'),
]
