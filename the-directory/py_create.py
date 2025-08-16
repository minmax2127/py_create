"""
Python Script template
-----------------------
Creates a template for your Python file
"""
import sys

def get_command_line_filename():
    """ Takes the filename, passed as a command-line argument"""
    filename = ""
    if len(sys.argv) > 1:
        # prompt user to enter only a filename without the file extension
        filename = sys.argv[1]
        if "." in filename:
            print("Only enter a filename without an extension. Ex. py py_create.py new_filename")
            sys.exit(1)
        filename = filename + ".py"
    else:
        print("Please enter the desired filename of your Python file. ex. sample_python")
        sys.exit(1)

    return filename

def comment_out(txt):
    """ Returns a commented out section """
    return '"""' + txt + '"""'

def build_template(title, desc):
    """ Returns the entire template """
    # Introduction Section
    introduction = f"\n{title}\n{"-" * len(title)}\n{desc}\n"
    introduction = comment_out(introduction)

    # Test Function
    test_func = f"\n\ndef test_func():\n    {comment_out("This is a sample description")}\n    print('Running test func...')"
    
    # Main Function
    main_func = f"\n\nif __name__ == '__main__':\n    test_func()"

    return introduction + test_func + main_func


if __name__ == "__main__":
    # create a python file from the filename
    filename = get_command_line_filename()
    f = open(filename, "w")

    # take user input for the title and description
    project_title = input("Enter project title: ")
    project_description = input("Enter project description: ")

    # insert the template
    template = build_template(project_title, project_description)
    f.write(template)

    # close filestream
    f.close()

    