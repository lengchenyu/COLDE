from django.shortcuts import render
from .models import Article, Tag, Classification
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.syndication.views import Feed 
# Create your views here.
def home(request):
	articles = Article.objects.all()
	date_list = Article.date_list.get_article_onDate()
	paginator = Paginator(articles,2)
	page_num = request.GET.get('page')
	try:
	    articles = paginator.page(page_num)
	except PageNotAnInteger:
	    articles = paginator.page(1)
	except EmptyPage:
	    articles = paginator.page(paginator.num_pages)

	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list()    
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'home.html', locals())

def detail(request, year, month, day, id):
	try:
		article = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404

	article.count += 1
	article.save()
	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list()
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'article.html', locals())

def archive_month(request, year, month):
	articles = Article.objects.filter(publish_time__year=year).filter(publish_time__month=month)
	paginator = Paginator(articles,3)
	page_num = request.GET.get('page')
	try:
	    articles = paginator.page(page_num)
	except PageNotAnInteger:
	    articles = paginator.page(1)
	except EmptyPage:
	    articles = paginator.page(paginator.num_pages)

	date_list = Article.date_list.get_article_onDate()    
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list()     
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'home.html', locals())

def archive(request):
	archives = Article.date_list.get_article_onDate()
	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'archives.html', locals())

def about(request):
	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'about.html', locals())

def message(request):
	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()
	return render(request, 'message.html', locals())

def tag(request, tag):
	tem = Tag.objects.get(name=tag)
	articles = tem.article_set.all()
	paginator = Paginator(articles,3)
	page_num = request.GET.get('page')
	try:
	     articles = paginator.page(page_num)
	except PageNotAnInteger:
	     articles = paginator.page(1)
	except EmptyPage:
	     articles = paginator.page(paginator.num_pages)

	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()

	return render(request, 'home.html', locals())

def category(request, category):
	tem = Classification.objects.get(name=category)
	articles = tem.article_set.all()
	paginator = Paginator(articles,3)
	page_num = request.GET.get('page')
	try:
	     articles = paginator.page(page_num)
	except PageNotAnInteger:
	     articles = paginator.page(1)
	except EmptyPage:
	     articles = paginator.page(paginator.num_pages)

	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()

	return render(request, 'home.html', locals())

def search(request):
	date_list = Article.date_list.get_article_onDate()
	tag_list = Tag.tag_list.get_tag_list()
	category_list = Classification.classification_list.get_classification_list() 
	hot_list = Article.date_list.get_hot_article()
	s = request.GET['s']
	articles = Article.objects.filter(content__icontains = s)
	if len(articles) == 0:
		error = True

	return render(request, 'home.html', locals())

class RSSFeed(Feed):
	title = "CLODE"
	link = "/rss/"
	description = "Blog of CLODE"

	def items(self):
		return Article.objects.order_by('-publish_time')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.content


	def item_pudate(self, item):
		return item.publish_time



