from django.urls import path
from .views import *


urlpatterns = [
    #>>>>>>>>>>>>>>>> FILTER Employee <<<<<<<<<<<<<<<<<<#
    path('filter-employee-user/', filter_employee_username),
    path('filter-employee-status/', filter_emoloyee_status),
    path('filter-employee-experience/', filter_emoloyee_experience),
    path('filter-employee-room/', filter_emoloyee_room),
    path('filter-employee-department/', filter_emoloyee_department),
    path('filter-employee-salary/', filter_emoloyee_salary),


    #>>>>>>>>>>>>>>>> FILTER Patient <<<<<<<<<<<<<<<<#
    path('filter-patient-doctor/', filter_patient_doctor),
    path('filter-patient-gender/', filter_patient_gender),
    path('filter-patient-phone_number/', filter_patient_phone_number),
    path('filter-patient-room/', filter_patient_room),
    path('filter-patient-payment-status/', filter_patient_payment_status),


    #>>>>>>>>>>>>>>> FILTER Room <<<<<<<<<<<<#
    path('filter-room-name/', filter_room_name),
    path('filter-room-status/', filter_room_status),
    path('filter-room-capasity/', filter_room_capasity),
    path('filter-room-equipment/', filter_room_equipment),
    path('filter-room-department/', filter_room_department),
    path('filter-room-is-booked/', filter_room_is_booked),


    #>>>>>>>>>>>>>>>> FILTER Payment <<<<<<<<<<<<<<<<#
    path('filter-comment-status/', filter_comment_status),
    path('filter-payment-patient/', filter_payment_patient),
    path('filter-payment-created-at/', filter_payment_created_at),
    path('filter-payment-payment-type/', filter_payment_payment_type),


    #>>>>>>>>>>>>>>>>>>> FILTER Income <<<<<<<<<<<<<<<<<<<<#
    path('filter-income-created-at/', filter_income_created_at),
    path('filter-income-amount/', filter_income_amount),


    #>>>>>>>>>>>>>>>>>>> FILTER Revenue <<<<<<<<<<<<<<<<<<#
    path('filter-revenue-patient/', filter_ravenue_created_at),
    path('filter-revenue-amount/', filter_ravenue_amount),


    #>>>>>>>>>>>>>>>>>>> FILTER Operation <<<<<<<<<<<<<<<<<<<<<#
    path('filter-operation-employees/', filter_operation_employee),
    path('filter-operation-date-time/', filter_operation_date_time),
    path('filter-operation-patient/', filter_operation_patient),
    path('filter-operation-room/', filter_operation_room),


    # >>>>>>>>>>>>>>>>>> FILTER Department <<<<<<<<<<<<<< #
    path('filter-department-name/', filter_department_name),


    #>>>>>>>>>>>>>>>>>>>FFILTER Equipment <<<<<<<<<<<<<<<#
    path('filter-equipment-name/', filter_equipment_name),


    #>>>>>>>>>>>>>>>>>> FILTER Attendence <<<<<<<<<<<<<<<<<<<<#
    path('filter-attendence-employee/', filter_attendence_employee),
    path('filter-attendence-date/', filter_attendence_date),

]