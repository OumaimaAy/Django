from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('ST', 'Standard'),
        ('PR', 'Premium'),
        ('VIP', 'VIP'),
    ]

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    membership_type = models.CharField(
        max_length=50,
        choices=MEMBERSHIP_CHOICES  # Apply the choices here
    )
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_membership_type_display()}"

    

# class UserPreference(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     interests = models.CharField(max_length=255)  # E.g., "Art, History, Science"
#     preferred_visit_times = models.CharField(max_length=100)  # E.g., "Weekends, Evenings"

# class VisitHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     visit_date = models.DateField()
#     duration = models.DurationField()
#     exhibits_visited = models.TextField()  # Store exhibit IDs or names
#     rating = models.IntegerField(null=True, blank=True)  # Optional feedback rating
