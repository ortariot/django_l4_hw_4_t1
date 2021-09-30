from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    article_query = Article.objects.all()
    print(article_query.first().scopes)
    context = {'object_list': article_query}
    

    # print(article_query[0].scopes.tag.name)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
