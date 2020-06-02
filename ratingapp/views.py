from django.shortcuts import render, get_object_or_404
from . models import Restaurant
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def rating(request):
    restaurants = Restaurant.objects.all().order_by('-rating')[:3]
    paginator = Paginator(restaurants, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'restaurants': restaurants,
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        # 'rating':rating,
    }
    return render(request, 'by_rating.html', context)

def index(request):
    restaurants = Restaurant.objects.order_by('-created')[:10]
    paginator = Paginator(restaurants, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'restaurants':restaurants,
        'queryset':paginated_queryset,
        'page_request_var':page_request_var,
        # 'rating':rating,
               }
    return render(request, 'index.html', context)

def detail(request):
    post_list = Restaurant.objects.all()
    context = { 'post_list': post_list}
    return render(request, 'details.html', context)

def post(request, id):
    post = get_object_or_404(Restaurant, id=id)
    return render(request, 'post-detail.html',post)

def search(request):
    queryset = Restaurant.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)

