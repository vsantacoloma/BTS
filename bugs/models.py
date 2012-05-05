from django.db import models

class Application(models.Model):
  name = models.CharField(max_length=30, unique=True)
  
  def __unicode__(self):
    return self.name

class Bug(models.Model):
  name = models.CharField(max_length=50)
  STATUS_CHOICES = (
    ('U', 'Unconfirmed'),
    ('A', 'Assigned'),
    ('R', 'Resolved'),
    ('D', 'Duplicate'),
    ('C', 'Closed')
  )
  status = models.CharField(max_length=2, choices=STATUS_CHOICES)
  priority = models.PositiveIntegerField()
  date_reported = models.DateTimeField('date reported')
  date_changed = models.DateTimeField('date changed')
  replication = models.TextField(max_length=200)
  visits = models.IntegerField()
  bug_origin = models.ForeignKey('Bug')
  
  def __unicode__(self):
    return self.name

class Component(models.Model):
  name = models.CharField(max_length=30, unique=True)
  bugs = models.ManyToManyField(Bug)
  application = models.ForeignKey(Application)
  
  def __unicode__(self):
    return self.name
    
class Comment(models.Model):
  content = models.TextField()
  bug = models.ForeignKey(Bug)
  
  def __unicode__(self):
    return self.content