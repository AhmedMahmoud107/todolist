# from todolist.models import TodoListt

# class UserQuerysetMixin():

#     def get_queryset(self, *args, **kwargs):
#         qs = super().get_queryset(*args, **kwargs)
#         request = self.request
#         user = request.user
#         if not user.is_authenticated:
#             return TodoListt.objects.none()
#         return qs.filter(user=request.user)
        