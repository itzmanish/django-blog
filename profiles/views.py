from django.shortcuts import render


def my_account(request):
    return render(request, 'signup.html')
