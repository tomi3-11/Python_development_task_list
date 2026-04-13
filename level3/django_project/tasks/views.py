from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
	if request.user.is_staff:
		tasks = Task.objects.all()
	else:
		tasks = Task.objects.filter(owner=request.user)

	return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required
def task_create(request):
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit=False)
			task.owner = request.user
			task.save()
			messages.success(request, "Task created successfully.")
			return redirect("task_list")
	else:
		form = TaskForm()

	return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_toggle(request, task_id):
	task = get_object_or_404(Task, id=task_id)

	if request.user == task.owner or request.user.is_staff:
		task.completed = not task.completed
		task.save(update_fields=["completed"])
	else:
		messages.error(request, "You do not have permission to modify this task.")

	return redirect("task_list")


@user_passes_test(lambda user: user.is_staff)
def admin_dashboard(request):
	users_count = Task.objects.values("owner").distinct().count()
	total_tasks = Task.objects.count()
	completed_tasks = Task.objects.filter(completed=True).count()

	return render(
		request,
		"tasks/admin_dashboard.html",
		{
			"users_count": users_count,
			"total_tasks": total_tasks,
			"completed_tasks": completed_tasks,
		},
	)
