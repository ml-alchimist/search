from cmd import Cmd
from .run import run

class Prompt(Cmd, object):
    data = ''       
    def default(self,  line):
        if len(line) > 0:
            print(run(line, self.data))
        else:
            print('query cannot be empty sorry !')
    
    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit