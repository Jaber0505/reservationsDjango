from django.shortcuts import render, get_object_or_404

from catalogue.models.review import Review

def index(request):
    reviews = Review.objects.select_related('show', 'user')
    title = "Liste des critiques"
    return render(request, 'review/index.html', {
        'reviews': reviews,
        'title': title
    })

def show(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review/show.html', {
        'review': review,
        'title': "Critique"
    })
