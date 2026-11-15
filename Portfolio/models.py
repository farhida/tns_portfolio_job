from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    full_name = models.CharField(max_length=120, default="Your Name")
    headline = models.CharField(max_length=180, default="Web Developer")
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume_file = models.FileField(upload_to="resume/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portfolio profile"
        verbose_name_plural = "Portfolio profile"

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=80, blank=True, help_text="Example: Frontend, Backend, Tools")
    proficiency = models.PositiveSmallIntegerField(default=75, help_text="Enter a value from 0 to 100.")
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=180)
    degree = models.CharField(max_length=180)
    field_of_study = models.CharField(max_length=180, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.degree} — {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=180)
    role = models.CharField(max_length=180)
    location = models.CharField(max_length=120, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.role} — {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=240, blank=True, help_text="Separate technologies with commas.")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    live_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or "project"
            candidate, number = base, 2
            while Project.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{number}"
                number += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} — {self.name}"
