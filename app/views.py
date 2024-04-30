from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Attendance, CustomUser

class HomePageView(TemplateView):
    template_name = 'home.html'

class PaySlipView(TemplateView):
    template_name = 'payslip.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'registration/signup.html'

class AttendanceListView(LoginRequiredMixin, ListView):
  model = Attendance
  template_name = 'attendance_list.html'
  login_url = 'login'
  def get_queryset(self):
    return Attendance.objects.filter(person=self.request.user)

class CustomUserDetailView(LoginRequiredMixin, DetailView): 
  model = CustomUser
  template_name = 'attendance_detail.html'
  login_url = 'login'
  def get_queryset(self):
     queryset = super().get_queryset()
     return queryset.filter(pk=self.request.user.pk)
  
class AttendanceCreateView(LoginRequiredMixin, CreateView):
  model = Attendance
  template_name = 'attendance_new.html'
  fields = ('person','time_in', 'time_out')
  login_url = 'login' 
  #redirect nalang kulang tsaka auto().now


  
