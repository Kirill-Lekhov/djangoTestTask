from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ApiTemplateCreateSerializer, ApiTemplateUpdateSerializer
from .permissions import IsOwnerOrReadOnly
from .models import ApiTemplate


from .REST_API_Templates.functions import put_variables_to_template, template_variables_number


class ApiTemplateCreateView(generics.CreateAPIView):
    serializer_class = ApiTemplateCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        return self.create(request, *args, **kwargs)


class ApiTemplateUpdateView(generics.UpdateAPIView):
    serializer_class = ApiTemplateUpdateSerializer
    queryset = ApiTemplate.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ApiTemplateDestroyView(generics.DestroyAPIView):
    queryset = ApiTemplate.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class ApiTemplateRetrieveView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        response = {}

        try:
            template = ApiTemplate.objects.get(id=kwargs["pk"])

            response['id'] = template.id
            response['user'] = template.user.username
            response['body'] = template.body
            response['number_of_variables'] = template_variables_number(template.body)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(response, status=status.HTTP_200_OK)


class ApiTemplateRetrieveListView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        response = {}

        try:
            templates = ApiTemplate.objects.all()
            response["templates"] = []

            for template in templates:
                template_form = dict()

                template_form['id'] = template.id
                template_form['user'] = template.user.username
                template_form['body'] = template.body
                template_form['number_of_variables'] = template_variables_number(template.body)

                response["templates"].append(template_form.copy())

            response["templates"] = sorted(response["templates"], key=lambda x: x["number_of_variables"])

        except Exception as err:
            return Response({"error_message": err}, status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response, status=status.HTTP_200_OK)


class ApiTemplateGetCompletedTemplate(APIView):
    def get(self, request, *args, **kwargs):
        response = {}

        try:
            template = ApiTemplate.objects.get(id=kwargs["pk"])
            answer = put_variables_to_template(template.body, request.data)
            response["answer"] = answer

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except IndexError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)
