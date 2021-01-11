from .models import Jabatan, Divisi
from rest_framework import serializers

class JabatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jabatan
        fields = ['id', 'nama_jabatan']


class DivisiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divisi
        fields = ['id', 'nama_divisi']