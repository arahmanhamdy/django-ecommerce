from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import MyUserCreationForm


def register(request):
    if request.user.is_authenticated():
        return redirect('pages:index')
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_done')
    context = {'form': form}
    return render(request, 'registration/registration_form.html', context)


class RegisterDoneView(TemplateView):
    template_name = 'registration/registration_done.html'
