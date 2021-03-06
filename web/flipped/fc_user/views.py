from django.shortcuts import render
import forms
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth import login,authenticate

def register(request):
    if request.method == 'GET':
        form = forms.RegisterForm()
    elif request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            from django.contrib.auth.models import User
            cd = form.cleaned_data;
            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            user = authenticate(username=cd['username'],password=cd['password'])
            login(request,user)
            return HttpResponseRedirect('/common/home/')
    return render(request,'fc_user/register.html',dict(form=form)) 
    

from django.utils.translation import ugettext as _
from django.http import HttpResponse
def trans(request):
    outputs = [_("username") , _("first_name") , _("last_name")] 
    return HttpResponse('<br/>'.join(outputs))
