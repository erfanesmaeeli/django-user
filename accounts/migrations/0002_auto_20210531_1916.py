# Generated by Django 3.2.3 on 2021-05-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ عباس2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ عباس'),
        ),
    ]