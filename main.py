from src.file import dir_info, load_data
from src.search import Search   
from src.prompt import Prompt
from cmd import Cmd
from src.run import run
import sys, getopt

def main(argv):
   """ Read command line and look for mandatory args """ 
   inputcmd = ''
   inputpath = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["icmd=","ipath="])
   except getopt.GetoptError:
      print ('test.py -i <command> -o <inputpath>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('main.py -i <command> -o <inputpath>')
         sys.exit()
      elif opt in ("-i", "--icmd"):
         inputcmd = arg
      elif opt in ("-o", "--ipath"):
         inputpath = arg
         
   if inputcmd =='' or inputpath =='':
       print('Use -h for help')
       sys.exit()
   elif inputcmd == 'search':
       print ('Read data from :', inputpath)
       
       # loading data
       try:
           info = dir_info(inputpath)
           if info == '':
               print('please verify path')
               raise SystemExit
           data = load_data(inputpath)
           # start search console
           prompt = Prompt()
           prompt.data = data
           prompt.prompt = 'search> '
           prompt.cmdloop('Starting prompt...')
       except Exception as e:
           print(e)
   else: 
       print('something went wrong ')
       
if __name__ == "__main__":
   main(sys.argv[1:])