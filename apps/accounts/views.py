from django.shortcuts import render

def accounts(request):
    print("*********************views/accounts")
    return render(request, 'accounts/accounts.html')
