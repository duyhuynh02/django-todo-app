from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post 


class HomePageView(ListView):
	model = Post 
	template_name = 'home.html'


class WorkDetailView(DetailView):
	model = Post 
	template_name = 'work_detail.html'


class WorkCreateView(CreateView):
	model = Post 
	template_name = 'work_new.html'
	fields = ['title', 'memo', 'author', 'completed']


class WorkUpdateView(UpdateView):
	model = Post 
	template_name = 'work_update.html'
	fields = ['title', 'memo', 'completed']


class WorkDeleteView(DeleteView):
	model = Post 
	template_name = 'work_delete.html'
	success_url = reverse_lazy('home')