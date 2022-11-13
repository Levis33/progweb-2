from django.urls import path
from project import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),

    path('campanhas/', views.campanhas_ativas, name='campanhas'),
    path('gerenciarcampanhas/', views.gerenciar_campanhas, name='gerenciar_campanhas'),
    path('criarcampanha/', views.criar_campanha, name='criar_campanha'),
    path('editarcampanha/<int:id_campanha>', views.editar_campanha, name='editar_campanha'),

    path('doar/<int:id_campanha>', views.doar_campanha, name='doar_campanha'),

    path('gerenciarusuarios/', views.gerenciar_usuarios, name='gerenciar_usuarios'),
    path('gerenciarusuarios/<int:user_id>/editar/', views.editar_usuario, name='editar_usuarios'),

    path('403/', views.handler_403, name='403'),

]

