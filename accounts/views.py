from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomErrorList

from django.shortcuts import redirect
# We import the redirect function, which is used to redirect the user to a different URL within the application.
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
# We import login and authenticate.
#  These are used for user authentication.
# We import login with an alias (auth_login) to avoid confusion with the login function name.

from django.contrib.auth.decorators import login_required
# We import the logout function as auth_logout. This is used to log a user out.
from django.contrib.auth.models import User
# We import the User model from Django’s authentication system.


def signup(request):
    # template_data = {}
    # template_data['title'] = 'Sign Up'
    template_data = {'title': 'Sign Up'}
    if request.method == 'GET':
        # template_data['form'] = UserCreationForm()
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'template_data': template_data})
    elif request.method == 'POST':
        #  This section checks whether the HTTP request method is POST, indicating that the form has been submitted
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        #  we create an instance of the UserCreationForm class,
        # passing the data from the request’s POST parameters (request.POST) to populate the form fields.
        # We imported our CustomErrorList class, and we passed this class as an argument to CustomUserCreationForm. 
        # This time, if an error is found when we submit the signup form,
        # the form will use our CustomErrorList class and display the errors with our custom HTML and CSS code.
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
            # return redirect('home.index')


        # The if form.is_valid() checks whether the submitted form data is valid,
        # according to the validation rules defined in the UserCreationForm class.
        # These validations include that the two password fields match, the password is not common,
        # and the username is unique, among others.
        # If the form data is valid, form.save() saves the user data to the database.
        # This means creating a new user account with the provided username and password.
        # Also, we redirect the user to the home page based on the URL pattern name.
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})
        # If the form data is not valid, the else section is executed,
        # and we pass the form (including the errors) to the template and render the accounts/signup.html template again



def login(request):
    # We create the login function. This function defines template_data and checks request.method.
    # template_data = {}
    # template_data['title'] = 'Login'
    template_data = {'title': 'Login'}
    if request.method == 'GET':
        # For GET requests, the function renders the accounts/login.html template.
        return render(request, 'accounts/login.html',{'template_data': template_data})
    elif request.method == 'POST':
        # For POST requests, the function attempts to authenticate the user using the provided username and password.
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            #  If authentication fails, it renders the login template again with an error message.
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',{'template_data': template_data})
        else:
            auth_login(request, user)
            # If authentication succeeds, it logs the user in and redirects them to the home page.
            return redirect('home.index')

# def login(request):
#     template_data = {'title': 'Login'}
#     if request.method == 'GET':
#         return render(request, 'accounts/login.html', {'template_data': template_data})
#     elif request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             return redirect('home.index')
#         else:
#             template_data['error'] = 'Invalid username or password'
#             return render(request, 'accounts/login.html', {'template_data': template_data})

@login_required
def logout(request):# We create the logout function, which uses the login_required decorator.
    # This means that only authenticated users can access this function.
    # The logout function calls auth_logout, which is used to log out the current user.
    auth_logout(request)
    return redirect('home.index') # Then, the function redirects the user to the home page.
# We import login_required, which is a decorator to ensure that only authenticated users can access specific view functions.
# A Django decorator is a function that wraps another function or method to modify its behavior.
# Decorators are commonly used for things such as authentication, permissions, and logging.

@login_required
def orders(request):
    # We use the login_required decorator to ensure that the user must be logged in to access the orders function.
    # We define the orders function, which takes a request object as a parameter.
    # template_data = {}
    # template_data['title'] = 'Orders'
    # template_data['orders'] = request.user.order_set.all()
    template_data = {'title': 'Orders', 'orders': request.user.order_set.all()}
    # We define the template_data variable and assign it a title.
    # We retrieve all orders belonging to the currently logged-in user (request.user).
    # The order_set attribute is used to access the related orders associated with the user through their relationship
    # Remember that there is a ForeignKey relationship between the User model and the Order model.
    return render(request, 'accounts/orders.html', {'template_data': template_data})
    # Finally, we pass the orders to the template and render it.