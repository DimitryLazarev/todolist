from django.test import TestCase

from todolistapp.models import ToDoList


class NoteAdderTest(TestCase):
    def test_adder(self):
        result = self.client.get('/note-adder/')
        note = ToDoList.objects.get(position=1)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(note.position, 1)


class NoteUpdaterTest(TestCase):
    def test_updater(self):
        self.client.get('/note-adder/')
        note = ToDoList.objects.get(position=1)
        self.assertEqual(note.text, '')
        self.client.post('/note-updater/1', {'note': 'qwerty'})
        note = ToDoList.objects.get(position=1)
        self.assertEqual(note.text, 'qwerty')


class NoteDeleterTest(TestCase):
    def test_deleter(self):
        self.client.get('/note-adder/')
        self.client.post('/note-updater/1', {'note': 'qwerty'})
        note = ToDoList.objects.get(position=1)
        self.assertEqual(note.text, 'qwerty')
        self.client.get('/note-deleter/1')
        notes = ToDoList.objects.filter(position=1)
        self.assertQuerysetEqual(notes, [])
