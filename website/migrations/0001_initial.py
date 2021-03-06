# Generated by Django 2.2.8 on 2020-09-12 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20, verbose_name='Gender')),
                ('name', models.CharField(max_length=256, verbose_name='Country Name')),
                ('email', models.EmailField(blank=True, error_messages={'unique': 'This email id is already registered.'}, max_length=254, null=True, unique=True, verbose_name='Email Address')),
                ('mobile', models.CharField(blank=True, error_messages={'unique': 'This mobile no is already registered.'}, max_length=15, null=True, unique=True, verbose_name='Mobile Number')),
            ],
        ),
    ]
