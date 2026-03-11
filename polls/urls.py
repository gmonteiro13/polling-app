from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # abaixo, troca-se o question_id por pk, que é o nome padrão para a chave primária.
    # o DetailView espera que a chave primária seja chamada pk ou id, então usando pk, não precisamos alterar o código do DetailView
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]