# Generated by Django 4.0.3 on 2022-12-07 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('reason', models.CharField(max_length=500)),
                ('complete', models.BooleanField(default=False)),
                ('vin', models.CharField(max_length=17, unique=True)),
                ('vip', models.BooleanField(default=False)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='service_rest.technician')),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]