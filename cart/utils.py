def calculate_cart_total(cart, movies_in_cart):
    # We define the calculate_cart_total function, which takes two parameters: cart and movies_in_cart.
    # The cart parameter is a dictionary that represents the user’s shopping cart.
    # Remember that the keys are strings representing movie IDs,
    # and the values are strings representing the quantities of each movie in the cart.
    # The movies_in_cart parameter is a list of Movie objects representing the movies in the cart.
    total = 0
    # We initialize a total variable by 0.
    for movie in movies_in_cart: # We iterate through the list of movies in the cart.
        quantity = cart[str(movie.id)]
        total += movie.price * int(quantity)
        # For each movie, we extract the corresponding quantity added to the cart and multiply it by the movie’s price.
        # Then, we add the total cost for the movie to the total variable.
    return total # Finally, we return the total variable.