from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'

class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('message_list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    template_name = 'message_form.html'
    fields = ['title', 'body']

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message_list')