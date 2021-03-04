from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
            return HttpResponseRedirect(reverse('accounts:user_login'))

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'accounts/signup.html',
                                        {'user_form':user_form,
                                        'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            messages.warning(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')
            print("Someone tried to login and failed!")
            print("Username: {} and Password {}".format(username, password))
    else:
        return render(request, 'accounts/login.html', {})

@login_required(login_url='/accounts/user_login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:user_login'))

# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'
