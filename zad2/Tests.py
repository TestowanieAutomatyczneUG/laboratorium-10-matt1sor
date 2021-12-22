import unittest
from note_zad1 import Note
from unittest.mock import *
from note_storage import note_storage
from note_service import NoteService



class NoteServiceTest(unittest.TestCase):

    @patch.object(note_storage, 'add')
    def test_note_service_add(self, mock_method):
        noteService = NoteService()
        note = Note("note", 3.21)
        mock_method.return_value = True
        self.assertEqual(noteService.add(note), True)

    @patch.object(note_storage, 'getAllNotesOf')
    def test_averageOf_many_notes(self, mock_method):
        noteService =NoteService()
        mock_method.return_value = [Note("note", 3.0), Note("note", 5.0), Note("note", 2.0), Note("note", 2.0)]
        self.assertEqual(noteService.averageOf("note"), 3.0)

    @patch.object(note_storage, 'getAllNotesOf')
    def test_averageOf_one_note(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = [Note("note", 3.0)]
        self.assertEqual(noteService.averageOf("note"), 3.0)

    @patch.object(note_storage, 'getAllNotesOf')
    def test_averageOf_no_notes(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = []
        self.assertEqual(noteService.averageOf("note"), 0.0)

    @patch.object(note_storage, "clear")
    def test_clear(self, mock_method):
        noteService = NoteService()
        mock_method.return_value = None
        self.assertIsNone(noteService.clear())