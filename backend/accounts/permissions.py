from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name__in=group_names).exists() or user.is_superuser:
                return True
            raise PermissionDenied
        return False
    return user_passes_test(in_groups)
