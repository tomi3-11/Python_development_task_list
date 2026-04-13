from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			group, _ = Group.objects.get_or_create(name="Regular User")
			user.groups.add(group)
			messages.success(request, "Registration successful. Please login.")
			return redirect("login")
	else:
		form = RegisterForm()

	return render(request, "registration/register.html", {"form": form})
