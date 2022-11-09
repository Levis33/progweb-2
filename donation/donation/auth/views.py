from donation.mailer import alert_staff
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

from donation.mailer import send_email
from django.contrib.auth.models import User
from donation.auth.forms import registerForm

from logger.models import LogEvents
from logger.functions import log_event

from django.contrib.auth import get_user_model

user = get_user_model()


class PasswordChangeView(views.PasswordChangeView):
    def post(self, request):
        response = super().post(request)

        if response.status_code == 302:
            send_email(request.user.email, 3, {
                'user': request.user
            })

        log_event(request, LogEvents.USER_CHANGED_PASSWORD)

        return response


def registerView(request):
    form = registerForm()

    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = True

            user.save()
            # alert_staff(1, {'nome': form.cleaned_data['nome'],
            #                 'email': form.cleaned_data['email'],
            #                 'link': request.META['HTTP_HOST'] + '/admin/auth/user/'})

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context=context)


class UserLoginView(views.LoginView):
    def post(self, request):
        response = super().post(request)

        # username = request.POST['username'].strip() utilizar com log
        if response.status_code == 302:
            pass
            # log_event(request, LogEvents.USER_LOGGED_IN, description=username)
        else:
            # user = None utilizar com log
            try:
                pass
                # user = User.objects.get(email=username)  utilizar com o log
            except User.DoesNotExist:
                pass

            # log_event(request, LogEvents.USER_FAILED_LOGIN, user=user, description=username)

        return response

    def get_success_url(self):
        return reverse('home')


@login_required
def logoutView(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
