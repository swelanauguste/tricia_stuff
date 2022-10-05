from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ContractCreateForm
from .models import Contract


class ContractListView(LoginRequiredMixin, ListView):
    model = Contract


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractCreateForm


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    fields = "__all__"
