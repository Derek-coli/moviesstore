from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([ f'<div class="alert alert-danger" role="alert"> {e}</div>' for e in self]))
    # We import the ErrorList class, which is a default class used to store
    # and display validation error messages associated with form fields.
    # We import the mark_safe function, which is used to mark a string as safe for HTML rendering,
    # indicating that it doesn’t contain any harmful content and should be rendered as-is without escaping.
    # We define a new class named CustomErrorList, which extends Django’s ErrorList class.
    # This will be the class to define our custom error look and feel.
    # We override the __str__() method of the base ErrorList class.
    # If the error list is empty (i.e., there are no errors), it returns an empty string,
    # indicating that no HTML should be generated. Otherwise, it defines a custom HTML code that uses <div> elements
    # and Bootstrap CSS classes to improve the way the errors are displayed. It also uses the mark_safe function to render the code as-is.


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    # We import the UserCreationForm class from Django’s authentication forms.
    # We create a new class named CustomUserCreationForm, which inherits from UserCreationForm,
    # making it a subclass of Django’s built-in user creation form.
    # We define the class constructor (the __init__ method).
    # The constructor calls the constructor of the parent class (UserCreationForm) through the super method.
    # Then, we iterate through the fields provided by UserCreationForm.
    # These are 'username', 'password1', and 'password2'.
    # For each field specified in the loop, we set the help_text attribute to None,
    # which removes any help text associated with these fields.
    # Finally, for each field specified in the loop, we add the CSS form-control class to the field’s widget.
    # This is a Bootstrap class that improves the look and feel of the fields.