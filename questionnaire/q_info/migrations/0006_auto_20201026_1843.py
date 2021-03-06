# Generated by Django 3.1.2 on 2020-10-26 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('q_info', '0005_auto_20201026_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='q_info.user', verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='создан'),
        ),
    ]
