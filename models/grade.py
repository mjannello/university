class Grade:
    def __init__(self, subject, mark, approval_date, file, book):
        self.subject = subject
        self.mark = mark
        self.approval_date = approval_date
        self.file = file
        self.book = book


class GradesReport:
    def __init__(self):
        self.grades = []
