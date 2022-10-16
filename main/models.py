from django.db import models


class News(models.Model):
    img = models.ImageField(upload_to='main/images')
    title = models.CharField(max_length=100)
    txt = models.TextField()

    def __str__(self):
        return self.title

class ServiceGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Service(models.Model):
    img = models.ImageField(upload_to='main/images')

    name = models.CharField(max_length=100)
    group = models.ForeignKey(ServiceGroup, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name


class Doctor(models.Model):
    img = models.ImageField(upload_to='main/images')

    name = models.CharField(max_length=100)
    dw = models.ManyToManyField(Service)
    about = models.TextField()
    yw = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class About(models.Model):
    img = models.ImageField(upload_to='main/images')
    title = models.CharField('Ном', max_length=100)
    txt = models.TextField('Текст')
    bool = models.BooleanField('Тарафи рост', default=False)

    def __str__(self):
        return self.title


class Partner(models.Model):
    img = models.ImageField(upload_to='main/images')
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.city + ', ' + self.country


class Image(models.Model):
    img = models.ImageField(upload_to='main/images')

    def __str__(self):
        return str(self.img)