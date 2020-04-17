import re
class Search:
    def __init__(self, sentence=None, content=None):
        self.content = content
        self.sentence = sentence
    
    def clean_world(self, world):
        """Remove special char, or any other clean process """
        result = re.sub(r"[^a-zA-Z0-9]+", ' ', world)
        return result
    
    def lower_world(self, world):
        """Convert world to lower"""
        return world.lower()
    
    def toSet(self, data):
       """ Convert sentence to query a (python set format) """
       try:
           clean_sentence = self.clean_world(data)
           lower_sentence = self.lower_world(clean_sentence)
           setContent = set(lower_sentence.split())
           return setContent
       except Exception as e:
           print('Something went wrong with query construction!')
    
    def compare(self, content, sentence):
        """ Compare two set and return find elements """
        try:
            result = sentence & content
            return result
        except Exception as e:
            print('Something went wrong with comparison:'+str(e))
        
    def score(self, input_sentence, input_content):
        """ Complete comparison and return a simple score """
        try:
            # init variables
            sentence = input_sentence
            content = input_content
            # generate sets
            sentence_set = self.toSet(sentence)
            # initial lenght of sentence
            init_len = len(sentence_set) 
            
            for line in content.splitlines():
                if len(sentence_set) > 0:
                    content_set = self.toSet(line)
                    rs = self.compare(content_set, sentence_set)
                    # if find result remove from initial query
                    if len(rs) > 0:
                        for el in rs:
                           sentence_set.remove(el) 
            
            end_len = len(sentence_set)
            return init_len, end_len
        except Exception as e:
            print('Something went wrong with scoring:'+str(e))
        
       
       