# Generated by Django 3.2.9 on 2021-11-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='')),
                ('Body', models.TextField()),
                ('Description', models.CharField(max_length=100)),
            ],
        ),
    ]