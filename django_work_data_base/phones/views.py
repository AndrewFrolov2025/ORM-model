from django.shortcuts import render, get_object_or_404

from phones.models import Phone

def catalog_view(request):
    sort = request.GET.get('sort')

    phones = Phone.objects.all()

    if sort == 'name':
        phones = phones.order_by('name')
    elif sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')

    context = {
        'phones': phones,
        'current_sort': sort,
    }

    return render(request, 'phones/catalog.html', context)

def phone_detail_view(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    context = {
        'phone': phone,
    }

    return render(request, 'phones/phone_detail.html', context)
