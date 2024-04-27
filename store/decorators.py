from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

from store.models import Item


def login_required(login_url='/'):

    def inner_func_as_args(func):

        def inner_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.warning(request, 'You should be authenticated!')
                return redirect(login_url)
            return func(request, *args, **kwargs)

        return inner_func

    return inner_func_as_args


# def my_news(func):

#     def inner_func(request, id, *args, **kwargs):
#         user = request.user
#         item = get_object_or_404(Item, id=id)
#         if user != item.author:
#             messages.warning(request, 'You cannot make any actions, it\'s not your news.')
#             return redirect('/workspace/')

#         return func(request, id, *args, **kwargs)

#     return inner_func