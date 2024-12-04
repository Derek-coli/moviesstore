from django.db import models
from django.contrib.auth.models import User
# We import the User model from Django’s django.contrib.auth.models module.
from movies.models import Movie
# We import the Movie model from the movies app.


class Order(models.Model):
    # We define a Python class named Order, which inherits from models.Model.
    # This means that Order is a Django model class.
    id = models.AutoField(primary_key=True)
    # id: This is an AutoField, which automatically increments its value for each new record added to the database.
    # The primary_key=True parameter specifies that this field is the primary key for the table,
    # uniquely identifying each record.
    total = models.IntegerField()
    # total: This is a IntegerField, which represents the total amount of the order.It stores integer values.
    date = models.DateTimeField(auto_now_add=True)
    # date: This is a DateTimeField , which represents the date and time when the order was created.
    # auto_now_add=True ensures that the date and time are automatically set to the current date and time when the order is created.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user: This is a foreign key relationship to the User model,
    # which establishes a many-to-one relationship between orders and users.
    # It means that each order is associated with a single user, and each user can have multiple orders.
    # on_delete=models.CASCADE specifies that if the related user is deleted, the associated orders will also be deleted.
    def __str__(self):
        # __str__ is a method that returns a string representation of the order.
        # In this case, it returns a string composed of the order ID and the username of the user who placed the order.
        return str(self.id) + ' - ' + self.user.username


class Item(models.Model):
    # We define a Python class named Item, which inherits from models.Model.
    # This means that Item is a Django model class.
    id = models.AutoField(primary_key=True)
    # id: This is an AutoField, which automatically increments its value for each new record added to the database.
    # The primary_key=True parameter specifies that this field is the primary key for the table,
    # uniquely identifying each record.
    price = models.IntegerField()
    # price: This is an IntegerField, which represents the price at which the item was purchased.
    quantity = models.IntegerField()
    # quantity: This is an IntegerField, which represents the desired quantity of the item to purchase.
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # order: This is a foreign key relationship with the Order model,
    # which defines a foreign key relating each item to a specific order.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # movie: This is a foreign key relationship with the Movie model,
    # which defines a foreign key relating each item to a specific movie.
    def __str__(self):
        # __str__ is a method that returns a string representation of the item. In this case,
        # it returns a string composed of the item ID and the name of the associated movie.
        return str(self.id) + ' - ' + self.movie.name