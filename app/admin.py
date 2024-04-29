from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from app.models import Department, Attendance, SalaryGrade, PayrollSlip, Requirements
from .models import CustomUser

admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(SalaryGrade)
admin.site.register(PayrollSlip)
admin.site.register(Requirements)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff' ]

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
