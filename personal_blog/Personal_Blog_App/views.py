from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from Personal_Blog_App.models import Article, Comment
from Personal_Blog_App.forms import ArticleForm, CommentForm
from functools import wraps
from dotenv import dotenv_values
import base64
import binascii
import re

def basic_auth_is_required(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            return HttpResponse(content='Unauthorized', status=401, headers={'WWW-Authenticate': 'Basic realm="Restricted Area"'})

        try:
            auth_decode = base64.b64decode(auth_header.split(' ')[1]).decode('utf-8')
            username, password = auth_decode.split(':')
        except (binascii.Error, ValueError):
            return HttpResponse('Invalid Authorization', status=400)

        config = dotenv_values('.env')
        if username != config.get('BASIC_AUTH_USERNAME') or password != config.get('BASIC_AUTH_PASSWORD'):
            return HttpResponseForbidden('Access Forbidden')

        request.authenticated_user = username
        return view(request, *args, **kwargs)

    return wrapper

@basic_auth_is_required
def adminpage(request):
    template = loader.get_template('adminpage.html')
    articles = list(Article.objects.all().values())
    if len(articles) == 0:
        articles = None

    return HttpResponse(template.render(request=request, context={'articles': articles, 'request': request}))

def main(request):
    template = loader.get_template('main.html')
    articles = list(Article.objects.all().values())
    if len(articles) == 0:
        articles = None

    return HttpResponse(template.render(request=request, context={'articles': articles}))

def article(request, articleid):
    try:
        articleobj = Article.objects.filter(id=articleid).values().first()
    except AttributeError:
        articleobj = None

    if articleobj is None:
        return HttpResponseRedirect('/notfound')

    template = loader.get_template('article.html')
    submitted = False # in sense of a comment

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            banned_words = ['fuck', 'bitch', 'nigg']
            passed = True
            for word in banned_words:
                if re.search(fr'(.*)({word})(.*)', form.data.get('content'), re.DOTALL | re.IGNORECASE) is not None:
                    passed = False
                    break

            if passed:
                post = form.save(commit=False)
                post.article = articleid
                post.save()
                return HttpResponseRedirect(f'/article/{articleid}?submitted=True')
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True

    comments = list(Comment.objects.filter(article=articleid).values())
    if len(comments) == 0:
        comments = None

    return HttpResponse(template.render(request=request, context={'article': articleobj,
                                                                  'form': form,
                                                                  'submitted': submitted,
                                                                  'comments': comments}))

def adminarticle(request, articleid):
    try:
        articleobj = Article.objects.filter(id=articleid).values().first()
    except AttributeError:
        articleobj = None

    if articleobj is None:
        return HttpResponseRedirect('/notfound')

    comments = list(Comment.objects.filter(article=articleid).values())
    if len(comments) == 0:
        comments = None

    template = loader.get_template('adminarticle.html')
    return HttpResponse(template.render(request=request, context={'article': articleobj, 'comments': comments}))

def post(request):
    template = loader.get_template('post.html')
    submitted = False

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/adminpage/post?submitted=True')
    else:
        form = ArticleForm()
        if 'submitted' in request.GET:
            submitted = True

    return HttpResponse(template.render(request=request, context={'form': form, 'submitted': submitted}))

def edit(request, articleid):
    try:
        articleobj = Article.objects.filter(id=articleid).values().first()
    except AttributeError:
        articleobj = None

    if articleobj is None:
        return HttpResponseRedirect('/notfound')

    template = loader.get_template('edit.html')
    submitted = False

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            articlequery = Article.objects.filter(id=articleid)[0]
            articlequery.title = form.data.get('title')
            articlequery.content = form.data.get('content')
            articlequery.save()
            return HttpResponseRedirect(f'/adminpage/{articleid}/edit?submitted=True')
    else:
        form = ArticleForm()
        if 'submitted' in request.GET:
            submitted = True

    return HttpResponse(template.render(request=request, context={'submitted': submitted, 'article': articleobj, 'form': form}))

def delete(request, articleid):
    try:
        articleobj = Article.objects.filter(id=articleid).values().first()
    except AttributeError:
        articleobj = None

    if articleobj is None:
        return HttpResponseRedirect('/notfound')

    template = loader.get_template('delete.html')

    articlequery = Article.objects.filter(id=articleid)[0]
    articlequery.delete()
    
    return HttpResponse(template.render(request=request, context={'article': articleobj}))

def deletecomment(request, articleid, commentid):
    try:
        commentquery = Comment.objects.filter(id=commentid)[0]
        commentquery.delete()
    except IndexError:
        return HttpResponseRedirect('/notfound')

    template = loader.get_template('deletecomment.html')
    return HttpResponse(template.render(request=request))