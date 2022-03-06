from choiceQuestions import choiceQuestion

def start():
    First = choiceQuestion()
    First.setText("2 x 9")
    First.addChoice("10", False)
    First.addChoice("18", True)
    First.addChoice("30", False)
    First.addChoice("19", False)

    Second = choiceQuestion()
    Second.setText("5 x 10")
    Second.addChoice("500", False)
    Second.addChoice("5", False)
    Second.addChoice("50", True)
    Second.addChoice("25", False)

    Third = choiceQuestion()
    Third.setText("3 x 4")
    Third.addChoice("12", True)
    Third.addChoice("18", False)
    Third.addChoice("15", False)
    Third.addChoice("8", False)

    Fourth = choiceQuestion()
    Fourth.setText("9 x 9")
    Fourth.addChoice("99", False)
    Fourth.addChoice("118", False)
    Fourth.addChoice("89", False)
    Fourth.addChoice("81", True)

    Fifth = choiceQuestion()
    Fifth.setText("50 x 50")
    Fifth.addChoice("250", False)
    Fifth.addChoice("2500", True)
    Fifth.addChoice("1250", False)
    Fifth.addChoice("500", False)

    presentQuestion(First)
    presentQuestion(Second)
    presentQuestion(Third)
    presentQuestion(Fourth)
    presentQuestion(Fifth)

def presentQuestion(x):
    x.display()
    responce = input("Your answer: ")
    print(x.checking(responce))

start()