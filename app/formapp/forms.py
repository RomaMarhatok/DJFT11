from django import forms

class DynamicForm(forms.Form):
    text = forms.CharField()
    def __init__(self,*args,**kwargs) -> None:
        extra_fields:dict = kwargs.get("extra_fields")
        if extra_fields is not None:
            kwargs.pop("extra_fields")
        super(DynamicForm,self).__init__(*args,**kwargs)
        if extra_fields is not None:
            for key in extra_fields.keys():
                self.fields[key] = forms.CharField()