import os

def dir_info(path):
    try:
        # Test if directory exist
        if (os.path.isdir(path)):
            lst = os.listdir(path) 
            number_files = len(lst)
            return number_files
        else:
            print('directory not exist')
            raise SystemExit
    except Exception as e:
        print(e)

def load_data(path):
    try:
        data = dict()
        for filename in os.listdir(path):
            if filename.endswith('.txt'):
                with open(os.path.join(path, filename), 'r') as f: # open in readonly mode
                    data[filename] = f.read()
        return data    
    except Exception as e:
        print(e)
