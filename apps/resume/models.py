from django.db import models


class ResumeItem(models.Model):
    """
    A single resume item, representing a job and title held over a given period
    of time.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=127)
    company = models.CharField(max_length=127)
    phones = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    start_date = models.DateField()
    # Null end date indicates position is currently held
    end_date = models.DateField(null=True, blank=True)
    project_title = models.CharField(max_length=100, null=True)
    project_description = models.CharField(max_length=500,null=True)
    hobbies = models.CharField(max_length=50,null=True)
    description = models.TextField(max_length=2047, blank=True)
    address = models.TextField(max_length=2047, blank=True)
    image = models.ImageField(upload_to='images/' ,null= True, blank=True)

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.user.username,
                                          self.title,
                                          self.company,
                                          self.phones,
                                          self.email,
                                          self.hobbies,
                                          self.project_description,
                                          self.project_title,
                                          self.address,
                                          self.image,
                                          self.start_date.isoformat())
