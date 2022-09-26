from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Contract


class ContractListView(ListView):
    model = Contract


class ContractDetailView(DetailView):
    model = Contract


class ContractCreateView(CreateView):
    model = Contract
    fields = '__all__'


class ContractUpdateView(UpdateView):
    model = Contract
    fields = '__all__'
