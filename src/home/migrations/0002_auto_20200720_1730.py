# Generated by Django 2.2.13 on 2020-07-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='CurrentCourses',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='students',
            name='PassedCourses',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='students',
            name='UndergraduateCourses',
            field=models.CharField(max_length=20000),
        ),
    ]