# Generated by Django 3.1.3 on 2020-12-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='', max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
