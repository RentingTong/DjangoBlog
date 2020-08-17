import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


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


class QuestionIndexViewTests(TestCase):
    def test_001_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_002_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the index page.
        """
        create_question(question_text="Past question.", days=-60)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_003_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on the index page.
        """
        create_question(question_text="Future question.", days=60)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_004_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions are displayed.
        """
        create_question(question_text="Past Question.", days=-60)
        create_question(question_text="Future Question.", days=60)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past Question.>']
        )

    def test_005_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-25)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 1.>', '<Question: Past question 2.>']
        )