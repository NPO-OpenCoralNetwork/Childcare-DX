from django.db import models
from django.conf import settings
from accounts.models import UserProfile

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='inquiries')
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Response(models.Model):
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, related_name='responses')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='responses')

    def __str__(self):
        return f"Response to {self.inquiry.title} by {self.user.username}"

class SavedResponse(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

class SavedInquiry(models.Model):
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('responder', 'inquiry')

class Report(models.Model):
    reporter = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reports_made')
    reported_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reports_received')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)