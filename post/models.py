from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=50)
	content =models.TextField(max_length=1000)
	created_at =models.DateTimeField(default=timezone.now)
	image =models.ImageField(upload_to='post-img/')

	class Meta:
		verbose_name=("post")
		verbose_name_plural=("post")

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse("post_detail",kwargs={"pk":self.pk})

	