from user.db_utils import get_user
from django.http import JsonResponse
from django.http import HttpResponse
import csv
from datetime import datetime

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
        return self.template_name
    

class DeleteMixin:
    def remove_from_DB(self, request):
        try:
            object_id = request.GET.get("pk", None)
            print("object_id")
            print(object_id)
            object = self.model.get_from_db(id=object_id)
            if object:
                print(object)
                self.model.delete(id=object_id)
                return True
        except Exception as e:
            return str(e)

    def get(self, request):
        status = self.remove_from_DB(request)
        return JsonResponse({"deleted": status})
    

class ExportMixin:
    fields = []
    name = ""
    queryset = None
    obj_list = []

    def get(self, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        date = datetime.now().strftime("%Y-%m-%d")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(
            f"{self.name}-{date}"
        )
        writer = csv.writer(response)
        writer.writerow(self.fields)
        self.write_rows(writer, self.get_queryset())
        return response

    def write_rows(self, writer, queryset):
        pass

    def get_queryset(self, *args, **kwargs):
        return self.queryset
