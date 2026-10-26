from functools import wraps
from django.http import Http404
from .models import Profile_Instance

def teacher_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        teacher_id = request.session.get("teacher_id")

        if not teacher_id:
            raise Http404("Page not found")

        if not Profile_Instance.objects.filter(
            pk=teacher_id,
            is_shop_instructor=True
        ).exists():
            raise Http404("Page not found")

        return view_func(request, *args, **kwargs)

    return wrapper