from django_ratelimit.decorators import ratelimit
from django.http import JsonResponse


def new_rates(non_registered_rate, registered_rate):
    def rate_limit_wrapper(view_func):
        non_registered_decorator = ratelimit(
            key="ip", rate=non_registered_rate, method="ALL", block=True
        )
        registered_decorator = ratelimit(
            key="user", rate=registered_rate, method="ALL", block=True
        )

        def wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                return registered_decorator(view_func)(request, *args, **kwargs)
            else:
                return non_registered_decorator(view_func)(request, *args, **kwargs)

        return wrapped_view

    return rate_limit_wrapper
