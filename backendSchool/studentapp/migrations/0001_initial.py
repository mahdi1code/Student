# Generated by Django 5.1 on 2024-08-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=300)),
                ('Grade', models.CharField(max_length=500)),
            ],
        ),
    ]
