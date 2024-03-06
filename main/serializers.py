from rest_framework import serializers
from .models import *

class UserSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = User
        fields = ("full_name", "phone_number", "address")


class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Employee
        fields = ("user", "status", "salary", "room", "experince", "bio", "age", "department")


class PatientSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Patient
        fields = ("doctor", "full_name", "age", "gender", "address", "photo", "phone_number", "extra_phone_number", "room", "bio", "stayed_day", "payment_status")


class RoomSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Room
        fields = ("name", "capacity", "status", "is_booked", "department", "equipment", "other_info")


class PaymentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Payment
        fields = ("patient", "payment_amount", "payment_type", "qr_code")


class CommentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Comment
        fields = ("patient", "text", "status", "created_at")


class IncomeSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Income
        fields = ("amount", "reason", "created_at")


class RevenueSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Revenue
        fields = ("amount", "reason", "created_at")


class CassaSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Cassa
        fields = ('__all__')


class OperationSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Operation
        fields = ("employees", "date_time", "start_time", "end_time", "patient", "room", "created_at")


class DepartmentSer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Department
        fields = ('__all__')


class EquipmentSer(serializers.ModelSerializer):
    depth = 1
    model = Equipment
    fields = ("name", "number", "bio", "extra_info")


class Info_about_clinicSer(serializers.ModelSerializer):
    depth = 1
    model = Info_about_clinic
    fields = ("total_patients_number", "total_employees_number", "bio", "address", "phone_number")


class AttendanceSer(serializers.ModelSerializer):
    depth = 1
    model = Attendance
    fields = ("employee", "date", "check_in", "check_out")













