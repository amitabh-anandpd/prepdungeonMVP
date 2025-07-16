from django.db import models
import json
    
class Waitlist(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    raw_score = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def set_score(self, score_dict: dict):
        self.raw_score = json.dumps(score_dict, separators=(",", ":"))
        self.save(update_fields=["raw_score"])

    def get_score(self):
        if self.raw_score:
            try:
                return json.loads(self.raw_score)
            except json.JSONDecodeError:
                pass
        return None

    def __str__(self):
        return f"{self.name} <{self.email}>"

class Question(models.Model):
    question = models.CharField(max_length=512, null=False)
    topic = models.CharField(max_length=128, null=False, default="Misc")
    subject = models.CharField(max_length=128, null=False, default="Misc")
    TYPE_CHOICES = [
        ('mcq', 'MCQ'),
        ('conceptual', 'Conceptual'),
        ('speed', 'Speed'),
    ]
    q_type = models.CharField(choices=TYPE_CHOICES, max_length=16, null=False)
    option1 = models.CharField(max_length=256, null=True, blank=True)
    option2 = models.CharField(max_length=256, null=True, blank=True)
    option3 = models.CharField(max_length=256, null=True, blank=True)
    option4 = models.CharField(max_length=256, null=True, blank=True)
    answer = models.CharField(max_length=1024, null=True, blank=True)
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    level = models.CharField(choices=LEVEL_CHOICES, max_length=16, null=False)
    
    def __str__(self):
        return self.question
    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "topic": self.topic,
            "subject": self.subject,
            "q_type": self.q_type,
            "option1": self.option1,
            "option2": self.option2,
            "option3": self.option3,
            "option4": self.option4,
            "answer": self.answer,
            "level": self.level,
            }

class ContactUsEmail(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('support', 'Support Request'),
        ('feedback', 'Feedback'),
        ('partnership', 'Partnership Opportunity'),
        ('bug', 'Bug Report'),
        ('feature', 'Feature Request'),
    ]
    email = models.EmailField(null=False)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=32, null=False)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    
