from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    TiquetListView,
    TiquetCreateview,
    TiquetDetailView,
    ResultatView

)
from . import views

urlpatterns = [
    path('', views.home, name='pari-home'),#voir accueil
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#voir detail d'un poste
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),#mettre a jour un poste
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),#supprimer un poste
    path('post/new/', PostCreateView.as_view(), name='post-create'),#crer un poste
    path('forum/', PostListView.as_view(), name='pari-forum'),#voir toutes les discutions du forum
    path('tiquet/', views.listiquet, name='pari-tiquet'),#voir toutes les tiquets de pari
    path('tiquet/<int:pk>/', TiquetDetailView.as_view(), name='pari-detail'),#details d'un tiquet
    path('tiquet/new/', TiquetCreateview.as_view(), name='pari-create'),#details d'un tiquet
    path('resultat/', ResultatView.as_view(), name='pari-resultat'),#details d'un tiquet
    
]