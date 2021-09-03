from django.urls import path, include

from .views import ApiTemplateCreateView, ApiTemplateUpdateView, ApiTemplateDestroyView, ApiTemplateRetrieveView, \
    ApiTemplateGetCompletedTemplate, ApiTemplateRetrieveListView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("template/create/", ApiTemplateCreateView.as_view()),
    path("template/update/<int:pk>", ApiTemplateUpdateView.as_view()),
    path("template/destroy/<int:pk>", ApiTemplateDestroyView.as_view()),
    path("template/retrieve/<int:pk>", ApiTemplateRetrieveView.as_view()),
    path("template/retrieve-list/", ApiTemplateRetrieveListView.as_view()),

    path("get-token/", obtain_auth_token, name="obtain"),

    path("template/get-completed/<int:pk>", ApiTemplateGetCompletedTemplate.as_view())
]
