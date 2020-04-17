import os
import pytest
from src.search import Search

@pytest.fixture
def min_sentence_set():
    """ minimum query  """
    return {'hello', 'world'}

@pytest.fixture
def min_content_set():
    """ minimum content  """
    return {'hello', 'world', 'of', 'geek'}

@pytest.fixture
def valid_result():
    """ valid result / what the search find """
    return {'hello', 'world'}

@pytest.fixture
def valid_score():
    """ valid score """
    return 2,0

@pytest.fixture
def min_sentence():
    """ minimum query  """
    return 'hello world'

@pytest.fixture
def min_content():
    """ minimum content  """
    return 'hello world of geek'

class TestIsValid:
    def test_compare(self, min_sentence_set, min_content_set, valid_result):
        result = Search().compare(sentence=min_sentence_set, content=min_content_set)
        assert result == valid_result
    
    def test_score(self,min_content, min_sentence, valid_score):
        result = Search(sentence=min_sentence, content=min_content).score()
        assert result == valid_score