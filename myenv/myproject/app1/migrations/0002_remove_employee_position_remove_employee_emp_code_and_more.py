# Generated by Django 4.2.4 on 2023-08-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Position',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='emp_code',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile',
        ),
        migrations.AddField(
            model_name='employee',
            name='e_mail',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
