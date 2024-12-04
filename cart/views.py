from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
# We import the redirect and get_object_or_404 functions.
from movies.models import Movie
# We also import the Movie model from the “movies” app.
from .utils import calculate_cart_total
# We import the calculate_cart_total function from the utils file.
from .models import Order, Item
# We import the Order and Item models from the current app directory.
from django.contrib.auth.decorators import login_required
# We import the login_required decorator.


def index(request):
    # We define the index function.
    cart_total = 0
    movies_in_cart = []
    # We initialize the cart_total to 0, and movies_in_cart as an empty list.
    cart = request.session.get('cart', {})
    # We retrieve the cart information from the session using request.session.get('cart', {}).
    movie_ids = list(cart.keys())
    # We extract the movie IDs that were added to the cart based on the cart keys.
    if movie_ids:
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        # If there are any movie IDs in the cart,
        # the function queries the database for movies with those IDs using Movie.objects.filter(id__in=movie_ids).
        cart_total = calculate_cart_total(cart, movies_in_cart)
        #  Additionally, we calculate the total cost of the movies in the cart using the calculate_cart_total function,
        #  which updates the cart_total variable.
    # template_data = {}
    # template_data['title'] = 'Cart'
    # template_data['movies_in_cart'] = movies_in_cart
    # template_data['cart_total'] = cart_total
    template_data = {'title': 'Cart', 'movies_in_cart': movies_in_cart, 'cart_total': cart_total}
    # Finally, we prepare the template_data dictionary and render the cart/index.html template.
    return render(request, 'cart/index.html', {'template_data': template_data})


def add(request, id):
    # add_to_cart(request, id):
    # We define the add function, which takes two parameters: the request and the movie ID.
    get_object_or_404(Movie, id=id)
    # We fetch the Movie object with the given id from the database (by using the get_object_or_404 function).
    # If no such object is found, a 404 (Not Found) error is raised.
    cart = request.session.get('cart', {})
    # We check the session storage for a key called 'cart'.
    # If the key exists, we retrieve the value associated with it and assign it to the cart variable.
    # If the key does not exist, a {} empty dictionary is assigned to the cart variable.
    cart[id] = request.POST['quantity']
    # We modify the cart variable.
    # We add a new key to the cart dictionary based on the movie ID,
    # and the corresponding value based on the movie quantity the user wants to add to
    # the cart. (We will collect quantity through an HTML form later.)
    # For example, if the user wants to add 2 movies with id=1,
    # a new key/value such as this cart["1"] = "2" will be added to the dictionary.
    request.session['cart'] = cart
    # The updated cart dictionary is then saved back to the session using request.session['cart'] = cart.
    # Return redirect('home.index')
    return redirect('cart.index')
    # After updating the cart, we redirect the user to the home page (home.index).

def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')
# We just update the user’s cart session to an empty dictionary.
# This removes all previous movies added to the cart, and we redirect the user to the cart page.


@login_required
def purchase(request):
# We use the login_required decorator to ensure that the user must be logged in to access the purchase function.
# We define the purchase function, which will handle the purchase process.
    cart = request.session.get('cart', {})
    # We retrieve the cart data from the user’s session.
    # The cart variable will contain a dictionary with movie IDs as keys and quantities as values.
    movie_ids = list(cart.keys())
    # We retrieve the movie IDs stored in the cart dict and convert them into a list named movie_ids.
    if (movie_ids == []):
        # We check if the movie_ids list is empty (which indicates the cart is empty).
        # In this case, the user is redirected to the cart.index page (here, the purchase function finalizes its execution).
        return redirect('cart.index')
    # If the cart is not empty, we continue the purchase process.
    movies_in_cart = Movie.objects.filter(id__in=movie_ids)
    # We retrieve movie objects from the database based on the IDs stored in the cart using Movie.objects.filter(id__in=movie_ids.
    cart_total = calculate_cart_total(cart, movies_in_cart)
    # We calculate the total cost of the movies in the cart using the calculate_cart_total() function.
    order = Order()
    # We create a new Order object.
    order.user = request.user
    # We set its attributes such as user (the logged-in user) and total (the cart total),
    order.total = cart_total
    order.save()
    # and save it to the database.
    for movie in movies_in_cart:
    # We iterate over the movies in the cart.
        item = Item()
    # We create an Item object for each movie in the cart. For each Item,
        item.movie = movie
        item.price = movie.price
        item.order = order
        item.quantity = cart[str(movie.id)]
        item.save()
    # we set its price and quantity, link the corresponding movie and order, and save it to the database.
    request.session['cart'] = {}
    # After the purchase is completed,
    # we clear the cart in the user’s session by setting request.session['cart'] to an empty dictionary.
    # template_data = {}
    # template_data['title'] = 'Purchase confirmation'
    # template_data['order_id'] = order.id
    template_data = {'title': 'Purchase confirmation', 'order_id': order.id}
    # We prepare the data to be sent to the purchase confirmation template.
    # This data includes the title of the page and the ID of the created order.
    return render(request, 'cart/purchase.html', {'template_data': template_data})
    # Finally, we render the cart/purchase.html template.

