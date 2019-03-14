# Generated by Django 2.1.5 on 2019-03-14 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_popularity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=150)),
                ('count', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('product_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
        ),
    ]
