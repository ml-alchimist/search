from .file import dir_info, load_data
from .search import Search



def filterTheDict(dictObj, callback):
    """ Filter the dict """ 
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict

def run(line, data):
    """ main function, run process for inputed data """
    result = dict()
    for filename in data:
        init, end = Search().score(input_sentence = line, input_content = data[filename])
        if end == 0:
            result[filename] = 100
        else:
            result[filename] = ((init-end)/init)*100
            
    # keep only key with value (score) > 0     
    filtred = dict()
    for (key, value) in result.items():
        # Check if key is even then add pair to new dictionary
        if value > 0:
            filtred[key] = value
    # get top 10 values
    data = sorted(filtred.items(), key=lambda x: x[1], reverse=True)[0:10]
    if len(data) > 0:
        return data
    else: 
        return 'No result sorry, try again with another world!' 

