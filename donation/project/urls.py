from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('gerenciarUsuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('campanhas/', views.campanhas, name='campanhas'),
    path('criarCampanha/', views.criar_campanha, name='criar_campanha'),
    path('editarCampanha/<int:id_campanha>', views.editar_campanha, name='editar_campanha'),
    path('doar/<int:id_campanha>', views.doar_campanha, name='doar_campanha')
]
