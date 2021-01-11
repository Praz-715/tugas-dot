from django.db import models

# Create your models here.
class Jabatan(models.Model):
    """Model definition for Jabatan."""

    # TODO: Define fields here
    nama_jabatan    = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """Meta definition for Jabatan."""

        verbose_name = 'Jabatan'
        verbose_name_plural = 'Jabatans'

    def __str__(self):
        """Unicode representation of Jabatan."""
        return "{}".format(self.nama_jabatan)

class Divisi(models.Model):
    """Model definition for Divisi."""

    # TODO: Define fields here
    nama_divisi    = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        """Meta definition for Divisi."""

        verbose_name = 'Divisi'
        verbose_name_plural = 'Divisis'

    def __str__(self):
        """Unicode representation of Divisi."""
        return "{}".format(self.nama_divisi)

class Karyawan(models.Model):
    """Model definition for Karyawan."""

    # TODO: Define fields here
    nik             = models.CharField(max_length=15, unique=True, null=False, blank=False, primary_key=True)
    nama_karyawan   = models.CharField(max_length=100, null=False, blank=False)
    alamat          = models.TextField()
    jk              = models.CharField(max_length=10, choices=[('L','Laki-laki'),('P','Perempuan')], null=False, blank=False)
    agama           = models.CharField(max_length=10, choices=[('IS','Islam'),('KR','Kristen'),('HI','Hindu'),('BD','Budha'),('KH','Konghucu')], null=True, blank=True)
    tlp             = models.CharField(max_length=13, null=True, blank=True)
    jabatan         = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    divisi          = models.ForeignKey(Divisi, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Karyawan."""

        verbose_name = 'Karyawan'
        verbose_name_plural = 'Karyawans'

    def __str__(self):
        """Unicode representation of Karyawan."""
        return "{}".format(self.nama_karyawan)

class Absensi(models.Model):
    """Model definition for Absensi."""

    # TODO: Define fields here
    nik         = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    tanggal     = models.DateField(null=False, blank=False)
    masuk       = models.TimeField(null=True, blank=True)
    pulang      = models.TimeField(null=True, blank=True)
    status_absen = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        """Meta definition for Absensi."""

        verbose_name = 'Absensi'
        verbose_name_plural = 'Absensis'

    def __str__(self):
        """Unicode representation of Absensi."""
        return "{} - {}".format(self.nik, self.tanggal)

class ListJob(models.Model):
    """Model definition for ListJob."""

    # TODO: Define fields here
    nama_job    = models.CharField(max_length=200, null=True, blank=True)
    deadline    = models.DateTimeField(null=True, blank=True)
    status      = models.BooleanField(auto_created=False)
    nik         = models.ForeignKey(Karyawan, on_delete=models.CASCADE)
    class Meta:
        """Meta definition for ListJob."""

        verbose_name = 'ListJob'
        verbose_name_plural = 'ListJobs'

    def __str__(self):
        """Unicode representation of ListJob."""
        pass



