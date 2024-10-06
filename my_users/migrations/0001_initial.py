# Generated by Django 5.1 on 2024-10-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='male', max_length=6)),
                ('phone', models.CharField(error_messages={'unique': 'The phone number is already in use.'}, help_text='09xx xxx xxxx', max_length=10, unique=True)),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether this lawyer has verified phone')),
                ('license_number', models.CharField(max_length=5)),
                ('history_of_legal_license', models.CharField(max_length=50)),
                ('about_me', models.TextField(blank=True, max_length=1000)),
                ('img', models.ImageField(blank=True, help_text='Set profile picture', upload_to='', verbose_name='Profile Picture')),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(error_messages={'unique': 'The phone number is already in use.'}, help_text='09xx xxx xxxx', max_length=10, unique=True)),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether this user has verified phone')),
            ],
        ),
    ]
