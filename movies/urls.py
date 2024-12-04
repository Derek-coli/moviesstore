from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/',views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
]

# The <int:id> part indicates that this path expects an integer value to be passed from the URL and that
# the integer value will be associated with a variable named id.
# The id variable will be used to identify to which movie the review that we want to create is linked. #
# For example, if the form is submitted to movies/1/review/create,
# it indicates that the new review will be associated with the movie with id=1.


# This path captures two integer values (the movie ID and review ID)
# from the URL and passes them to the edit_review function as arguments.