from django.shortcuts import render, redirect, get_object_or_404
# We import the redirect function, which is used to redirect the user to a different URL.
# We import the get_object_or_404 function, which retrieves an object from the database
# or raises an HTTP 404 (Not Found) error (if the object is not found).


# movies = [
#     {
#         'id': 1,
#         'name': 'Inception',
#         'price': 12,
#         'description': 'A mind-bending heist thriller.'
#     },
#     {
#         'id': 2,
#         'name': 'Avatar',
#         'price': 13,
#         'description': 'A journey to a distant world and  the battle for resources.'
#     },
#     {
#         'id': 3,
#         'name': 'The Dark Knight',
#         'price': 14,
#         'description': 'Gotham\'s vigilante faces the Joker.'
#     },
#     {
#         'id': 4,
#         'name': 'Titanic',
#         'price': 11,
#         'description': 'A love story set against the backdrop of the sinking Titanic.',
#     },
# ]
from .models import Movie, Review
# We import the Review model, which will be used to create new reviews.
from django.contrib.auth.decorators import login_required
# We import login_required, which is used to verify that only logged users can access the create_review function.
# If a guest user attempts to access this function via the corresponding URL, they will be redirected to the login page.


def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    # template_data = {}
    # template_data['title'] = 'Movies'
    # template_data['movies'] = movies
    # template_data = {'title': 'Movies', 'movies': movies}
    # template_data['movies'] = Movie.objects.all()
    # template_data = {'title': 'Movies', 'movies': Movie.objects.all()}
    template_data = {'title': 'Movies', 'movies': movies  }

    return render(request, 'movies/index.html',{'template_data': template_data})

def show(request, id):
    # movie = movies[id - 1]
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    # We retrieve all review objects that are associated with the movie that we are showing.

    # template_data = {}
    # template_data['title'] = movie['name']
    # template_data['movie'] = movie
    # template_data = {'title': movie['name'], 'movie': movie}
    # template_data['reviews'] = reviews
    template_data = {'title': movie.name , 'movie': movie,  'reviews': reviews}
    return render(request, 'movies/show.html',{'template_data': template_data})
    # We add those reviews to the template_data dictionary, which is passed to the movies/show.html template.

@login_required
def create_review(request, id): # We create the create_review function that handles creating a review.
    # The create_review takes two arguments: the request that contains information about the HTTP request,
    # and the id, which represents the ID of the movie for which a review is being created.
    if request.method == 'POST' and request.POST['comment'] != '':
        # Then, we check whether the request method is POST
        # and the comment field in the request’s POST data is not empty.
        movie = Movie.objects.get(id=id)
        # We retrieve the movie using Movie.objects.get(id=id) based on the provided id.
        review = Review() # We create a new Review object.
        review.comment = request.POST['comment']
        # We set the comment based on the comments collected in the form
        review.movie = movie
        # We set the movie, based on the retrieved movie from the database
        review.user = request.user
        # We set the user, based on the authenticated user who submitted the form
        review.save()
        # Finally, we save the review to the database and redirect the user to the movie show page.
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
    # In the else case, we redirect the user to the movie show page using the redirect('movies.show', id=id) code.

@login_required
def edit_review(request, id, review_id):
    # We use the @login_required decorator to ensure that the edit_review function can only be accessed by authenticated users.
    # If an unauthenticated user tries to access this function, they will be redirected to the login page.
    # We define the edit_review function, which takes three parameters: the request, the movie ID, and the review ID.

    review = get_object_or_404(Review, id=review_id)
    # We retrieve the Review object with the given review_id.
    # If the review does not exist, a 404 error will be raised.
    if request.user != review.user:
        # We check whether the current user (request.user) is the owner of the review to be edited (review.user)
        # If the user does not own the review, the function redirects them to the movie.show page.
        return redirect('movies.show', id=id)
    if request.method == 'GET':
        # Then, we check whether the request method is GET.
        # In that case, the function prepares data for the template and renders the edit_review.html template.

        # template_data = {}
        # template_data['title'] = 'Edit Review'
        # template_data['review'] = review
        template_data = {'title': 'Edit Review', 'review': review}
        return render(request, 'movies/edit_review.html',{'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        # If the request method is POST and the comment field in the request’s POST data is not empty,
        # the function proceeds to update the review and redirects the user to the movie show page.
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
    # In any other case, the function redirects the user to the movie show page.

@login_required
def delete_review(request, id, review_id):
    # We use the @login_required decorator
    # to ensure that the delete_review function can be only accessed by authenticated users.
    # If an unauthenticated user tries to access this function, they will be redirected to the login page.
    # We retrieve the Review object with the given review_id that belongs to the current user (request.user).
    review = get_object_or_404(Review, id=review_id, user=request.user)
    # If the review does not exist, or if the user does not own the review, an HTTP 404 error will be raised.
    review.delete()
    # We delete the review from the database using the Django model’s delete() method.
    return redirect('movies.show', id=id) # We redirect to the previous movie show page

