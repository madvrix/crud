# Generated by Django 2.2.17 on 2020-11-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orderan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemesan', models.CharField(max_length=225)),
                ('nama_pesanan', models.CharField(max_length=255)),
                ('jumlah_pesanan', models.IntegerField()),
                ('tgl_pesan', models.DateField(null=True)),
            ],
            options={
                'ordering': ['pemesan'],
            },
        ),
    ]