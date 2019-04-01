##########################################################################
# CS 101
# Program : 4 Web Headers
# Name Erik Marquez
# Email eemxr9@mail.umkc.edu
# PROBLEM : Web Headers - Take input from a user. open a txt file and return the headers from that file
# ALGORITHM :
#   1. Ask user for a file to open
#   2. Validate the input
#   3. Ask user for a file to save to
#   4. Validate the input
#   5. Repeat
#   6. User can quite with Q
# ERROR HANDLING:
# Any Special Error handling to be noted.
# OTHER COMMENTS:
# Any special comments
###########################################################################




headers = ('<h1>','<h2>','<h3>','<h4>','<h5>','<h6>','<h7>','<h8>',)


def start_file():
    '''Ask the user for a file to open
    Validate user input
    Quite when they enter Q
    '''
    while True:
        try:
            file_to_open = input("Enter HTML file to open or Q to exit ==>")

            if file_to_open == "Q" or file_to_open == 'q':
                return 'Q'

            fh=open(file_to_open)
            fh_lines = fh.readlines()
            break

        except FileNotFoundError:
            print('File not found {}\n'.format(file_to_open))

    fh.close()
    return fh_lines

def save_file():
    '''Ask the user for the name of the file to save
    Validate user file.
    '''
    while True:
        try:
            save_to_file = input('\nEnter name of html file to write to ==>')
            sv = open(save_to_file, 'w')
            break

        except IOError:
            print('IO Error {}'.format(save_to_file))

    return sv,save_to_file


def headers_script(start_file, save_file):
    '''opens the file that user secified
    creates file to save to
    saves the file and closses the file.
    '''
    for idx in start_file:
        idx = idx.strip()
        if idx[0:4] in headers:
            key = headers.index(idx[0:4])
            key1 = headers.index(idx[0:4]) + 1
            print(('\t'* key),idx[4:len(idx)-5],file=save_file)
            #print(('\t'* key),idx[4:len(idx)-6])
    print()

    save_file.close()


# main program loop


while True:

    start = start_file()

    if start == 'Q':
        break

    save = save_file()

    headers_script(start,save[0])

    print('Successfully output to file {}'.format(save[1]))


    print()

print('\nThanks for using the software')






