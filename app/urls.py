from django.urls import path
from .views import HomePageView, SignUpView, AttendanceListView, CustomUserDetailView, AttendanceCreateView, PaySlipView, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('users/signup/', SignUpView.as_view(), name='signup'),
    path('attendance/', AttendanceListView.as_view(), name='article_list'),
    path('profile/<int:pk>/', CustomUserDetailView.as_view(), name='profile'),
    path('attendance/new', AttendanceCreateView.as_view(), name='article_new'),
    path('payslip/', PaySlipView.as_view(), name='payslip'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
