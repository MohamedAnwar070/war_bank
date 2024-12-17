from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Account

def open_account(request):
    if request.method == 'POST':
        name = request.POST['name']
        pin = request.POST['pin']
        deposit = float(request.POST['deposit'])
        account = Account.objects.create(name=name, pin=pin, balance=deposit)
        return HttpResponse(f"Account created for {account.name} with balance Rs.{account.balance}.")
    return render(request, 'open_account.html')

def deposit_money(request):
    if request.method == 'POST':
        pin = request.POST['pin']
        amount = float(request.POST['amount'])
        try:
            account = Account.objects.get(pin=pin)
            account.balance += amount
            account.save()
            return HttpResponse(f"Deposit successful! New balance: Rs.{account.balance}.")
        except Account.DoesNotExist:
            return HttpResponse("Account not found.")
    return render(request, 'deposit.html')

def withdraw_money(request):
    if request.method == 'POST':
        pin = request.POST['pin']
        amount = float(request.POST['amount'])
        try:
            account = Account.objects.get(pin=pin)
            if account.balance >= amount:
                account.balance -= amount
                account.save()
                return HttpResponse(f"Withdrawal successful! New balance: Rs.{account.balance}.")
            else:
                return HttpResponse("Insufficient funds.")
        except Account.DoesNotExist:
            return HttpResponse("Account not found.")
    return render(request, 'withdraw.html')

def check_balance(request):
    if request.method == 'GET':
        pin = request.GET.get('pin')
        try:
            account = Account.objects.get(pin=pin)
            return render(request, 'check_balance.html', {'balance': account.balance})
        except Account.DoesNotExist:
            return HttpResponse("Account not found.")
    return render(request, 'check_balance.html')
