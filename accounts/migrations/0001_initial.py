# Generated by Django 3.0.8 on 2020-08-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accpython',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('opt1', models.CharField(max_length=20)),
                ('opt2', models.CharField(max_length=20)),
                ('opt3', models.CharField(max_length=20)),
                ('opt4', models.CharField(max_length=20)),
                ('corr', models.CharField(max_length=20)),
            ],
        ),
    ]
