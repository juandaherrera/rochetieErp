# Generated by Django 3.2.4 on 2021-06-24 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_auto_20210622_1751'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('nit', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='NIT')),
                ('address', models.CharField(blank=True, max_length=120, null=True, verbose_name='Dirección')),
                ('address_2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Datos adicionales')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Número telefónico')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city', verbose_name='Ciudad')),
                ('creator_user', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario creador')),
                ('modifier_user', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Último usuario que modificó')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['name'],
            },
        ),
    ]
