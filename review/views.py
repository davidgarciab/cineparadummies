from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import PostForm

def review_list(request):
    reviews = Review.objects.filter(rate__gte=5).order_by('created_date')
    return render(request, 'review/review_list.html', {'reviews':reviews})

def review_detail(request, pk):
        review = get_object_or_404(Review, pk=pk)
        return render(request, 'review/review_detail.html', {'review': review})
    
def review_new(request):
    form = PostForm()
    return render(request, 'review/review_edit.html', {'form': form})

def review_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review.views.review_detail', pk=review.pk)
    else:
        form = PostForm()
    return render(request, 'review/review_edit.html', {'form': form})

def review_edit(request, pk):
        review = get_object_or_404(Review, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.save()
                return redirect('review.views.review_detail', pk=review.pk)
        else:
            form = PostForm(instance=review)
        return render(request, 'review/review_edit.html', {'form': form})
