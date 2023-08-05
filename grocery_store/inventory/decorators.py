from django.contrib.auth.decorators import user_passes_test


def group_required(staff):
    def check_group(user):
        return user.groups.filter(name=staff).exists()

    return user_passes_test(check_group)
