# Generated by Django 5.0.2 on 2024-03-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0002_labour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labour',
            name='image',
            field=models.ImageField(default='django_project\\LMS\\static\\LMS\\profile_pics\\default.jpg', upload_to='django_project\\LMS\\static\\LMS\\profile_pics'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='image',
            field=models.ImageField(default='django_project\\LMS\\static\\LMS\\profile_pics\\default.jpg', upload_to='django_project\\LMS\\static\\LMS\\profile_pics'),
        ),
    ]