# Generated by Django 3.1.1 on 2020-09-25 03:18

import django.db.models.deletion
import swapper
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sample_ipam', '0002_remove_ipaddress_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subnet',
            name='organization',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=swapper.get_model_name('openwisp_users', 'Organization'),
                verbose_name='organization',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='subnet',
            unique_together={('subnet', 'organization')},
        ),
    ]
