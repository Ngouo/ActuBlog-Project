from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('user-login')
  else:
    form = SignUpForm()
  context = {
    'form': form,
  }
  return render(request, 'Utilisateurs/sign_up.html', context)


@login_required
def profil_user(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      return redirect('profil_user')
                                                                          #cette fonction permet de metre a jour les informations sur son profil
  else:                                                                   #aprèes l'avoir créé (23e à la 38e ligne)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    
  context = {
    'u_form': u_form,
    'p_form': p_form,
  }
  return render(request, 'Utilisateurs/profil_user.html', context)



def deconnection(request):
  logout(request)
  return render(request, 'Utilisateurs/logout.html')