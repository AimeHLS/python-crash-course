import pytest
from items_test import AnonymousSurvery

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    return language_survey


def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_multiple_responses(language_survey):
    """Test that multiple responses are stored properly."""

    responses = ['English', 'Spanish', 'Mandarin','Kinyarwanda']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses