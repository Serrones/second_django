from django.db import models

# Create your models here.

class User_Profile(models.Model):
    # Fields...
    def __str__ (self):
        return self.name

    name = models.CharField(max_length=100, verbose_name="Name")
    login = models.CharField(max_length=25, verbose_name="Login")
    password = models.CharField(max_length=20, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone number",
                            null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Birthday" , null=True,
                            default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection",
                            null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    years_seniority = models.IntegerField(verbose_name="Seniority",
                            default=0)
    date_created = models.DateField(verbose_name="Profile Creation Date",
                            auto_now_add=True)

class Supervisor(User_Profile):
    # Fields...
    def __str__ (self):
        return self.name
    # Duplicated common fields
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")

class Developer(User_Profile):
    # Fields...
    def __str__ (self):
        return self.name
    # Duplicated common fields
    gerente = models.ForeignKey(Supervisor, verbose_name="Supervisor")

class Project(models.Model):
    # Fields...
    def __str__ (self):
        return self.name
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=100, verbose_name="Client name")

class Task(models.Model):
    # Fields...
    def __str__ (self):
        return self.name
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time" ,
                            null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project" ,
                            null=True, default=None, blank=True)
    developers = models.ManyToManyField(Developer ,through="Dev_Work_Task")

class Dev_Work_Task(models.Model):
    developer = models.ForeignKey(Developer)
    task = models.ForeignKey(Task)
    time_elapsed_dev = models.IntegerField(verbose_name="Time elapsed",
                            null=True, default=None, blank=True)
