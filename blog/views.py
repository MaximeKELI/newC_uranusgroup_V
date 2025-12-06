"""
Vues pour le blog/CMS
"""
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Article, Category


def article_list(request):
    """
    Liste des articles de blog
    """
    category_slug = request.GET.get('category')
    search = request.GET.get('search', '')
    
    articles = Article.objects.filter(status='published')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = articles.filter(category=category)
    
    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(excerpt__icontains=search) |
            Q(content__icontains=search)
        )
    
    categories = Category.objects.all()
    featured_articles = Article.objects.filter(status='published', featured=True).order_by('-published_at')[:3]
    
    context = {
        'articles': articles,
        'categories': categories,
        'featured_articles': featured_articles,
        'current_category': category_slug,
        'search': search,
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    """
    Détail d'un article
    """
    article = get_object_or_404(Article, slug=slug, status='published')
    
    # Incrémenter le compteur de vues
    article.views_count += 1
    article.save(update_fields=['views_count'])
    
    related_articles = Article.objects.filter(
        category=article.category,
        status='published'
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'blog/article_detail.html', context)
