# Generated by Django 2.1.7 on 2019-03-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chaiwalaapp', '0004_auto_20190318_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chai_Order_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chaiwala', models.CharField(max_length=100)),
                ('Quantity', models.CharField(max_length=255)),
            ],
        ),
    ]
