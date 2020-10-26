from django.db import models

class User(models.Model):
    FEMALE = 'female'
    MALE = 'male'

    GENDER_CHOICES = [
        (FEMALE, 'Женский'),
        (MALE, 'Мужской'),
    ]

    name = models.CharField(max_length = 128, verbose_name = 'инициалы')
    gender = models.CharField(max_length = 128, choices = GENDER_CHOICES, verbose_name = 'пол')
    age = models.IntegerField(verbose_name = 'Возраст (полных лет)')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'создан')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

class Question(models.Model):
    TEXT = 'text'
    OPTION = 'option'
    OPTIONS = 'options'

    QUESTION_TYPE_CHOICES = [
        (TEXT, 'Ответ текстом'),
        (OPTION, 'Ответ с выбором одного варианта'),
        (OPTIONS, 'Ответ с выбором нескольких вариантов'),
    ]

    name = models.CharField(max_length = 128, verbose_name = 'название вопроса') 
    text_question = models.TextField(max_length = 300, verbose_name = 'текст вопроса')
    type_answer = models.CharField(max_length = 128, choices = QUESTION_TYPE_CHOICES, verbose_name = 'тип вопроса')
    answer_s = models.ForeignKey('Answer', blank = True, null = True, on_delete = models.CASCADE, verbose_name = 'Выберите ответ')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'создан')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')       
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

class Questionnaire(models.Model):
    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STATUS_CHOICES = [
        (ACTIVE, 'Активный'),
        (INACTIVE, 'Неактивный'),
    ]

    name = models.CharField(max_length = 128, verbose_name = 'название опроса')
    status = models.CharField(max_length = 128, choices = STATUS_CHOICES, verbose_name = 'статус')
    users = models.ForeignKey('User', blank = True, null = True, on_delete = models.SET_NULL, verbose_name = 'назначенные пользователи')
    questions = models.ManyToManyField(Question, blank = True, verbose_name = 'назначенные вопросы')
    description = models.TextField(max_length = 300,blank = True, null = True, verbose_name = 'описание')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'создан')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')       
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "опросы"
        verbose_name_plural = "опросы"


class Answer(models.Model):
    name = models.ForeignKey('Question', blank = True, null = True, on_delete = models.SET_NULL, verbose_name = 'ответ для вопроса')
    users = models.ForeignKey('User', blank = True, null = True, on_delete = models.SET_NULL, verbose_name = 'пользователь')
    answer_s = models.CharField(max_length = 128, verbose_name = 'ответ')
    created_at = models.DateField(auto_now_add = True, verbose_name = 'создан')
    updated_at = models.DateField(auto_now = True, verbose_name = 'отредактирован')

    def __str__(self):
        return self.answer_s

    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"



