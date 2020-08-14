import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_001_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        :return: boolean
        """
        time = timezone.now() + datetime.timedelta(days=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_002_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than 30 days.
        :return: boolean
        """
        time = timezone.now() - datetime.timedelta(days=30, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_003_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is within 30 days.
        :return: boolean
        """
        time = timezone.now() - datetime.timedelta(days=29, hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)