# Generated by Django 3.1.5 on 2021-01-11 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_divisi', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Divisi',
                'verbose_name_plural': 'Divisis',
            },
        ),
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jabatan', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Jabatan',
                'verbose_name_plural': 'Jabatans',
            },
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=15, unique=True)),
                ('nama_karyawan', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('jk', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10)),
                ('agama', models.CharField(blank=True, choices=[('IS', 'Islam'), ('KR', 'Kristen'), ('HI', 'Hindu'), ('BD', 'Budha'), ('KH', 'Konghucu')], max_length=10, null=True)),
                ('tlp', models.CharField(blank=True, max_length=13, null=True)),
                ('divisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitorwfh.divisi')),
                ('jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitorwfh.jabatan')),
            ],
            options={
                'verbose_name': 'Karyawan',
                'verbose_name_plural': 'Karyawans',
            },
        ),
    ]
