from django.contrib import admin
from .models import Jabatan, Divisi, Karyawan, ListJob, Absensi
# Register your models here.
admin.site.register(Absensi)
admin.site.register(ListJob)
admin.site.register(Karyawan)