from django.urls import path
from Utilisateurs.views import sign_up, profil_user,deconnection
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    path('profil_user', profil_user, name='profil_user'),
    path("login_user", auth_view.LoginView.as_view(template_name='Utilisateurs/login.html'), name='user-login'),
    path("deconnexion", deconnection, name='deconnection'),
    path("password_reset", auth_view.PasswordResetView.as_view(template_name='Utilisateurs/password_reset.html'),name='password_reset'),
    path("password_reset_done", auth_view.PasswordResetDoneView.as_view(template_name='Utilisateurs/password_reset_done.html'),name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>", auth_view.PasswordResetConfirmView.as_view(template_name='Utilisateurs/password_reset_confirm.html'),name='password_reset_confirm'),
    path("password_reset_complete", auth_view.PasswordResetCompleteView.as_view(template_name='Utilisateurs/password_reset_complete.html'), name='password_reset_complete')
]
