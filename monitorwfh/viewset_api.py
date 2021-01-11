from .models import Jabatan, Divisi
from .serializers import JabatanSerializer, DivisiSerializer
from rest_framework import viewsets

class JabatanView(viewsets.ModelViewSet):
    queryset = Jabatan.objects.all()
    serializer_class = JabatanSerializer
    

class DivisiView(viewsets.ModelViewSet):
    queryset = Divisi.objects.all()
    serializer_class = DivisiSerializer
    