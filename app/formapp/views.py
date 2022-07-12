from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.db.models.query import QuerySet
from .models import FieldsModel
from django.core import serializers
from .forms import DynamicForm
# Create your views here.

def index(request:HttpRequest):
    if request.method == "GET":
        return render(request,"formapp/index.html",context={"form":DynamicForm()})
    if request.method == "POST":
        extra_fields:dict = {key:value for key,value in request.POST.items() if "text" in key}
        form = DynamicForm(request.POST,extra_fields=extra_fields)
        if form.is_valid():
            FieldsModel.objects.create(inputs=form.cleaned_data)
        return redirect("all")

def models_list(request:HttpRequest):
    if request.method == "GET":
        filed_models:QuerySet = FieldsModel.objects.all()
        json_data = serializers.serialize("json",queryset=filed_models)
        return HttpResponse(content=json_data,content_type='application/json')