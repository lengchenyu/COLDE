#encoding:utf8
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class TagManager(models.Manager):
	def get_tag_list(self):
		tags = Tag.objects.all()
		tag_list = []

		for i in range(len(tags)):
			tag_list.append([])
			posts = tags[i].article_set.all()	
			name = tags[i].name
			tag_list[i].append(name)
			tag_list[i].append(len(posts))

		return tag_list


class Tag(models.Model):
	name = models.CharField(max_length=30)

	objects = models.Manager()
	tag_list = TagManager()

	def get_absolute_url(self):
		return reverse('tag',kwargs={'tag': self.name})

	def __unicode__(self):
		return self.name


class ClassificationManager(models.Manager):
	def get_classification_list(self):
		classifications = Classification.objects.all()
		classification_list = []

		for i in range(len(classifications)):
			classification_list.append([])
			posts = classifications[i].article_set.all()
			name = classifications[i].name	
			classification_list[i].append(name) 
			classification_list[i].append(len(posts))

		return classification_list


class Classification(models.Model):
	name = models.CharField(max_length=30)

	objects = models.Manager()
	classification_list = ClassificationManager()

	def get_absolute_url(self):
		return reverse('category', kwargs={'category': self.name})

	def __unicode__(self):
		return self.name




class ArticleManager(models.Manager):
	def get_article_onDate(self):
		post_date = Article.objects.dates('publish_time', 'month', order='DESC')
		date_list = []

		for i in range(len(post_date)):
			date_list.append([])
			curyear = post_date[i].year
			curmonth = post_date[i].month
			tempArticle = Article.objects.filter(publish_time__year=curyear, publish_time__month=curmonth)
			date_list[i].append(post_date[i])
			date_list[i].append(len(tempArticle))
			date_list[i].append(tempArticle)

		return date_list

	def get_hot_article(self):
		articles = Article.objects.order_by('-count')
		if len(articles) < 5:
			hot_list = articles[:len(articles)]
		else:
			hot_list = articles[:5]

		return hot_list


class Article(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	img = models.ImageField(upload_to='abstract_img')
	abstract = models.TextField()
	publish_time = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, blank=True)
	classification = models.ForeignKey(Classification)
	count = models.IntegerField(default=0)

	objects = models.Manager()
	date_list = ArticleManager()

	def get_absolute_url(self):
		return reverse('detail', kwargs={
			'year': self.publish_time.strftime('%Y'),
			'month': self.publish_time.strftime('%m'),
			'day': self.publish_time.strftime('%d'),
			'id': self.id
			})
	
	def get_tags(self):#返回一个文章对应的所有标签
	    tag = self.tags.all()
	    return tag
	def get_after_article(self):#返回当前文章的前一篇文章
	    temp = Article.objects.order_by('id')
	    cur = Article.objects.get(id=self.id)
	    count=0
	    for i in temp:
	        if i.id == cur.id:
	         	 index = count
	         	 break
	        else:
	           count=count+1
	    if index != 0:
	     return temp[index-1]

	def get_before_article(self):#返回当前文章的后一篇文章
	    temp = Article.objects.order_by('id')
	    max =  len(temp)-1
	    cur = Article.objects.get(id=self.id)
	    count=0
	    for i in temp:
	        if i.id == cur.id:
	         	 index = count
	           	 break
	        else:
	           count=count+1
	    if index != max:
	     return temp[index+1]


	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-publish_time']
