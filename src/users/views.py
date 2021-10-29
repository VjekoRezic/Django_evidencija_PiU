from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@user_passes_test(lambda u: u.is_superuser)
def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Stvoren korisnik {username}')
            return redirect('user-get')

    else:

        form = UserCreationForm()
    return render(request, 'users/create.html', {'form':form})




@user_passes_test(lambda u: u.is_superuser)
def getUsers(request):
    
    User = get_user_model()
    users = User.objects.all()

    return render(request,'users/users.html', {"users":users})


@user_passes_test(lambda u: u.is_superuser)
def deleteUser(request):
    if request.method == 'POST':
        id = request.POST.get('userid', None)
        print(request.POST)
        print(id)
        
        User = get_user_model()
        users = User.objects.filter(id=int(id))
        users.delete()
        return HttpResponse("Korisnik izbrisan")
    return HttpResponse("Bad request", 400)
    