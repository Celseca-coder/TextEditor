
# commands/text_commands.py
class AppendCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text
        self.prev_line_count = 0

    def execute(self):
        self.prev_line_count = len(self.editor.lines)
        self.editor.lines.append(self.text)
        self.editor.mark_modified()

    def undo(self):
        self.editor.lines.pop()
        if len(self.editor.lines) == self.prev_line_count - 1:
            self.editor.mark_unmodified()

    def is_undoable(self):
        return True