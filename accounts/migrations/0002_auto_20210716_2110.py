# Generated by Django 3.2.5 on 2021-07-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'カスタムユーザー', 'verbose_name_plural': 'カスタムユーザー'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='プロフィール画像'),
        ),
    ]