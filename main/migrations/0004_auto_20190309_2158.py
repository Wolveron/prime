# Generated by Django 2.1.5 on 2019-03-09 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190309_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mails',
            new_name='mail',
        ),
        migrations.RenameModel(
            old_name='news',
            new_name='new',
        ),
        migrations.RenameModel(
            old_name='products',
            new_name='product',
        ),
        migrations.DeleteModel(
            name='UploadTest',
        ),
    ]