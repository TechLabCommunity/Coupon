# Generated by Django 2.2.4 on 2019-08-03 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190803_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used_by_seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
