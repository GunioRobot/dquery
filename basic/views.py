from basic.models import *
from django.http import HttpResponse 
from django.template import Context 
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from basic.forms import *

def toys_list(request):
    toys = Toy.objects.all()
    variables = RequestContext(request,{
        'toys': toys, 
        'show_detail': True,
        })
    return render_to_response(
            'basic/list.html', variables)

def toys_detail(request, toy_id):
    toy = get_object_or_404(Toy, pk=toy_id)
    variables = RequestContext(request,{
        'toy': toy,
        'show_edit': True,
        })
    return render_to_response(
            'basic/details.html', variables)

def toys_add(request):
    if request.method == 'POST':
        form = ToySaveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/toys/')
    else: 
        form = ToySaveForm()
    variables = RequestContext(request,{
        'form': form,
        })
    return render_to_response(
            'basic/add.html', variables)

def toys_edit(request, toy_id):
    ajax = 'ajax' in request.GET
    if request.method == 'POST':
        toy = get_object_or_404(Toy, pk=toy_id)
        form = ToySaveForm(request.POST, instance=toy)
        if form.is_valid():
            form.save()
            if ajax:
                toy = get_object_or_404(Toy, pk=toy_id)
                form = ToySaveForm(instance=toy)
                variables = RequestContext(request,{
                    'form': form,
                    })
                return render_to_response(
                        'basic/add.html', variables)
            else:
                return HttpResponseRedirect('/toys/')
        else:
            if ajax:
                return HttpResponse(u'Fail!')
    else:
        toy = get_object_or_404(Toy, pk=toy_id)
        form = ToySaveForm(instance=toy)
        variables = RequestContext(request,{
            'form': form,
            })
        return render_to_response(
                'basic/add.html', variables)

def _toys_edit(request, toy_id):
    if request.method == 'POST':
        toy = get_object_or_404(Toy, pk=toy_id)
        form = ToySaveForm(request.POST, instance=toy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/toys/')
    else:
        toy = get_object_or_404(Toy, pk=toy_id)
        form = ToySaveForm(instance=toy)
        variables = RequestContext(request,{
            'form': form,
            })
        return render_to_response(
                'basic/add.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/toys/')
