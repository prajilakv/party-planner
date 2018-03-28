from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response
from django.db.models import Sum

from .forms import GuestForm, FinanceForm, BuffetForm
from .models import Guests, Finance, Buffet

from django.contrib import messages
from django.shortcuts import redirect
from django.forms import modelformset_factory

from rest_framework import viewsets
from .serializers import FinanceSerializer, GuestsSerializer


class GuestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer


class FinanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


# Create your views here.

def dashboard(request):
    guests = {}
    finance = {}
    guest_form = GuestForm()
    finance_form = FinanceForm()

    if Buffet.objects.filter(id=1).exists():
        instance = Buffet.objects.get(id=1)
        buffet_form = BuffetForm(instance=instance)
    else:
        buffet_form = BuffetForm()

    GuestFormSet = modelformset_factory(Guests, fields="__all__")
    if request.method == 'POST' and 'guest' in request.POST:
        guestformset = GuestFormSet(request.POST, request.FILES)
        if guestformset.is_valid():
            guestformset.save()
    else:
        guestformset = GuestFormSet()

    FinanceFormSet = modelformset_factory(Finance, fields="__all__")
    if request.method == 'POST' and 'fin' in request.POST:
        financeformset = FinanceFormSet(request.POST, request.FILES)
        if financeformset.is_valid():
            financeformset.save()
    else:
        financeformset = FinanceFormSet()

    fin_list = finance_calc(request)
    guest_count = fin_list[0]
    total_cost = fin_list[1]

    return render(request, 'dashboard.html', {'guest_form': guest_form, 'finance_form': finance_form,
                  'guests': guestformset, 'finance': financeformset, 'buffet_form': buffet_form,
                  "gcount": guest_count, "total_cost": total_cost})


def add_guest(request):
    if request.method == 'POST':
        guest_form = GuestForm(request.POST)
        if guest_form.is_valid():
            guests = guest_form.save()
            #return HttpResponseRedirect(reverse('dashboard'))
            return redirect('dashboard')
        else:
            messages.error(request, "not valid")
    else:
        guest_form = GuestForm()
    return dashboard(request)


def add_finance(request):
    if request.method == 'POST':
        finance_form = FinanceForm(data=request.POST)
        if finance_form.is_valid():
            finance = finance_form.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'error')
    else:
        finance_form = FinanceForm()
    return dashboard(request)


def buffet_price(request):
    if request.method == 'POST':
        buffet_form = BuffetForm(data=request.POST)
        if buffet_form.is_valid():
            obj, created = Buffet.objects.update_or_create(
                id=1, defaults={'adult_price': buffet_form.cleaned_data['adult_price'], 'kid_price': buffet_form.cleaned_data['kid_price']},)
            buffet_rate = buffet_form.save()
            return redirect('dashboard')
        else:
            messages.error(request, 'error')
    return dashboard(request)


def finance_calc(request):
    total_adults = Guests.objects.filter(status="3").aggregate(Sum('adults'))['adults__sum']
    total_kids = Guests.objects.aggregate(Sum('children'))['children__sum']

    guest_count = {"adult": total_adults, "kids": total_kids}

    buffet = Buffet.objects.get(id=1)
    adult_rate = buffet.adult_price
    kid_rate = buffet.kid_price
    total_buffet_price = (total_adults * adult_rate) + (total_kids * kid_rate)
    obj, created = Finance.objects.update_or_create(
                item='Buffet', defaults={'price': total_buffet_price})
    total_cost = Finance.objects.aggregate(Sum('price'))['price__sum']

    return_variable = [guest_count, total_cost]
    return return_variable




