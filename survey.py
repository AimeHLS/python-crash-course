from items_test import AnonymousSurvery

# Define a question, and make a survey.
question = "\nWhat programming language did you learn first?"
language_survey = AnonymousSurvery(question)

# Show the question, and store responses to the question.
language_survey.show_question()
print("\nEnter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()