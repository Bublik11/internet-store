from authapp.forms import ShopUserEditForm, ShopUserLoginForm, ShopUserRegisterForm
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


def login(request):
    title = "Вход в систему"

    if request.method == "POST":
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main"))
    else:
        login_form = ShopUserLoginForm()

    content = {"title": title, "login_form": login_form}
    return render(request, "authapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {"title": title, "edit_form": edit_form}

    return render(request, "authapp/edit.html", content)


def register(request):
    title = "регистрация"

    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = ShopUserRegisterForm()

    content = {"title": title, "register_form": register_form}

    return render(request, "authapp/register.html", content)
