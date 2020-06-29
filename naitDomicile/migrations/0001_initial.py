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
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_price_province', to='base.Zone')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('child_name', models.CharField(max_length=50)),
                ('child_birth', models.DateField()),
                ('payment_method', models.CharField(max_length=64)),
                ('payment_serial', models.CharField(max_length=64)),
                ('rejection_msg', models.TextField(blank=True, null=True)),
                ('secretary_validated', models.BooleanField(default=False)),
                ('ready', models.BooleanField(default=False)),
                ('child_birth_quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_ChildBirthQuarterNaD', to='base.Quarter')),
                ('child_birth_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_ChildBirthZoneNaD', to='base.Zone')),
                ('child_mother', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_ChildMotherNaD', to='base.Profile')),
                ('first_witness', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_WitnessNaDO', to='base.Profile')),
                ('residence_quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_QuartierNaD', to='base.Quarter')),
                ('second_witness', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_WitnessNaDT', to='base.Profile')),
                ('supervisor', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_SupervisorNaD', to='base.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_BeneficiareNaD', to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, related_name='naitdom_ZoneNaD', to='base.Zone')),
            ],
        ),
    ]