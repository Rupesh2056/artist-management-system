from django.shortcuts import redirect,render

class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            return redirect("user_login")
        return super().dispatch(request,*args,**kwargs)
    

class HasPermissionMixin:
    authorized_goups = [] 
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user:
            if user.user_type in self.authorized_goups :
                return super().dispatch(request,*args,**kwargs)
            else:
                return  render(request, "permission_denied.html")
        return redirect("user_login")
        



