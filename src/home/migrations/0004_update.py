# Generated by Django 2.2.13 on 2020-07-21 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('update', models.CharField(max_length=50000)),
            ],
            options={
                'db_table': 'Update',
            },
        ),
    ]
