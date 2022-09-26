from operator import imod

from django.urls import path

from . import views

app_name = "contracts"


urlpatterns = [
    path("", views.ContractListView.as_view(), name="contract-list"),
    path(
        "detail/<int:pk>/", views.ContractDetailView.as_view(), name="contract-detail"
    ),
    path("create/", views.ContractCreateView.as_view(), name="contract-create"),
    path(
        "update/<int:pk>/", views.ContractUpdateView.as_view(), name="contract-update"
    ),
]
