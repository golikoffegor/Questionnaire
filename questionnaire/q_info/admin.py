from django.contrib import admin
from .models import User, Question, Questionnaire, Answer

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'age', 'created_at', 'updated_at']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_answer', 'created_at', 'updated_at']

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'users','created_at', 'updated_at']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name', 'users', 'answer_s','created_at', 'updated_at']

admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Answer, AnswerAdmin)