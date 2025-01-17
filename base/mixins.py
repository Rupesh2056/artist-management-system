from django.shortcuts import redirect,render


def get_redirected(user):
    if user.user_type == "admin":
        return redirect("index")
    elif user.user_type == "artist_manager":
        return redirect("artist_list")
    else:
        return redirect("album_list")
class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            return redirect("user_login")
        return super().dispatch(request,*args,**kwargs)
    

class HasPermissionMixin:
    authorized_groups = [] 
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user:
            if "all" in self.authorized_groups or user.user_type in self.authorized_groups :
                return super().dispatch(request,*args,**kwargs)
            else:
                return  render(request, "permission_denied.html")
        return redirect("user_login")  
