# Generated by Django 3.1.2 on 2020-10-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название вопроса')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название вопроса')),
                ('t_question', models.TextField(max_length=300, verbose_name='текст вопроса')),
                ('temper', models.CharField(choices=[('text', 'Ответ текстом'), ('option', 'Ответ с выбором одного варианта'), ('options', 'Ответ с выбором нескольких вариантов')], max_length=128, verbose_name='тип вопроса')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='зарегестрирован')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='отредактирован')),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='q_info.answer', verbose_name='Выберите ответ')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='инициалы')),
                ('gender', models.CharField(choices=[('female', 'Женский'), ('male', 'Мужской')], max_length=128, verbose_name='пол')),
                ('age', models.IntegerField(verbose_name='Возраст (полных лет)')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='зарегестрирован')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='отредактирован')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название опроса')),
                ('status', models.CharField(choices=[('active', 'Активный'), ('inactive', 'Неактивный')], max_length=128, verbose_name='пол')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='описание')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='зарегестрирован')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='отредактирован')),
                ('users', models.ManyToManyField(to='q_info.Question')),
            ],
            options={
                'verbose_name': 'опросы',
                'verbose_name_plural': 'опросы',
            },
        ),
    ]
