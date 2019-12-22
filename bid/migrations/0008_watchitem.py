# Generated by Django 3.0 on 2019-12-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191222_1447'),
        ('bid', '0007_biddeduser_selliteminstantincrement'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bid.SellItem')),
                ('watching_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
        ),
    ]
