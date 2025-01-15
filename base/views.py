from django.shortcuts import render
from typing import Any
from django.shortcuts import redirect
from django.views import View

class BaseUpdateView(View):
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)   
        return render(request,self.get_template_names(),context)
    
    def get_object(self):
        return self.model.get_from_db(id=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        self.instance = self.model.get_from_db(id=kwargs.get("pk"))
        context["form"] = self.form_class(initial=self.instance.__dict__) 
        return context
    
    def post(self,request,*args,**kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST)
        if form.is_valid():      
            instance.update(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})