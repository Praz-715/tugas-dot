from .models import Jabatan, Divisi, Karyawan, Absensi, ListJob
from .serializers import JabatanSerializer, DivisiSerializer, KaryawanSerializer, AbsensiSerializer, ListJobSerializer
from rest_framework import viewsets

class JabatanView(viewsets.ModelViewSet):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    

class DivisiView(viewsets.ModelViewSet):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer

class KaryawanView(viewsets.ModelViewSet):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer

class AbsensiView(viewsets.ModelViewSet):
    queryset = Absensi.objects.all()
    serializer_class = AbsensiSerializer

class ListJobView(viewsets.ModelViewSet):
    queryset = ListJob.objects.all()
    serializer_class = ListJobSerializer
    