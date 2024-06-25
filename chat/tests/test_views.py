from django.test import TestCase, Client

class ChatViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_room_view(self):
        response = self.client.get('/chat/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'room_selection.html')
