# Generated by Django 2.1.5 on 2019-03-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('members', models.TextField()),
                ('image', models.FileField(default='img/main_logo.jpg', upload_to='')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=150)),
                ('file_descriprion', models.TextField()),
                ('file_self', models.FileField(default='img/main_logo.jpg', upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(default='img/main_logo.jpg', upload_to=''),
        ),
    ]
