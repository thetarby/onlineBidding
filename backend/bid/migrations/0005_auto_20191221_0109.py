# Generated by Django 3.0 on 2019-12-20 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0004_auto_20191221_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellitem',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bid.Item'),
        ),
    ]
