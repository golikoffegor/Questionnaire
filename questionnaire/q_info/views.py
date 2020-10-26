from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import *

def set_query_params(request):
    q_fields = list(request.GET)
    q_params = dict()
    for key in q_fields:
        value = request.GET.get(key, None)
        if value:
            q_params[key] = value
    return q_params

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        filtered_query_set = self.queryset
        params = set_query_params(self.request)

        if "upper" in params:
            filtered_query_set = filtered_query_set.filter(age__gte = params["upper"])
        if "lower" in params:
            filtered_query_set = filtered_query_set.filter(age__lte = params["lower"])

        return filtered_query_set

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class QuestionnaireViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()

    def get_queryset(self):
        filtered_query_set = self.queryset
        params = set_query_params(self.request)

        if "status" in params:
            filtered_query_set = filtered_query_set.filter(status = params["status"])

        return filtered_query_set

class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

