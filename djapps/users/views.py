from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login


@login_required
def home(request):
    """
    Home view that renders the home page.
    """
    template_name = 'users/home.html'
    context = {} # You can add context data here if needed   
    
    return render(request, template_name=template_name, context=context)

def custom_login(request):
    """
    Custom login view that renders the login page.
    """
    template_name = 'users/login.html'
    if request.method == 'POST':
        user_input = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=user_input, password=password)
        if user is not None:
            login(request, user)
            # User is authenticated, redirect to a success page
            return redirect('home')
        else:
            # Invalid credentials, render the login page with an error message
            return render(request, template_name, {'error': 'Invalid username or password'})
        
    else:
        # GET request, render the login page
        return render(request, template_name)

def custom_logout(request):
    """
    Custom logout view that logs out the user and redirects to the home page.
    """
    logout(request)
    return redirect('home')
    
    
