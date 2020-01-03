from django.shortcuts import render

def accounts(request):
    print("*********accounts views.oy*********")
    return render(request, 'accounts/accounts.html')
