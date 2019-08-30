from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from .models import Expenses

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AddExpenseView(ListView,LoginRequiredMixin):
    model = Expenses
    login_url = '/login/'
    template_name = 'expense_list.html'
