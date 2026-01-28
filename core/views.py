from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Service, Order

def home(request):
    return render(request, 'core/home.html')

def service_list(request):
    services = Service.objects.all()
    categories = Service.CATEGORY_CHOICES
    return render(request, 'core/service_list.html', {'services': services, 'categories': categories})

@login_required
def order_create(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        requirements = request.POST.get('requirements')
        Order.objects.create(
            customer=request.user,
            service=service,
            requirements=requirements
        )
        messages.success(request, 'Order submitted successfully!')
        return redirect('dashboard')
    return render(request, 'core/order_create.html', {'service': service})

@login_required
def dashboard(request):
    # Simple dashboard showing user's orders
    if request.user.is_staff:
        orders = Order.objects.all().order_by('-created_at')
        return render(request, 'core/dashboard_admin.html', {'orders': orders})
    else:
        orders = Order.objects.filter(customer=request.user).order_by('-created_at')
        return render(request, 'core/dashboard_customer.html', {'orders': orders})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Ensure user is authorized (Customer owner or Admin)
    # is_staff check handles admins, order.customer handles owner
    if not request.user.is_staff and order.customer != request.user:
        return redirect('dashboard')
    
    # Get chat history
    chat_messages = order.messages.all().order_by('timestamp')
    
    return render(request, 'core/order_detail.html', {
        'order': order,
        'chat_messages': chat_messages
    })

def logout_view(request):
    logout(request)
    return redirect('home')

