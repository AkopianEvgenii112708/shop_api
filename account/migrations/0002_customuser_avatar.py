# Generated by Django 4.1.5 on 2023-01-17 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_avatar.jpg', upload_to='avatars/'),
        ),
    ]