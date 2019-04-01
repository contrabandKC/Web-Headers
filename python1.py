def start_file():
    '''Ask the user for a file to open
    Validate user input
    Quite when they enter Q
    '''
    while True:
        try:
            file_to_open = input("Enter HTML file to open or Q to exit ==>")

            if file_to_open == "Q" or file_to_open == 'q':
                return file_to_open

            fh=open(file_to_open)
            fh_lines = fh.readlines()
            break

        except FileNotFoundError:
            print('File not found {}\n'.format(file_to_open))

    fh.close()
    return fh_lines

start_file()