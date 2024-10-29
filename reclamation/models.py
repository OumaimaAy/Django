from django.db import models
from django.contrib.auth.models import User
from .utils import analyze_sentiment

class Reclamation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', 'Urgent'),
    ]

    CATEGORY_CHOICES = [
        ('Service', 'Service'),
        ('Product', 'Product'),
        ('Billing', 'Billing'),
        ('Technical', 'Technical'),
        ('Other', 'Other'),
    ]
    SENTIMENT_ORDER = {
        "Very Negative": 1,
        "Negative": 2,
        "Neutral": 3,
        "Positive": 4,
        "Very Positive": 5,
    }
    @property
    def sentiment_order(self):
        return self.SENTIMENT_ORDER.get(self.sentiment, 3)
    def save(self, *args, **kwargs):
        if not self.sentiment:
            self.sentiment = analyze_sentiment(self.description)
        super().save(*args, **kwargs)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    sentiment = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.ImageField(upload_to='reclamation_attachments/', blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.sentiment:
            self.sentiment = analyze_sentiment(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.status}) - {self.user.username}"

class Response(models.Model):
    reclamation = models.ForeignKey(Reclamation, on_delete=models.CASCADE, related_name="responses")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.user.username} on {self.created_at}"