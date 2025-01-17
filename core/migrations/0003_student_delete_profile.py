# Generated by Django 5.0.6 on 2024-05-12 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201129_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('parent_first_name', models.CharField(max_length=100)),
                ('parent_last_name', models.CharField(max_length=100)),
                ('parent_phone', models.CharField(max_length=20)),
                ('present', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
