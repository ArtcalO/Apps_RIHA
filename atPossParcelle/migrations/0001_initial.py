# Generated by Django 3.0.7 on 2020-06-28 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('zone_price', models.IntegerField(default=0)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atposs_price_province', to='base.Zone')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('rejection_msg', models.TextField(blank=True, null=True)),
                ('secretary_validated', models.BooleanField(null=True)),
                ('ready', models.BooleanField(default=False)),
                ('first_witness', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='atposs_parc_witness1', to=settings.AUTH_USER_MODEL)),
                ('quarter_leader', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='atposs_parc_quater_leader', to=settings.AUTH_USER_MODEL)),
                ('residence_quarter', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atposs_parc_residence', to='base.Quarter')),
                ('second_witness', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='atposs_parc_witness2', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atposs_parc_user', to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(max_length=64, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atposs_parc_zone', to='base.Zone')),
                ('zone_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atposs_parc_province_payment', to='base.PaymentZone')),
            ],
        ),
    ]
