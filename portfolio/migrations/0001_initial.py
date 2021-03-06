# Generated by Django 2.0.6 on 2018-11-22 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField(max_length=30)),
                ('Category_details', models.TextField(max_length=2000)),
                ('category_image', models.FileField(upload_to='')),
                ('number_of_orders', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.TextField(max_length=200)),
                ('order_abstract', models.TextField(max_length=2000)),
                ('order_details', models.TextField(max_length=5000)),
                ('order_date', models.DateField(null=True)),
                ('order_image', models.FileField(default='', upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Category')),
            ],
        ),
    ]
