from note_storage import note_storage


class NoteService:
    def __init__(self):
        self.noteStorage = note_storage()

    def add(self, note):
        return self.noteStorage.add(note)

    def averageOf(self, name):
        allNotes = self.noteStorage.getAllNotesOf(name)
        noteSum = 0
        for note in allNotes:
            noteSum += note.note
        numOfNotes = len(allNotes)
        if numOfNotes == 0:
            return 0
        return noteSum / numOfNotes

    def clear(self):
        return self.noteStorage.clear()


