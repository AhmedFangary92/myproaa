# from django.http import request
# from django.http.response import Http404, HttpResponse, HttpResponseBase, HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic.base import TemplateView
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
# from django.utils.translation import gettext as _


class home(ListView):
    model = List
    template_name = 'home.html'
    context_object_name = 'all_items'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ListForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, ('Item has been added to list.'))
                return redirect('home')
            else:
                messages.warning(request, ('Nothing has been added to list!'))
                return redirect('home')

class delete(DeleteView):
    def get(self, request, list_id):
        item = get_object_or_404(List, pk=list_id)
        item.delete()
        messages.success(request, ('Item has been deleted.'))
        return redirect('home')

class cross_off(UpdateView):
    def get(self, request, list_id):
        item = get_object_or_404(List, pk=list_id)
        item.completed = True
        item.save()
        messages.success(request, ('Item has been crossed off.'))
        return redirect('home')

class uncross(ListView):
    def get(self, request, list_id):
        item = get_object_or_404(List, pk=list_id)
        item.completed = False
        item.save()
        messages.success(request, ('Item has been uncrossed!'))
        return redirect('home')

class edit(ListView):
    model = List
    template_name = 'edit.html'
    context_object_name = 'item'

    def post(self, request, list_id):
        if request.method == 'POST':
            item = get_object_or_404(List, pk=list_id)
            form = ListForm(request.POST or None, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, ('Item has been edited.'))
                return redirect('home')
            messages.warning(request, ('Nothing has been edited.'))
            return redirect('home')
