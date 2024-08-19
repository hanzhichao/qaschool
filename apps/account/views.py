from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                # return HttpResponse('Invalid login')
                return HttpResponse("<script>toastr.success('评论提交成功');</script>")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')