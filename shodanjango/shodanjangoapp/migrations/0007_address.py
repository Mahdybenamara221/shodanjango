# Generated by Django 4.1.5 on 2023-02-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shodanjangoapp', '0006_delete_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Address',
            },
        ),
    ]
