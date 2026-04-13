from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_user_roles(sender, **kwargs):
    regular_group, _ = Group.objects.get_or_create(name="Regular User")
    admin_group, _ = Group.objects.get_or_create(name="Admin User")

    regular_permissions = Permission.objects.filter(codename__in=["view_task", "add_task", "change_task"])
    admin_permissions = Permission.objects.filter(codename__in=["view_task", "add_task", "change_task", "delete_task"])

    regular_group.permissions.set(regular_permissions)
    admin_group.permissions.set(admin_permissions)
