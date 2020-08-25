from django.urls import path

from .views import ListPokemon, GetPokemon

urlpatterns = [
    path('', ListPokemon.as_view()),
    path('<pk>/', GetPokemon.as_view())
]