import threading
import time
import re

# let user know the program is starting
print("starting program...")


# function to rewrite the program
def rewrite():
    # wait for main thread to exit
    print("waiting one second...")
    time.sleep(1)

    # check the file to see if file was already changed or not
    print("checking file...")
    f = open('rewriteMe.py', 'r')
    file_string = f.read()
    # if file was previously changed (no matches), exit the program
    regex_list = re.findall(r'\nprint\(.*(start).*\)', file_string)
    if not regex_list:
        print('exiting program...')
        exit(0)
    # if file was not previously changed, change the file (this file)
    replaced_string = re.sub(r'\nprint\(.*(start).*\)', '\nprint("this is the replaced string")', file_string)
    f.close()

    # rewrite the file with the altered contents
    print('rewriting file...')
    f = open('rewriteMe.py', 'w')
    f.write(replaced_string)
    f.close()

    # execute the altered file (again, it is this file).  no need to re-read it since it's already in the variable.
    print('executing file...')
    exec replaced_string
    exit(0)

# take in other file as code (rather than as string input) and execute it
input_file = open('inputAsCode.py', 'r')
string = input_file.read()
exec string
input_file.close()

# make thread to run other function (DO NOT WAIT FOR IT TO FINISH.  JUST EXIT)
t = threading.Thread(target=rewrite)
t.start()
