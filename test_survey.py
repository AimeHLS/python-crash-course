from items_test import AnonymousSurvery

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_multiple_responses():
    """Test that multiple responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    responses = ['English', 'Spanish', 'Mandarin','Kinyarwanda']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses


