"""
URL configuration for prepdungeon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from .views import index, features, about, contact, faq
from .views import clear_notifications, clear_question_ids, join_waitlist
from .views import testMCQ, checkMCQ, testSpeed, checkSpeed, testConceptual, checkConceptual

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('features/', features, name="features"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('faq/', faq, name="faq"),
    path('test-mcq/', testMCQ, name='test-mcq'),
    path('test-speed/', testSpeed, name='test-speed'),
    path('test-conceptual/', testConceptual, name='test-conceptual'),
    path('clear-notification/', clear_notifications, name="clear_notifications"),
    path('clear-question-ids/', clear_question_ids, name="clear_question_ids"),
    path('submit-mcq/', checkMCQ, name="checkMCQ"),
    path('submit-speed/', checkSpeed, name="checkSpeed"),
    path('submit-conceptual/', checkConceptual, name="checkConceptual"),
    path('join-waitlist/', join_waitlist, name="join_waitlist"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
