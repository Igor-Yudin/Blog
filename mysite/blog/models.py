from django.db import models
from django.utils import timezone
import os

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	content = models.TextField(default = "")


	#def __unicode__(self):
	#	return self.title

	#def get_absolute_url(self):
	#	return str.format("/blog/{0}/", self.id)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title

	def approved_comments(self):
		return self.comments.filter(approved_comment = True)

class Comment(models.Model):
	post = models.ForeignKey('blog.Post', related_name = 'comments')
	author = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

def get_image_path(instance, filename):
	return os.path.join('banners', str(instance.id), filename)

class Shop(models.Model):
	name = models.CharField(max_length = 200)
	motto = models.CharField(max_length = 200)
	advantages = models.TextField(default = "")
	# advantages_short = models.TextField(default = "")

	SUPERWHITE = 'SW'
	DARKSTYLE = 'DS'

	BASE_STYLES = 	{
		(SUPERWHITE, 'Super white'),
		(DARKSTYLE, 'Dark style'),
	}

	base_style = models.CharField(
		max_length = 10,
		choices = BASE_STYLES,
		default = SUPERWHITE,
		)

	banner_image = models.ImageField(
		upload_to = 'banners',
		null = True,
		blank = True
		)

	contact_phone = models.CharField(
		max_length = 20,
		default = "+7-904-776-30-57"
		)
	email = models.EmailField(default = "Igor_Yudin@inbox.ru")

# class ShopToShow(models.Model):
# 	name = models.CharField(max_length = 200)
# 	motto = models.CharField(max_length = 200)
# 	advantages = models.TextField(default = "")
# 	is_advantages_full = models.BooleanField(default = True)

class Visit(models.Model):
	# shop_advantages_full = models.BooleanField(default = None, null = True)
	# shop_advantages = models.TextField(default = "")

	WINDOWSXP = 1
	WINDOWSVISTA = 2
	WINDOWS7 = 3
	WINDOWS8 = 4
	WINDOWS10 = 5
	OSX = 6
	LINUX = 7
	SOLARIS = 8
	ANDROID = 9
	WINDOWSPHONE = 10
	IOS = 11
	BLACKBERRY = 12

	OS = [
		(WINDOWSXP, "Windows XP"),
		(WINDOWSVISTA, "Windows Vista"),
		(WINDOWS7, "Windows 7"),
		(WINDOWS8, "Windows 8"),
		(WINDOWS10, "Windows 10"),
		(OSX, "OS X"),
		(LINUX, "Linux"),
		(SOLARIS, "Solaris"),
		(ANDROID, "Android"),
		(WINDOWSPHONE, "Windows Phone"),
		(IOS, "iOS"),
		(BLACKBERRY, "Blackberry OS"),
	]

	os = models.CharField(max_length = 100,
		# choices = OS,
		blank = True,
		null = True
		)

	CHROME = 1
	FIREFOX = 2
	OPERA = 3
	SAFARI = 4
	IE = 5

	BROWSER = [
		(CHROME, "Chrome"),
		(FIREFOX, "Firefox"),
		(OPERA, "Opera"),
		(SAFARI, "Safari"),
		(IE, "Internet Explorer"),
	]

	browser = models.CharField(max_length = 100,
		# choices = BROWSER,
		blank = True,
		null = True)

	DESKTOP = 1
	PHONE = 2

	DEVICE = [
		(DESKTOP, "Desktop"),
		(PHONE, "Smartphone"),
	]

	device = models.CharField(max_length = 100,
		# choices = DEVICE,
		blank = True,
		null = True)

	time_enter = models.DateTimeField(default = timezone.now)

	time_escape = models.DateTimeField(blank = True, 
		null = True)

	language = models.CharField(max_length = 100,
		blank = True,
		default = "ru-ru")
	
	ip = models.CharField(max_length = 100,
		blank = True,
		null = True)
	
	country = models.CharField(max_length = 100, 
		blank = True,
		null = True)
	
	city = models.CharField(max_length = 100, 
		blank = True,
		null = True)
	
	SUNNY = 1
	CLOUDY = 2
	SNOW = 3
	RAIN = 4
	FAIR = 5
	WINDY = 6

	WEATHER = [
		(SUNNY, "Sunny"),
		(CLOUDY, "Cloudy"),
		(SNOW, "Snow"),
		(RAIN, "Rain"),
		(WINDY, "Windy"),
	]

	weather = models.CharField(max_length = 100,
		# choices = WEATHER,
		blank = True,
		null = True)

	SPRING = 1
	SUMMER = 2
	AUTOMN = 3
	WINTER = 4

	SEASON = [
		(SPRING, "Spring"),
		(SUMMER, "Summer"),
		(AUTOMN, "Automn"),
		(WINTER, "Winter"),
	]


	season = models.CharField(max_length = 100,
		# choices = SEASON,
		blank = True,
		null = True)
	
	is_selebration = models.BooleanField(default = False)

	MONDAY = 1
	TUESDAY = 2
	WEDNESDAY = 3
	THURSDAY = 4
	FRIDAY = 5
	SATURDAY = 6
	SUNDAY = 7

	WEEK = [
		(MONDAY, "Monday"),
		(TUESDAY, "Tuesday"),
		(WEDNESDAY, "Wednesday"),
		(THURSDAY, "Thursday"),
		(FRIDAY, "Friday"),
		(SATURDAY, "Saturday"),
		(SUNDAY, "Sunday"),
	]

	day_of_the_week = models.CharField(max_length = 100,
		# choices = WEEK,
		blank = True,
		null = True)

	FINE = 1
	GOOD = 2
	NORMAL = 3
	BAD = 4

	MOOD = [
		(FINE, "Fine"),
		(GOOD, "Good"),
		(NORMAL, "Normal"),
		(BAD, "Bad"),
	]

	mood = models.CharField(max_length = 100,
		# choices = MOOD,
		blank = True,
		null = True)

	comment = models.TextField(blank = True)

	BUY = 1
	NOT_BUY = 2

	RESULT = [
		(BUY, "Buy"),
		(NOT_BUY, "Didn't buy")
	]

	result = models.CharField(max_length = 100,
		# choices = RESULT,
		blank = True,
		null = True)