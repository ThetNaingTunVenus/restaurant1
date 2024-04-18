import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum,Count,F
from django.http import HttpResponse
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView,ListView
# import generic UpdateView
from django.views.generic.edit import DeleteView

from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.paginator import Paginator

from .forms import *
from .models import *
# Create your views here.
def test(request):
    return render(request, 'item_list.html')

class itemlist(View):
    def get(self, request):
        items = item.objects.all()
        form = itemcreateform()
        context = {'items':items, 'form':form}
        return render(request, 'item_list.html', context)
