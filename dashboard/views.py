from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


""" start CRUD Employee model """
#read_employee_object
class GetAllEmployeeItems(ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSer


#create_employee_object
class CreateEmployeeApiView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


#update_employee_object
class UpdateEmployeeApiView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


#delete_employee_objects
class DeleteEmployeeApiView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSer


""" start CRUD Patient model """
#read_patient_objects
class GetAllPatientItems(ListCreateAPIView):
    queryset = Patient.objects.all().order_by('-id')
    serializer_class = PatientSer


#create_patient_objects
class CreatePatientApiView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSer


#update_patient_objects
class UpdatePatientApiView(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSer


#delete_patient_objects
class DeletePatientApiView(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSer


""" start CRUD Room model """
#read_room_objects
class GetAllRoomItems(ListCreateAPIView):
    queryset = Room.objects.all().order_by('-id')
    serializer_class = RoomSer


#create_room_objects
class CreateRoomApiView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSer


#update_room_objects
class UpdateRoomApiView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSer


#delete_room_objects
class DeleteRoomApiView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSer


""" start CRUD Payment model """
#read_payment_objects
class GetAllPaymentItems(ListCreateAPIView):
    queryset = Payment.objects.all().order_by('-id')
    serializer_class = PaymentSer


#create_payment_objects
class CreatePaymentApiView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer

class UpdatePaymentApiView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer

class DeletePaymentApiVew(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSer


""" start CRUD Comment model """
#read_comment_objects
class GetAllCommentItems(ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSer


#create_comment_objects
class CreateCommentApiView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


#update_comment_objects
class UpdateCommentApiView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


#delete_comment_objects
class DeleteCommnetApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSer


""" start CRUD Income model """
#read_income_objects
class GetAllIncomeItems(ListCreateAPIView):
    queryset = Income.objects.all().order_by('-id')
    serializer_class = IncomeSer


#read_income_objects
class CreateIncomeAPiView(CreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSer


#update_income_objects
class UpdateIncomeApiView(UpdateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSer


#delete_income_objects
class DeleteIncomeApiView(DestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSer


""" start CRUD Revenue model """
#read_revenue_objects
class GetAllRevenueItems(ListCreateAPIView):
    queryset = Revenue.objects.all().order_by('-id')
    serializer_class = RevenueSer


#create_revenue_objects
class CreateRevenueApiView(CreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSer


#update_revenue_objects
class UpdateRevenueApiView(UpdateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSer


#delete_revenue_objects
class DeleteRevenueApiView(DestroyAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSer


""" start CRUD Cassa model """
#read_cassa_objects
class GetAllCassaItems(ListCreateAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSer


#create_cassa_objects
class CreateCassaApiView(CreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


#update_cassa_objects
class UpdateCassaApiView(UpdateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


#delete_cassa_objects
class DeleteCassaApiView(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSer


""" start CRUD Operation model """
#read_operation_objects
class GetAllOperationItems(ListCreateAPIView):
    queryset = Operation.objects.all().order_by('-id')
    serializer_class = OperationSer


#create_operation_objects
class CreateOperationApiView(CreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSer


#update_operation_objects
class UpdateOperationApiView(UpdateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSer


#delete_operation_objects
class DeleteOperationApiView(DestroyAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSer


""" start CRUD Department model """
#read_department_objects
class GetAllDepartmentApiView(ListCreateAPIView):
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSer


#create_department_objects
class CraeteDepartmentApiView(CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSer


#update_department_objects
class UpdateDepartmentApiView(UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSer


#delete_department_objects
class DeleteDepartmentApiView(DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSer


""" start CRUD Equipment model """
#read_equipment_objects
class GetAllEquipmentItems(ListCreateAPIView):
    queryset = Equipment.objects.all().order_by('-id')
    serializer_class = EquipmentSer


#create_equipment_objects
class CreateEquipmentApiView(CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSer


#update_equipment_objects
class UpdateEquipmentApiView(UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSer


#delete_equipment_objects
class DeleteEquipmentApiView(DestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSer


""" start CRUD Info_about_clinic model """
#read_info_about_clinic_objects
class GetAllInfo_about_clinicItems(ListCreateAPIView):
    queryset = Info_about_clinic.objects.all().order_by('-id')
    serializer_class = Info_about_clinicSer


#create_info_about_clinic_objects
class CreateInfo_about_clinicApiView(CreateAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSer


#update_info_about_clinic_objects
class UpdateInfo_about_clinicApiView(UpdateAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSer


#delete_info_about_clinic_objects
class DeleteInfo_about_clinicApiView(DestroyAPIView):
    queryset = Info_about_clinic.objects.all()
    serializer_class = Info_about_clinicSer


""" start CRUD Attendance model """
#read_attendance_objects
class GetAllAttendanceItems(ListCreateAPIView):
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = AttendanceSer


#create_attendance_objects
class CreateAttendanceApiView(CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer


#update_attendance_objects
class UpdateAttendanceApiView(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer


#delete_attendance_objects
class DeleteAttendanceApiView(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSer





