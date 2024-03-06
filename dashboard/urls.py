from django.urls import path
from .views import *

urlpatterns = [
    #>>>>>>>>>>>>>>>>> CRUD urls Employee Items <<<<<<<<<<<<<
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee/', CreateEmployeeApiView.as_view()),
    path('update-employee/', UpdateEmployeeApiView.as_view()),
    path('delete-employee/', DeleteEmployeeApiView.as_view()),


    #>>>>>>>>>>>>>>>>> CRUD urls Patient Items <<<<<<<<<<<<<
    path('get-patient-items/', GetAllPatientItems.as_view()),
    path('create-patient/', CreatePatientApiView.as_view()),
    path('update-patient/', UpdatePatientApiView.as_view()),
    path('delete-patient/', DeletePatientApiView.as_view()),


    #>>>>>>>>>>>>>>>>>> CRUD urls Room Items <<<<<<<<<<
    path('get-room-items/', GetAllRoomItems.as_view()),
    path('create-room/', CreateRoomApiView.as_view()),
    path('update-room/', UpdateRoomApiView.as_view()),
    path('delete-room/', DeleteRoomApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Payment Itmes <<<<<<<<<<
    path('get-payment-items/', GetAllPaymentItems.as_view()),
    path('create-payment/', CreatePaymentApiView.as_view()),
    path('update-payment/', UpdatePaymentApiView.as_view()),
    path('delete-payment/', DeletePaymentApiVew.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Commnet Items <<<<<<<<<<
    path('get-comment-items/', GetAllCommentItems.as_view()),
    path('create-comment/', CreateCommentApiView.as_view()),
    path('update-comment/', UpdateCommentApiView.as_view()),
    path('delete-comment/', DeleteCommnetApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Income Items <<<<<<<<<<<<
    path('get-income-items/', GetAllIncomeItems.as_view()),
    path('create-income/', CreateIncomeAPiView.as_view()),
    path('update-income/', UpdateIncomeApiView.as_view()),
    path('delete-income/', DeleteIncomeApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Revenue Items <<<<<<<<<<<<
    path('get-revenue-items/', GetAllRevenueItems.as_view()),
    path('create-revenue/', CreateRevenueApiView.as_view()),
    path('update-revenue/', UpdateRevenueApiView.as_view()),
    path('delete-revenue/', DeleteRevenueApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Cassa Items <<<<<<<<<<<
    path('get-cassa-items/', GetAllCassaItems.as_view()),
    path('create-cassa/', CreateCassaApiView.as_view()),
    path('update-cassa/', UpdateCassaApiView.as_view()),
    path('delete-cassa/', DeleteCassaApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Operation Items <<<<<<<<<<<<<<<
    path('get-operation-items/', GetAllOperationItems.as_view()),
    path('create-operation/', CreateOperationApiView.as_view()),
    path('update-operation/', UpdateOperationApiView.as_view()),
    path('delete-operation/', DeleteOperationApiView .as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Department Items <<<<<<<<<<<<<<<<<
    path('get-department-items', GetAllDepartmentApiView.as_view()),
    path('create-department/', GetAllDepartmentApiView.as_view()),
    path('update-department/', UpdateDepartmentApiView.as_view()),
    path('delete-department/', DeleteDepartmentApiView.as_view()),


    #>>>>>>>>>>>>>>>> CRUD urls Equipment Items <<<<<<<<<<<<<<<<<<<<<<
    path('get-equipment-items/', GetAllEquipmentItems.serializer_class),
    path('create-equipment/', CreateEquipmentApiView.serializer_class),
    path('update-equipment/<int:pk>/', UpdateEquipmentApiView.serializer_class),
    path('delete-equipment/<int:pk>/', DeleteEquipmentApiView.serializer_class),


    #>>>>>>>>>>>>>>>> CRUD urls Info_about_clinic Items <<<<<<<<<<<<<<<<<<<<<<
    path('get-info-about-clinic-items/', GetAllInfo_about_clinicItems.as_view()),
    path('create-info-about-clinic/', CreateInfo_about_clinicApiView.as_view()),
    path('update-info-about-clinic/', UpdateInfo_about_clinicApiView.as_view()),
    path('delete-info-about-clinic/', DeleteInfo_about_clinicApiView.as_view()),


    #>>>>>>>>>>>>>> CRUD urls Attendance Items <<<<<<<<<<<<<<<<<<<<<<<<<<
    path('get-attendance-items/', GetAllAttendanceItems.as_view()),
    path('create-attendance/', CreateAttendanceApiView.as_view()),
    path('update-attendance/', UpdateAttendanceApiView.as_view()),
    path('delete-attendance/', DeleteAttendanceApiView.as_view()),
]