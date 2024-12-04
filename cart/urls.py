from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='cart.index'),
    path('<int:id>/add/', views.add, name='cart.add'),
    path('clear/', views.clear, name='cart.clear'),
    path('purchase/', views.purchase, name='cart.purchase'),
]
# The <int:id> part indicates that this path expects an integer value to be passed from the URL and that
# the integer value will be associated with a variable named id.
# The id variable will be used to identify which movie we want to add to the cart.
# For example, the cart/1/add a path indicates that we want to add the movie with id=1 to the cart.