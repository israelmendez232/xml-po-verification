# Generated by Django 2.2.6 on 2019-10-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verificação',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml', models.FileField(blank=True, upload_to='XMLs', verbose_name='Insira aqui o XML:')),
                ('po', models.FileField(blank=True, upload_to='POs', verbose_name='Insira aqui a Ordem de COmpra:')),
            ],
        ),
    ]
