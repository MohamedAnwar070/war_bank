from django.urls import path
from . import views

urlpatterns = [
    path('open_account/', views.open_account, name='open_account'),
    path('deposit/', views.deposit_money, name='deposit_money'),
    path('withdraw/', views.withdraw_money, name='withdraw_money'),
    path('check_balance/', views.check_balance, name='check_balance'),
]
