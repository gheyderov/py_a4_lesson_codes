from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
User = get_user_model()


class Command(BaseCommand):
    help = "Used to delete fake users"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args: Any, **options: Any):
        users = User.objects.filter(is_superuser = False)
        users.delete()