from django.shortcuts import redirect

class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            return redirect("user_login")
        return super().dispatch(request,*args,**kwargs)

