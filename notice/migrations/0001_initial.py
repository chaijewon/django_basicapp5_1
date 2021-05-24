# Generated by Django 3.2.3 on 2021-05-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=34)),
                ('subject', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField()),
            ],
        ),
    ]
