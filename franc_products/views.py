import itertools

from django.shortcuts import render
from django.views.generic import ListView

from franc_order.forms import UserNewOrderForm
from .models import Product ,ProductGallery
from django.http import Http404
from franc_products_category.models import ProductCategory
from franc_tag.models import tag
class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6
    def get_queryset(self):
        return Product.object.get_active_product()
class ProductsListByCategory(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = ProductCategory.objects.filter(name__exact=category_name).first()
        if category is None:
            raise Http404('صحفه مورد نظر یافت نشد')
        return Product.object.get_prodcut_by_category(category_name)

def my_grouper(n,iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))
def product_detail(request,*args,**kwargs):
    select_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id':select_product_id})
    product: Product= Product.object.get_by_id(select_product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    product.visit_count += 1
    product.save()
    related_products = Product.object.get_queryset().filter(categories__product=product).distinct()
    grouped_related_products = my_grouper(3,related_products)
    galleries = ProductGallery.objects.filter(product_id=select_product_id)
    grouped_galleries = my_grouper(3 ,galleries)
    content = {
        'product': product,
        'galleries':grouped_galleries,
        'related_products':grouped_related_products,
        'new_order_form':new_order_form
        }
    return render(request, "products/product_detail.html", content)

class SearchProductView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6
    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.object.search(query)

        return Product.object.get_active_product()

def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context ={
        'categories':categories
    }
    return render(request,'products/products_categories_partial.html',context)