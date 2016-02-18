# coding: utf-8
''' This script allows you to copy a .py script to the iOS clipboard and then use Open In...
to have that script saved in Pythonista.  This requires both the Workflow and Pythonista apps
and the workflow at https://workflow.is/workflows/2102d6b710844244bcc22742e860b62c'''

import clipboard
import console
import os
import sys

def save(filename, text):
    with open(filename,'w') as f:
        f.write(text)
    return filename

def main():
    text = clipboard.get()
    assert text, 'No text on the clipboard!'
    filename = sys.argv[1]
    console.clear()
    print('Wait a Moment Please!')
    filename = save(filename, text)
    console.set_font('Futura', 16)
    print('Done!\nFile Saved as:\n' + filename)
    
if __name__ == '__main__':
    main()