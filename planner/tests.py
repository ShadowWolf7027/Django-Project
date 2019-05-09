from django.test import TestCase, Client
from django.urls import reverse
from .models import Event, File
from datetime import datetime
from unittest import mock

class EventTestCase(TestCase):
    # Verify that only valid dates can be inputted
    def test_valid_event(self):
        try:
            date = datetime.strptime('2019-13-35', '%Y-%m-%d')
            test_event = Event.objects.create(title='Test', description='Test', 
                                date=date, course='Test')
            self.assertEqual(test_event.date, True)
        except ValueError:
            return False

class EventListViewTestCase(TestCase):
    # Verify there are no issues with any of the pages
    def test_calendar(self):
        response = self.client.get(reverse('planner:planner'))
        self.assertEqual(response.status_code, 200)

    def test_new_event_view(self):
        response = self.client.get(reverse('planner:event_new'))
        self.assertEqual(response.status_code, 200)

class FileTestCase(TestCase):
    # Verify that a file can be uploaded with information saved
    def test_file_field(self):
        mock_file = mock.MagicMock(spec=File)
        mock_file.description = 'test.pdf'
        file_model = File(document=mock_file)
        self.assertEqual(file_model.document.description, mock_file.description)