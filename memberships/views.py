from django.shortcuts import render, redirect
from .models import Membership
from django.contrib.auth.decorators import login_required
from .forms import MembershipForm  # Create this form in the next step


def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'memberships/membership_list.html', {'memberships': memberships})

def membership_create(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            membership = form.save(commit=False)
            membership.user = request.user  # Associate with logged-in user
            membership.save()
            return redirect('membership_list')
    else:
        form = MembershipForm()
    return render(request, 'memberships/membership_form.html', {'form': form})

def membership_update(request, pk):
    membership = Membership.objects.get(pk=pk)
    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect('membership_list')
    else:
        form = MembershipForm(instance=membership)
    return render(request, 'memberships/membership_form.html', {'form': form})

def membership_delete(request, pk):
    membership = Membership.objects.get(pk=pk)
    membership.delete()
    return redirect('membership_list')