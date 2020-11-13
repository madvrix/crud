# Generated by Django 2.2.17 on 2020-11-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_makanan', models.CharField(max_length=255)),
                ('jumlah', models.IntegerField(max_length=10)),
                ('harga', models.IntegerField(max_length=15)),
                ('produksi', models.DateField(null=True)),
                ('exp', models.DateField(null=True)),
            ],
            options={
                'ordering': ['nama_makanan'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
