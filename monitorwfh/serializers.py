from .models import Jabatan, Divisi, Karyawan, Absensi, ListJob
from rest_framework import serializers

class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ['id', 'nama_jabatan']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'nama_divisi']

class KaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = ['nik', 'nama_karyawan', 'alamat', 'jk', 'agama', 'tlp', 'jabatan', 'divisi']

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = ['id', 'nik', 'tanggal', 'masuk', 'pulang', 'status_absen']

class ListJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListJob
        fields = ['id', 'nama_job', 'deadline', 'status', 'nik', 'progres']