from .models import userpost
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import signupForm, signinForm, postForm, updateUserForm, updatePasswordForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request, nav=False):
    posts = userpost.objects.all()
    if request.user.is_authenticated:
        nav = True
    return render(request, 'main/home.html', {'posts': posts, 'nav': nav})


def about(request, nav=False):
    if request.user.is_authenticated:
        nav = True
    return render(request, 'main/about.html', {'nav': nav})


@login_required
def profile_page(request):
    user_instance = User.objects.get(username=request.user.username)

    if request.method == "POST":
        form = updateUserForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!!")
    else:
        form = updateUserForm(instance=user_instance)
    return render(request, 'main/profile.html', {'nav': True, 'form': form, "username": request.user.username})


@login_required
def dashboard(request):
    uname = request.user.username
    posts = userpost.objects.filter(username=uname)
    nav = {
        '1': 'Dashboard',
        '2': 'Logout'
    }
    return render(request, 'main/dashboard.html', {'username': uname, 'posts': posts, 'nav': True})


@login_required
def add_post(request, username):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            ttle = form.cleaned_data['title']
            desc = form.cleaned_data['description']
            addpost = userpost.objects.create(
                username=username, title=ttle, description=desc)
            addpost.save()
            messages.success(request, "Blog added successfully!!")
            return HttpResponseRedirect('/dashboard/')
    else:
        form = postForm()
    return render(request, 'main/post.html', {'username': username, 'form': form, 'nav': True})


@login_required
def edit_post(request, id):
    post = userpost.objects.get(pk=id)

    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            ttle = form.cleaned_data['title']
            desc = form.cleaned_data['description']

            post.title = ttle
            post.description = desc
            post.save()

            messages.success(request, "Blog Updated successfully!!")
            return HttpResponseRedirect('/dashboard/')
    else:
        form = postForm(instance=post)
    return render(request, 'main/editpost.html', {'form': form, 'id': id, 'nav': True})


@login_required
def full_post(request, id):
    # this function is for users to read their own blogs
    fullpost = userpost.objects.get(pk=id)
    return render(request, 'main/fullpost.html', {'userpost': fullpost, 'nav': True})


def read_full_post(request, id, back, nav=False):
    # this function is for users to read blogs from other users
    fullpost = userpost.objects.get(pk=id)
    if request.user.is_authenticated:
        nav = True
    return render(request, 'main/readfullpost.html', {'nav': nav, 'post': fullpost, 'back': back})


@login_required
def delete_post(request, id):
    post_to_delete = userpost.objects.get(pk=id)
    post_to_delete.delete()
    messages.success(request, "Blog deleted!!")
    return HttpResponseRedirect('/dashboard/')


@login_required
def show_user(request, username):
    all_posts = userpost.objects.filter(username=username)
    return render(request, 'main/user.html', {'posts': all_posts, 'username': username, 'nav': True})


def change_password(request):
    if request.method == "POST":
        frm = updatePasswordForm(user=request.user, data=request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, 'Password changed!!')
            return HttpResponseRedirect('/profile/')
    else:
        frm = updatePasswordForm(user=request.user)
    return render(request, 'main/change_password.html', {'form': frm, 'nav': True})


def login_user(request):

    if request.method == "POST":
        frm = signinForm(request=request, data=request.POST)
        if frm.is_valid():
            name = frm.cleaned_data['username']
            upassword = frm.cleaned_data['password']
            user = authenticate(username=name, password=upassword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')
    else:
        frm = signinForm()
    return render(request, 'main/signin.html', {'form': frm, 'nav': False})


def signup(request):

    if request.method == "POST":
        frm = signupForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, "Account Created Successfully")
            return HttpResponseRedirect('/dashboard/')

    else:
        frm = signupForm()
    return render(request, 'main/signup.html', {'form': frm, 'nav': False})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login_user/')
