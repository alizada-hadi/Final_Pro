from django.contrib.auth.decorators import user_passes_test


def group_required(*group_name):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_name)) or user.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url="403")
