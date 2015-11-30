from django.shortcuts import render, get_object_or_404
from .models import Review

def review_list(request):
    reviews = Review.objects.filter(rate__gte=5).order_by('created_date')
    return render(request, 'review/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
        review = get_object_or_404(Review, pk=pk)
        return render(request, 'review/review_detail.html', {'review': review})