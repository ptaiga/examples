from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.contrib.auth.models import User

from .models import Article
from .functions import get_followers, send_alert

def index(request):
    subscribe_list = request.user.subscriber.subscribe_list.split(',')
    if (subscribe_list == ['']): subscribe_list = []
    subscriptions = User.objects.filter(id__in = subscribe_list)
    post_list = Article.objects.filter(user__in=subscriptions)\
                                .order_by('-pub_date')
    subscriptions_name = ', '.join([user.username for user in subscriptions])
    followers_list = get_followers(request.user.id)
    readed_articles = request.user.subscriber.readed_articles.split(',')
    if (readed_articles == ['']): readed_articles = []
    readed_articles = [int(elem) for elem in readed_articles]
    context = {
        'post_list': post_list,
        'user': request.user,
        'followers_list': followers_list,
        'subscriptions': subscriptions_name,
        'readed_articles': readed_articles
    }
    return render(request, 'main/index.html', context)

def post(request, post_id):
    article = get_object_or_404(Article, pk=post_id)
    readed_articles = request.user.subscriber.readed_articles.split(',')
    if (readed_articles == ['']): readed_articles = []
    readed_articles = [int(elem) for elem in readed_articles]
    context = {
        'article': article,
        'readed_articles': readed_articles
    }
    return render(request, 'main/post.html', context)

def new_post(request):
    return render(request, 'main/new_post.html', {})

def add_post(request):
    if (request.method == 'POST'):
        a = Article(\
            user=request.user,\
            header=request.POST['header'],\
            content=request.POST['content'],\
            pub_date=timezone.now())
        a.save()
        send_alert(a)
        return HttpResponseRedirect(reverse('main:index', args=()))
    else:
        return HttpResponse('Something went wrong')

def post_mark(request, post_id, action):
    subscriber = request.user.subscriber
    readed_articles = request.user.subscriber.readed_articles.split(',')
    if (readed_articles == ['']): readed_articles = []
    readed_articles = [int(elem) for elem in readed_articles]
    if (action == 'read'):
        readed_articles.append(int(post_id))
    if (action == 'unread'):
        readed_articles.remove(int(post_id))
    readed_articles = [str(a) for a in readed_articles]
    subscriber.readed_articles = ','.join(readed_articles)
    subscriber.save()
    return HttpResponseRedirect(reverse('main:index', args=()))

def subscriptions(request):
    subscribe_list = request.user.subscriber.subscribe_list.split(',')
    if (subscribe_list == ['']): subscribe_list = []
    subscriptions = User.objects.filter(id__in = subscribe_list)
    users = User.objects.all().exclude(id__in = subscribe_list)
    context = {
        'users': users,
        'subscriptions': subscriptions,
        'user': request.user,
    }
    return render(request, 'main/subscriptions.html', context)

def subscribe(request):
    if (request.method == 'POST'):
        subscriber = request.user.subscriber
        former_subscriptions = subscriber.subscribe_list.split(',')
        if (former_subscriptions == ['']): former_subscriptions = []
        subscribe = []
        keys = request.POST
        for key in keys:
            if (key[0:4] == 'user'):
                subscribe.append(keys[key])
                if (keys[key] in former_subscriptions):
                    former_subscriptions.remove(keys[key])
        subscriber.subscribe_list = ','.join(subscribe)

        articles_for_mark_unread = []
        for subscription in former_subscriptions:
            user = User.objects.get(id=subscription)
            articles = Article.objects.filter(user=user)
            for a in articles:
                articles_for_mark_unread.append(int(a.id))

        readed_articles = request.user.subscriber.readed_articles.split(',')
        if (readed_articles == ['']): readed_articles = []
        readed_articles = [int(elem) for elem in readed_articles]

        for article_id in articles_for_mark_unread:
            if (article_id in readed_articles):
                readed_articles.remove(article_id)
        readed_articles = [str(elem) for elem in readed_articles]
        subscriber.readed_articles = ','.join(readed_articles)

        subscriber.save()
        return HttpResponseRedirect(reverse('main:index', args=()))
    else:
        return HttpResponse('Something went wrong')


def users(request):
    user_list = User.objects.all()
    return render(request, 'main/users.html', {'user_list': user_list})
    #output = ', '.join([u.username + ': ' + str(u.pk) for u in user_list])
    #return HttpResponse(output)

def send_mail(request):
    subject = 'Test email'
    body = 'This is the test email.'
    from_email = 'info@ti-tech.ru'
    to = 'ptaiga@gmail.com'
    with mail.get_connection() as connection:
        mail.EmailMessage(subject, body, from_email, [to],
                          connection=connection).send()
    return HttpResponse('Sent!')