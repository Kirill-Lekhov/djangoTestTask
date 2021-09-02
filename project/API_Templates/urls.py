from django.urls import path, include

from .views import ApiTemplateCreateView, ApiTemplateUpdateView, ApiTemplateDestroyView, ApiTemplateRetrieveView


urlpatterns = [
    path("template/create/", ApiTemplateCreateView.as_view()),
    path("template/update/<int:pk>", ApiTemplateUpdateView.as_view()),
    path("template/destroy/<int:pk>", ApiTemplateDestroyView.as_view()),
    path("template/retrieve/<int:pk>", ApiTemplateRetrieveView.as_view()),
]
