<html>
<Body>
<h1>##Lab7</h1>
<h2>
Here we do take the Goory a python plugin as the project example.
Goory is a super intreseting Python GUI application development framework, which could avoid the Terminal application operating and to became a GUI interface.
</h2>
##At the beginning I used the Python 3 as the enviroment, please check before use.
<hr/>

##Download and install
##For install we could pip or git clone, please make sure install and finish config of pip and git before using. 

pip install Gooey
<br/>
#or 
<br/>
git clone https://github.com/chriskiehl/Gooey.git
<hr/>


##Widgets(Not all)

<table>
  <tr>
    <td>Widgets Name</td>
    <td>Widgets Type</td>
  </tr>
  <tr>
    <td>FileChooser</td>
    <td>File selector</td>
  </tr>
<tr>
    <td>MultiFileChooser</td>
    <td>File multiselector</td>
  </tr>
<tr>
    <td>DirChooser</td>
    <td>Directory selector</td>
  </tr>
<tr>
    <td>MultiDirChooser</td>
    <td>Directory multielector</td>
  </tr>
<tr>
    <td>FileSaver</td>
    <td>File saving</td>
  </tr>
<tr>
    <td>DateChooser</td>
    <td>Date select</td>
  </tr>
<tr>
    <td>TextField</td>
    <td>Text Entry Box</td>
  </tr>
<tr>
    <td>Dropdown</td>
    <td>dropdown list</td>
  </tr>
<tr>
    <td>Counter</td>
    <td>Number Counter</td>
  </tr>
<tr>
    <td>CheckBox</td>
    <td>Check Box</td>
  </tr>
</table>

##Example Beginnging.
<br/>
##Let's start with a simple CLI application based on the Argparse library:  

from argparse import ArgumentParser
def main():<br/>
    parser = ArgumentParser(description="My Cool GUI Program!")<br/>
    parser.add_argument('Filename')<br/>
    parser.add_argument('Date')<br/>
    parser.parse_args()<br/>

if __name__ == '__main__':
    main()

##There is a CLI program that accepts two mandatory parameters Filename and Date, but for simplicity we have not specified its functionality.  
 
##To run the python cli.py FILENAME DATE command, run python cli.py FILENAME DATE.  

from gooey import Gooey, GooeyParser

@Gooey<br/>
def main():##(Global configuration)<br/>
    parser = GooeyParser(description="My Cool GUI Program!")<br/>
    parser.add_argument('Filename')<br/>
    parser.add_argument('Date')<br/>
    parser.parse_args()<br/>

if   __name__ == '__main__':
    main()

##This could gives us a simple GUI dialog, and basically didn't take much coding.<br/>
##IF we add the new lines in it we will get a Dedicated control of Date, Like a Selection sub window.

parser.add_argument('Filename', widget="FileChooser")<br/>
parser.add_argument('Date', widget="DateChooser")

##Also it is easy to custom your GUI Layout by using code.
<br/>
show_sidebar=True<br/>
show_sidebar=False<br/>
navigation='TABBED'<br/>
tabbed_groups=True<br/>

## work site 
https://github.com/chriskiehl/GooeyExamples
</Body>
</html>
