from django.shortcuts import render, redirect
from .forms import ProductForm, ProductListForm
from .models import Products, ProductList
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def order_records(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(product_name__icontains=q))
        paged_post = Products.objects.filter(multiple_q)
    else:
        products = Products.objects.all().order_by('-id')
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    context = {
        'products':paged_post,
    }
    return render(request, 'app/order_records.html', context)

@login_required
def orderform(request):
    form = ProductForm(request.POST)
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.total_price = instance.unit_price * instance.quantity
            instance.user = request.user
            instance.save()
            messages.success(request, 'Order successful')
            return redirect('staff_dashboard-page')
        else:
            form = ProductForm()
    else:
        form = ProductForm()
    context = {
        'form':form,
    }
    return render(request, 'app/orderform.html', context)

@login_required
def add_new_product(request):
    form = ProductListForm(request.POST)
    if request.method=='POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a new product.')
            return redirect('admin_dashboard-page')
        else:
            form = ProductListForm()
    else:
        form = ProductListForm()
    context = {
        'form':form,
    }
    return render(request, 'app/add_new_product.html', context)

@login_required
def warehouse_stock(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(product_name__icontains=q))
        paged_post = Products.objects.filter(multiple_q)
    else:
        product_list = ProductList.objects.all().order_by('-id')
        paginator = Paginator(product_list, 7)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    context = {
        'product_list':paged_post,
    }
    return render(request, 'app/warehouse_stocks.html', context)

@login_required
def staffs(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(username__icontains=q) |Q(last_name__icontains=q) |Q(first_name__icontains=q) |Q(email__icontains=q))
        paged_post = User.objects.filter(multiple_q)
    else:
        user = User.objects.all()
        paginator = Paginator(user, 6)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    context = {
        'user':paged_post,
    }
    return render(request, 'app/staffs.html', context)

@login_required
def stocks_pricelist(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(product_name__icontains=q))
        paged_post = ProductList.objects.filter(multiple_q)
    else:
        product_list = ProductList.objects.all().order_by('-id')
        paginator = Paginator(product_list, 10)
        page = request.GET.get('page')
        paged_post = paginator.get_page(page)
    context = {
        'product_list':paged_post,
    }
    return render(request, 'app/stocks_pricelist.html', context)

@login_required
def admin_dashboard(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'app/admin_dashboard.html', context)

@login_required
def staff_dashboard(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'app/staff_dashboard.html', context)



    
