from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()

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
    


def register(request):
    template_name = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']

            if password != password2:
                form.add_error('password2', 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})