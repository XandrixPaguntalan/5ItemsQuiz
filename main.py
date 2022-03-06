class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def setText(self, question):
        self._text =question

    def setAnswer(self, correctanswer):
        self._answer = correctanswer

    def checking(self, input):
        return input == self._answer

    def display(self):
        print(self._text)