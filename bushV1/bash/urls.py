from django.urls import path
from .views import *


urlpatterns = [
    path('', bash_main),
    path('best', bash_best),
    path('random', bash_random),
    path('byrating', bash_byrating),
    path('abyss', bash_abyss),
    path('abysstop', bash_abysstop),
    path('abyssbest', bash_abyssbest),
    path('abyss/', bash_abyss),
    path('faq/', bash_faq),
]
