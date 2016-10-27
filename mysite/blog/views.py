from django.shortcuts import render, get_object_or_404, redirect
from . models import Post, Comment, Shop, Visit
from django.utils import timezone
from django.contrib.staticfiles import finders
from . forms import PostForm, CommentForm, ShopForm, VisitForm
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'blog/post_detail.html', {'post' : post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
		return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk = pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm(instance = post)
	return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts' : posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.publish()
	return redirect('post_detail', pk = pk)

@login_required
def post_remove(request, pk):
	post = get_object_or_404(Post, pk = pk)
	post.delete()
	return redirect('post_list')

def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk = pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_post.html', {'form' : form})

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk = pk)
	post_pk = comment.post.pk
	comment.delete()
	return redirect('post_detail', pk = post_pk)

@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk = pk)
	comment.approve()
	return redirect('post_detail', pk = comment.post.pk)


################################################################
def shop_new(request):
	if request.method == "POST":
		form = ShopForm(request.POST, request.FILES)
		if form.is_valid():
			#img = request.FILES.get('banner_image')

			shop = form.save()
			#shop.save()
			return redirect('shop_list')
	else:
		form = ShopForm()
		return render(request, 'lp/shop_edit.html', {'form' : form})

def shop_show(request, pk):
	shop = get_object_or_404(Shop, pk = pk)
	if request.method == "POST":
		visit_pk = request.POST.get('visit_pk')
		visit = Visit.objects.get(pk = visit_pk)
		mood = request.POST.get('mood')
		visit.mood = mood
		visit.comment = request.POST.get('comment')
		if request.POST.get('result') == "on":
			visit.result = "Buy"
		else:
			visit.result = "Didn't buy"
		visit.time_escape = timezone.now()###########WRONG
		visit.save()
		return redirect('visit_edit', pk = visit.pk)
	else:
		visit = remember_visit(request)
	return render(request, 'lp/shop_show.html', {'shop' : shop, 'visit' : visit})

def shop_edit(request, pk):
	shop = get_object_or_404(Shop, pk = pk)
	if request.method == "POST":
		form = ShopForm(request.POST, request.FILES, instance = shop)
		if form.is_valid():
			shop = form.save()
			return redirect('shop_list')
	else:
		form = ShopForm(instance = shop)
		return render(request, 'lp/shop_edit.html', {'form' : form})

def get_weather_for(city, code):
	import requests
	try:
		r = requests.get(str.format('http://api.openweathermap.org/data/2.5/weather?q={0},{1}&APPID=5935d635f074bcc8ba1d127e1d5243c4', code, city))
		return r.json()['weather'][0]['description']
	except:
		return None

def get_season(datetime):
	month = datetime.month
	if month in range(3, 6):
		return "Spring"
	elif month in range(6, 10):
		return "Summer"
	elif month in range(10, 12):
		return "Automn"
	else:
		return "Winter"


celebrations = {
	"RU" : ['1/1', '2/1', '3/1', '4/1', '5/1', '6/1', '7/1', '8/1', '23/2', '1/5', '9/5', '12/6', '4/11', '31/12'],
	"US" : ['1/1', '2/1', '16/1', '20/1', '29/5', '4/7', '4/9', '9/10', '11/11', '23/11', '25/12'],
}

#####################################################
def remember_visit(request):
	from user_agents import parse
	user_agent_string = request.META['HTTP_USER_AGENT']
	user_agent = parse(user_agent_string)
	
	browser = user_agent.browser.family

	os = user_agent.os.family

	device = (lambda u_a: "Desktop" if user_agent.is_pc
									else "Smartphone")(user_agent)
	ip = (lambda meta:
		meta.get('HTTP_X_FORWSRDED_FOR')
		if meta.get('HTTP_X_FORWARDED_ROF')
		else meta.get('REMOTE_ADDR')) (request.META)

	if request.META.get('HTTP_ACCEPT_LANGUAGE'):
		language = request.META['HTTP_ACCEPT_LANGUAGE'].split(',')[0]

	#Country, City
	try:
		g = GeoIP2()
		country = g.country(ip)['country_name']
		country_code = g.country(ip)['country_code']
		city = g.city(ip)[city]

		weather = None
		if country and city:
			weather = get_weather_for(city, country_code)

		if celebrations.get('country_code'):
			is_selebration = str.format("{0}/{1}", dt.day, dt.month) in celebrations[country_code]
		else:
			is_selebration = False
	except:
		country = None
		city = None
		weather = None
		is_selebration = False

	dt = timezone.now()

	weekday = dt.strftime("%A")
	season = get_season(dt)

	visit = Visit.objects.create(os = os, browser = browser, device = device, language = language,
		ip = ip, country = country, city = city, weather = weather, season = season, 
		day_of_the_week = weekday, is_selebration = is_selebration)
	return visit

def visit_new(request):
	if request.method == "POST":
		form = VisitForm(request.POST)
		if form.is_valid():
			visit = form.save()
			return redirect('visit_list')
	else:
		form = VisitForm()
		return render(request, 'lp/visit_edit.html', {'form' : form})

def visit_list(request):
	visits = Visit.objects.all()
	return render(request, 'lp/visit_list.html', {'visits' : visits})

def visit_edit(request, pk):
	visit = get_object_or_404(Visit, pk = pk)
	if request.method == "POST":
		form = VisitForm(request.POST, instance = visit)
		if form.is_valid():
			visit = form.save(commit = False)
			visit.save()
			return redirect('visit_list')
	else:
		form = VisitForm(instance = visit)
	return render(request, 'lp/visit_edit.html', {'form' : form})

def visit_remove(request, pk):
	visit = get_object_or_404(Visit, pk = pk)
	visit.delete()
	return redirect('visit_list')

def shop_list(request):
	shops = Shop.objects.all()
	return render(request, 'lp/shop_list.html', {'shops' : shops})

def shop_remove(request, pk):
	shop = get_object_or_404(Shop, pk = pk)
	shop.delete()
	return redirect('shop_list')