
from django.core.exceptions import PermissionDenied


def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:

                raise PermissionDenied

        return wrapper

    return decorator