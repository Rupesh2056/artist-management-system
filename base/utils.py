
from user.db_utils import get_user


class BaseForm:
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs[
                    "class"
                ] = "form-control form-control-solid"
            

def get_request_user(request):
    email = request.session.get("user_email")
    if email:
        return get_user(email)
    return None