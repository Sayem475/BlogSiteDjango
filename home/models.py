from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    msg = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(auto_now_add=True, blank= True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email

class design(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    texts = models.TextField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    sno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

class htmlchapters(models.Model):
    sno = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name

class htmldescription(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    chapters = models.ForeignKey(htmlchapters, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class csschapters(models.Model):
    sno = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name

class cssdescription(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    chapters = models.ForeignKey(csschapters, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class jschapters(models.Model):
    sno = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name

class jsdescription(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    chapters = models.ForeignKey(jschapters, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class pychapters(models.Model):
    sno = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name

class pydescription(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    chapters = models.ForeignKey(pychapters, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class djchapters(models.Model):
    sno = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chapter_name

class djdescription(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    chapters = models.ForeignKey(djchapters, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title