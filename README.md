# py_create
A Windows command to generate a Python file with a clean customizable template.

## Installation
⚠️ Should only work on Windows
1. Clone this repository.
2. Copy the path of the directory in which "py_create.py" and "py_create.bat" is in.
3. Open "System Environment Variables" in your Start menu.
4. Click on "Environment Variables" button.
5. In System Variables, click on "Path" and click edit.
6. Create a new path, and paste the directory path of the local repository.
7. Click "Ok".

## Usage
After following the installation steps above, you may now use the command "py_create" in any directory of your device.

To use this,
1. Open Windows Powershell and go to any directory of your choosing.
2. Follow this format: 
    ``` powershell
    $ py_create <filename>
    ex. py_create convert_currency
    ```
    Note: Do not add file extension like ".py" in your filename.
3. Fill out the form regarding the project details.
    ``` powershell
    # Sample
    Enter project title: Currency Converter
    Enter project description: Scrapes a currency converter website to get rates.
    ```
4. This will create a Python file in this directory with this template:
    
    **convert_currency.py**

    ```python
    """
    New Sample File
    ---------------
    This is a sample description for the sample file
    """

    def test_func():
        """This is a sample description"""
        print('Running test func...')

    if __name__ == '__main__':
        test_func()
    ```
