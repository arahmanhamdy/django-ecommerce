from django.shortcuts import render, redirect
from .forms import MyUserCreationForm


def register(request):
    if request.user.is_authenticated():
        return redirect('index:index')
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_done')
    context = {'form': form}
    return render(request, 'registration/registration_form.html', context)
