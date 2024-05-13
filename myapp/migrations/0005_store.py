# Generated by Django 4.2.4 on 2024-05-10 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_vendor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('softdel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myapp.softdel')),
                ('name', models.CharField(max_length=50)),
                ('vendors', models.ManyToManyField(to='myapp.vendor')),
            ],
            bases=('myapp.softdel',),
        ),
    ]
