from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


"""  Start EMPLOYEE model  """
@api_view(['GET'])
def filter_employee_username(request):
    username = request.GET.get('full_name')
    users = Employee.objects.filter(user__icontains=username).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emoloyee_status(request):
    username = request.GET.get('status')
    users = Employee.objects.filter(status__icontains=username).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emoloyee_experience(request):
    experience = request.GET.get('experience')
    users = Employee.objects.filter(experience__icontains=experience).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emoloyee_room(request):
    room_id = request.GET.get('room_id')
    users = Employee.objects.filter(room_id=room_id).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_emoloyee_department(request):
    department_id = request.GET.get('department_id')
    users = Employee.objects.filter(department_id=department_id).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_emoloyee_salary(request):
    salary = request.GET.get('salary')
    users = Employee.objects.filter(salary__icontains=salary).order_by('-id')
    ser = EmployeeSer(users, many=True)
    return Response(ser.data)


"""  Start PATIENT model  """
@api_view(['GET'])
def filter_patient_doctor(request):
    doctor_id = request.GET.get('doctor_id')
    users = Patient.objects.filter(doctor_id=doctor_id).order_by('-id')
    ser = PatientSer(users, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_patient_gender(request):
    gender = request.GET.get('Male')
    users = Patient.objects.filter(gender=gender).order_by('-id')
    ser = PatientSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_phone_number(request):
    phone_number = request.GET.get('phone_number')
    users = Patient.objects.filter(phone_number=phone_number).order_by('-id')
    ser = PatientSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_room(request):
    room = request.GET.get('bolalar')
    users = Patient.objects.filter(room=room).order_by('-id')
    ser = PatientSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_patient_payment_status(request):
    payment_status = request.GET.get('paid')
    users = Patient.objects.filter(payment_status=payment_status).order_by('-id')
    ser = PatientSer(users, many=True)
    return Response(ser.data)


"""  Start ROOM model  """
@api_view(['GET'])
def filter_room_name(request):
    name = request.GET.get('name')
    users = Room.objects.filter(name=name).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_department(request):
    department_id = request.GET.get('department')
    users = Room.objects.filter(department_id=department_id).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_status(request):
    status = request.GET.get('lux')
    users = Room.objects.filter(status=status).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_capasity(request):
    capasity = request.GET.get('capasity')
    users = Room.objects.filter(capasity=capasity).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_is_booked(request):
    is_booked = request.GET.get('is_booked')
    users = Room.objects.filter(is_booked=is_booked).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_equipment(request):
    equipment_id = request.GET.get('equipment')
    users = Room.objects.filter(equipment_id=equipment_id).order_by('-id')
    ser = RoomSer(users, many=True)
    return Response(ser.data)


"""  Start PAYMENT model  """
@api_view(['GET'])
def filter_payment_patient(request):
    patient = request.GET.get('patient')
    users = Payment.objects.filter(patient_id=patient).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_created_at(request):
    created_at = request.GET.get('created_at')
    users = Payment.objects.filter(created_at=created_at).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_payment_type(request):
    payment_type = request.GET.get('payment_type')
    users = Payment.objects.filter(payment_type=payment_type).order_by('-id')
    ser = PaymentSer(users, many=True)
    return Response(ser.data)


"""  Start COMMENT model  """
@api_view(['GET'])
def filter_comment_status(request):
    status = request.GET.get('status')
    users = Comment.objects.filter(status=status).order_by('-id')
    ser = CommentSer(users, many=True)
    return Response(ser.data)


"""  Start INCOME model  """
@api_view(['GET'])
def filter_income_created_at(request):
    created_at = request.GET.get('created_at')
    users = Income.objects.filter(created_at=created_at).order_by('-id')
    ser = IncomeSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_income_amount(request):
    amount = request.GET.get('amount')
    users = Income.objects.filter(amount=amount).order_by('-id')
    ser = IncomeSer(users, many=True)
    return Response(ser.data)


"""  Start RAVENUE model  """
@api_view(['GET'])
def filter_ravenue_created_at(request):
    created_at = request.GET.get('created_at')
    users = Ravenue.objects.filter(created_at=created_at).order_by('-id')
    ser = RavenueSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_ravenue_amount(request):
    amount = request.GET.get('amount')
    users = Ravenue.objects.filter(amount__icontains=amount).order_by('-id')
    ser = RavenueSer(users, many=True)
    return Response(ser.data)


"""  Start OPERATION model  """
@api_view(['GET'])
def filter_operation_employee(request):
    employees_user_id = request.GET.get('employees')
    users = Operation.objects.filter(employees_user_id=employees_user_id).order_by('-id')
    ser = OperationSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_date_time(request):
    date_time = request.GET.get('date_time')
    users = Operation.objects.filter(date_time__icontains=date_time).order_by('-id')
    ser = OperationSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_operation_patient(request):
    patient_id = request.GET.get('patient')
    users = Operation.objects.filter(patient_id=patient_id).order_by('-id')
    ser = OperationSer(users, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_operation_room(request):
    room_id = request.GET.get('room')
    users = Operation.objects.filter(room_id=room_id).order_by('-id')
    ser = OperationSer(users, many=True)
    return Response(ser.data)


"""  Start DEPARMENT model  """
@api_view(['GET'])
def filter_department_name(request):
    name = request.GET.get('name')
    users = Department.objects.filter(name=name).order_by('-id')
    ser = DepartmentSer(users, many=True)
    return Response(ser.data)


"""  Start EQUMENT model  """
@api_view(['GET'])
def filter_equipment_name(request):
    name = request.GET.get('name')
    users = Equipment.objects.filter(name=name).order_by('-id')
    ser = EquipmentSer(users, many=True)
    return Response(ser.data)


"""  Start ATTENDANCE model  """
@api_view(['GET'])
def filter_attendence_employee(request):
    employee = request.GET.get('employee')
    users = Attendence.objects.filter(employee=employee).order_by('-id')
    ser = AttendenceSer(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_attendence_date(request):
    date = request.GET.get('date')
    users = Attendence.objects.filter(date=date).order_by('-id')
    ser = AttendenceSer(users, many=True)
    return Response(ser.data)
