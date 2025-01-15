
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


class PartialTemplateMixin:
    '''
    created seperate mixing to be implemented on table list.

    '''
    def get_partial_template(self):
        partial_template_name =  "htmx_partial/" + self.template_name
        return partial_template_name
    
    def get_partial_list_template(self):
        partial_list_template = "htmx_partial/" + self.template_dir + "table_content.html"
        return partial_list_template

    
    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            if (self.request.GET.get("search") or self.request.GET.get("q")):
                return [self.get_partial_list_template()]
            return [self.get_partial_template()]
        return super().get_template_names()