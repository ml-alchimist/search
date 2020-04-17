import os
import pytest
from src.search import Search

@pytest.fixture
def min_content():
    """Represent minimal file content"""
    return ''' Hello world of geek
             this is a test content for our powreful search engine
            '''
            


@pytest.fixture
def special_char():
    """Represent wolrd with special char """
    return {'input':'hello!@',
            'output': 'hello '}

@pytest.fixture
def lower_world():
    """Convert world to lower"""
    return {'input':'HELLO',
            'output': 'hello'}


@pytest.fixture
def min_sentence():
    """Respresent a single wolrd """
    return 'hello WORLD of geek!!!!'

@pytest.fixture
def min_query():
    """Convert sentence to query """
    return {'hello', 'world', 'of', 'geek'}
    

class TestIsValid:
    """Test how code verifies whether a search query return valid result """
    def test_special_char(self, special_char):
        input = special_char['input']
        output = special_char['output']
        result =  Search().clean_world(input)
        assert result == output
    
    def test_lower_char(self, lower_world):
        input = lower_world['input']
        output = lower_world['output']
        result =  Search().lower_world(input)
        assert result == output
        
    def test_minimal(self, min_sentence, min_query):
        result = Search().toSet(min_sentence)
        assert min_query == result