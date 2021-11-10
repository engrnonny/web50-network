# Generated by Django 3.1.3 on 2021-11-09 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
