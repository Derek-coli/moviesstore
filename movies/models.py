from django.db import models
from django.contrib.auth.models import User
# We import the User model from Django’s django.contrib.auth.models module.

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Review(models.Model):
    # We define a Python class named Review,
    # which inherits from models.Model. This means that Review is a Django model class.
    id = models.AutoField(primary_key=True)
    # id is an AutoField, which automatically increments its value for each new record added to the database
    # The primary_key=True parameter specifies that this field is the primary key for the table,
    # uniquely identifying each record.
    comment = models.CharField(max_length=255)
    # comment is a CharField, which represents a string field with a maximum length of 255 characters.
    # It stores the movie review text.
    date = models.DateTimeField(auto_now_add=True)
    # date is a DateTimeField, which stores the date and time when the review was created.
    # The auto_now_add=True parameter sets the date to the current date and time when a new record is created.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user is a ForeignKey field, which establishes a relationship between the Review and User models.
    # It represents the user who wrote the review.
    # The on_delete=models.CASCADE parameter specifies that if the associated User record is deleted,
    # the Review record will also be deleted (cascade deletion).
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # movie is a foreign key relationship to the Movie model.
    # A review is associated with a movie.
    # The on_delete parameter specifies how to handle the deletion of a movie that a review is associated with.
    # In this case, on_delete=models.CASCADE means that if the related movie is deleted,
    # the associated review will also be deleted.

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user is another foreign key relationship but to the User model.
    # A review is associated with a user (the person who wrote the review).
    # Similar to the movie attribute, on_delete=models.CASCADE specifies that if the related user is deleted,
    # the associated review will also be deleted.

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
    # __str__ is a method that returns a string representation of the review.
    # In this case, it returns a string that is composed of the review ID and
    # the name of the movie associated with the review.