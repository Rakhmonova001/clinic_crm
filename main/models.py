import qrcode.constants
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File


class User(AbstractUser):
    full_name = models.CharField(max_length=112, db_index=True, verbose_name="To'liq ism sharif")
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="Telefon raqam", validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number',
        )
    ])
    address = models.CharField(max_length=255, verbose_name="Manzil")

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.full_name

class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE)
    status = models.IntegerField(choices=(
        (1, "doctor"),
        (2, "manager"),
        (3, "admin"),
        (4, "nurse"),
        (5, "director"),
        (6, "cooker"),
    ))
    salary = models.PositiveIntegerField(verbose_name="Maosh")
    work_time = models.CharField(max_length=255, null=True, blank=True,verbose_name="Ish vaqti")
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE,  verbose_name="Xona")
    experince = models.CharField(max_length=255, verbose_name="Tajriba")
    bio = models.TextField(null=True, blank=True, verbose_name="Ma' lumot")
    age = models.IntegerField(default=18, verbose_name="Yosh")
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name="Bo'lim")

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Ishchilar'

    def __str__(self):
        return self.user.full_name

class Patient(models.Model):
    doctor = models.ForeignKey(to='Employee',on_delete=models.CASCADE, verbose_name="Doktor")
    full_name = models.CharField(max_length=200, db_index=True, verbose_name="To'liq ism sharif")
    age = models.IntegerField(default=18, verbose_name="Yosh")
    gender = models.IntegerField(default=1,choices=(
        (1, "Male"),
        (2, "Female"),
    ), verbose_name="Jins")
    address = models.CharField(max_length=200, verbose_name="Manzil")
    photo = models.ImageField(upload_to='patintent_phoot/', validators=[ImageFileValidator()])
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="Telefon raqam", validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number',
        )
    ])
    extra_phone_number = models.IntegerField(max_length=13, null=True, blank=True, verbose_name="Qo'shimcha telefon raqam")
    room = models.ForeignKey(to='Room', on_delete=models.CASCADE)
    bio = models.TextField()
    stayed_day = models.DateField(verbose_name="Necha kun qolishi")
    payment_status = models.IntegerField(default=3, choices=(
        (1, "full_paid"),
        (2, "part_paid"),
        (3, "unpaid"),
    ), verbose_name="To'lov  holati")

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Bemorlar'

    def __str__(self):
        return self.full_name

class Room(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    capacity = models.IntegerField(null=True, blank=True, verbose_name="Sig'imi")
    status = models.IntegerField(default=4, choices=(
        (1, "lux"),
        (2, "free"),
        (3, "econom"),
        (4, "other"),
    ), verbose_name="Holat")
    is_booked = models.BooleanField(default=False, verbose_name="Zakaz qilndi")
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, verbose_name="Bo'lim")
    equipment = models.ForeignKey(to='Equipment', on_delete=models.CASCADE, verbose_name="Jihoz")
    other_info = models.TextField(null=True, blank=True, verbose_name="Qo'shimcha  ma'lumot")

    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Xonalar'

    def __str__(self):
        return self.name

class Payment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name="Bemor")
    payment_amount = models.IntegerField(verbose_name="To'lov miqdori")
    payment_type = models.IntegerField(default=3, choices=(
        (1, "cash"),
        (2, "by_card"),
        (3, "other"),
    ), verbose_name="To'lov turi")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_date(f"Your data to encode in the QR code: {self.patient.full_name}")
        qr.make(fit=True)
        img = qr._image(fill_color="black", black="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)
    created_at = models.DateTimeField(auto_created=True, verbose_name="Yaratilgan ")

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Bemorlar'


class Comment(models.Model):
    patient = models.ForeignKey(to='Patient', on_delete=models.CASCADE, verbose_name="Bemor")
    text = models.CharField(max_length=200, verbose_name="Kommentariya")
    status = models.IntegerField(default=1, choices=(
        (1, 'comment'),
        (2, 'complain'),
        (3, 'suggest'),
    ))
    created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Kommentariyalar'

class Income(models.Model):
    amount = models.IntegerField(verbose_name="Jami_summma")
    reason = models.CharField(max_length=255, verbose_name="Sabab")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Yaratilgan")

    class Meta:
        verbose_name = 'Income'
        verbose_name_plural = 'Kirimlar'

class Revenue(models.Model):
    amount = models.IntegerField(verbose_name="Jami")
    reason = models.CharField(max_length=255, verbose_name="Sabab")
    created_at = models.DateTimeField(auto_created=True, verbose_name="Yaratilgan")

    class Meta:
        verbose_name = 'Revenue'
        verbose_name_plural = 'Chiqimlar'

class Cassa(models.Model):
    total_amount = models.PositiveIntegerField(default=0, verbose_name="Umumiy miqdori")

    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Kassallar'


class Operation(models.Model):
    employees = models.ManyToManyField(to='Employee', verbose_name="Doktorlar")
    date_time = models.DateTimeField(default=0, verbose_name="Boshlangan vaqt")
    start_time = models.DateTimeField(max_length=200, verbose_name="Tugagan vaqt")
    end_time = models.CharField(max_length=200, verbose_name="Tugagan vaqt")
    patient = models.ForeignKey(to='Patient',on_delete=models.CASCADE, verbose_name="Bemor")
    room = models.ForeignKey(to='Room',on_delete=models.CASCADE, verbose_name="Xona")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Yaratilgan")

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operatsiyalar'

class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Bolimlar'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Ism")
    number = models.CharField(max_length=200, verbose_name="Raqam")
    bio = models.TextField()
    extra_info = models.TextField(max_length=255, verbose_name="Qo'shimcha ma'lumot")

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Jihozlar'

    def __str__(self):
        return self.name

class Info_about_clinic(models.Model):
    total_patients_number = models.IntegerField( verbose_name="Umumiy kasallar soni")
    total_employees_number = models.IntegerField( verbose_name="Umumiy ishchilar soni")
    bio = models.TextField()
    address = models.CharField(max_length=255, verbose_name="Manzil")
    phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number',
        )
    ], verbose_name="Telefon raqam")

    class Meta:
        verbose_name = 'Info_about_clinic'
        verbose_name_plural = 'Klinika haqida malumotlar'


class Attendance(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ['employee', 'date']

def clean(self):
    if self.check_out and self.chrck_in < self.check_in:
        raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"





