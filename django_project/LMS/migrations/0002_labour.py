# Generated by Django 5.0.2 on 2024-03-04 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Labour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='django_project\\LMS\\static\\LMS\\profile_pics')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LMS.manager')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]