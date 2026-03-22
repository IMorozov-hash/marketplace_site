from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy

def product_home(request):
    products = Product.objects.all()
    return render(request,'products/product-home.html',{'products': products})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = ('product')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/create.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product-delete.html'
    success_url = reverse_lazy('product-home')

def create(request):
    error = None
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-home')
        else:
            error = 'Form is not valid'
    else:
        form = ProductForm()
    return render(request, 'products/create.html', {'form': form, 'error': error})