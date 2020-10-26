from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('id','name','gender','age','created_at','updated_at')

class QuestionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Question
        fields = ('id','name','text_question','type_answer','answer_s_id','created_at','updated_at')

class QuestionnaireSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Questionnaire
        fields = ('id','name','status','users','questions','description','created_at','updated_at')

class AnswerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Answer
        fields = ('id','name','answer_s','created_at','updated_at')
