import re
import os
import shutil
import argparse
import sys

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
# shows dialog box and return the path
root = Tk()
# root.geometry("550x280")
# confiugures column 0 to stretch with a scaler of 1.
root.columnconfigure(0, weight=1)
# confiugures row 0 to stretch with a scaler of 1.
root.rowconfigure(0, weight=1)
# confiugures column 0 to stretch with a scaler of 1.
root.columnconfigure(1, weight=1)
# confiugures row 0 to stretch with a scaler of 1.
root.rowconfigure(1, weight=1)
# confiugures column 0 to stretch with a scaler of 1.
root.columnconfigure(2, weight=1)
# confiugures row 0 to stretch with a scaler of 1.
root.rowconfigure(2, weight=1)
# root.resizable(False, False)

# # Create a main frame
# main_frame = Frame(root)
# main_frame.pack(fill=BOTH, expand=1)

# # create a canvas
# my_canvas = Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# # create scrollbar to canvas
# my_scrollbar = ttk.Scrollbar(
#     main_frame, orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)

# # config canvas
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
#     scrollregion=my_canvas.bbox("all")))

# # create another frame inside the canvas
# second_frame = Frame(my_canvas)

# # Add new frame to window in canvas
# my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

root.title('ADS Rename Files Tool (Made By Jamie Geddes)')
i = 0
y = 0

# root.iconbitmap('icon.ico')

def findDir():
        global path
        path = filedialog.askdirectory()
        # print(path) turn into label at some point

        return path


def myClick():
    # global path
    myButton2['state'] = 'disabled'
    
    
    
    
    
    # maek list blank each time click is run
    my_listbox.delete(0, END)
    my_listbox2.delete(0, END)
    # check directory
    retval = os.getcwd()

    print("Directory changed successfully %s" % retval)

    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write

    def new_names(filenames):
        """
        Generate new filenames for the given filenames
        """
        print(filenames)

        # print(filenames[0])
        for i in range(0, len(filenames)):
            print("filenames original", i, ":", filenames[i])
            if i == 0:
                exec('Label%d=Label(root,text="Files Submitted:")\nLabel%d.grid(row=3, column=0)' %
                     (i, i))

            # create items in listbox
            my_listbox.insert(END, filenames[i])
            my_listbox.itemconfig(i, {'fg': 'blue'})
            if (i % 2) == 0:
                my_listbox.itemconfig(i, {'bg': '#f5f5f5'})

            # exec('Label%d=Label(root,text= "%d" ". "+"%s",fg="#FF0000")\nLabel%d.grid(row=4, column=4)' %
            #      (i, i+1, filenames[i], i))

        #     for i in range(0, len(Result)):
        #     print "result", i, ":", Result[i]
        #     self.labelVars[i].set(Result[i])
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)

        # Replace white space with underscores:
        filenames_new = (re.sub('\s+', '_', fn) for fn in filenames)
        # Replace white plus with plus:
        filenames_new = (re.sub('\\+', '_plus_',  fn) for fn in filenames_new)
        # Replace white comma with hyphen:
        filenames_new = (re.sub('\,', '-',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\(', '_',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\@', '_at_',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\&', '_and_',  fn) for fn in filenames_new)

        # filenames_new = (
        #     re.sub('\.*[.](?!txt$|jpg$|png$|tif$|bmp$|xlsx$|rtf$|jpeg$|docx$|doc$|odt$|xls$|pdf$|ods$|e57$|obj$|vrml$|mtl$|stl$|aac$|aif$|flac$|mp3$|ogg$|xml$|html$|sgml$|xhtml$|dwg$|dxf$|svg$|csv$|cfm$|vrml$|gml$|xsd$|vrml$|cpg$|dbf$|prj$|sbn$|sbx$|shp$|shx$|shp.xml$|mg$|3DS$|3G2$|3GP$|7z$|AGR$|AI$|BIN$|BLEND$|CSS$|DB$|DOCM$|DOCHTML$|DOCMHTML$|DOT$|fbx$)[^.]*', '-', fn) for fn in filenames_new)

        if var.get() == 1:
            
            # Alphabet For lowercase
            filenames_new = (re.sub('A', 'a',  fn) for fn in filenames_new)
            filenames_new = (re.sub('B', 'b',  fn) for fn in filenames_new)
            filenames_new = (re.sub('C', 'c',  fn) for fn in filenames_new)
            filenames_new = (re.sub('D', 'd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('E', 'e',  fn) for fn in filenames_new)
            filenames_new = (re.sub('F', 'f',  fn) for fn in filenames_new)
            filenames_new = (re.sub('G', 'g',  fn) for fn in filenames_new)
            filenames_new = (re.sub('H', 'h',  fn) for fn in filenames_new)
            filenames_new = (re.sub('I', 'i',  fn) for fn in filenames_new)
            filenames_new = (re.sub('J', 'j',  fn) for fn in filenames_new)
            filenames_new = (re.sub('K', 'k',  fn) for fn in filenames_new)
            filenames_new = (re.sub('L', 'l',  fn) for fn in filenames_new)
            filenames_new = (re.sub('M', 'm',  fn) for fn in filenames_new)
            filenames_new = (re.sub('N', 'n',  fn) for fn in filenames_new)
            filenames_new = (re.sub('O', 'o',  fn) for fn in filenames_new)
            filenames_new = (re.sub('P', 'p',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Q', 'q',  fn) for fn in filenames_new)
            filenames_new = (re.sub('R', 'r',  fn) for fn in filenames_new)
            filenames_new = (re.sub('S', 's',  fn) for fn in filenames_new)
            filenames_new = (re.sub('T', 't',  fn) for fn in filenames_new)
            filenames_new = (re.sub('U', 'u',  fn) for fn in filenames_new)
            filenames_new = (re.sub('V', 'v',  fn) for fn in filenames_new)
            filenames_new = (re.sub('W', 'w',  fn) for fn in filenames_new)
            filenames_new = (re.sub('X', 'x',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Y', 'y',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Z', 'z',  fn) for fn in filenames_new)
            # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('([.](?![A-Za-z0-9]+$))', '-',  fn)
                         for fn in filenames_new)

        # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('[^a-zA-Z0-9._-]', '',  fn)
                         for fn in filenames_new)

        filenames_new = (re.sub('\-shp.xml', '.shp.xml', fn)
                         for fn in filenames_new)

        # Merge consecutive underscores for aesthetics
        filenames_new = [re.sub('_+', '_', fn) for fn in filenames_new]

        # # Merge consecutive underscores for aesthetics
        # filenames_new = [re.sub('_+', '_', fn) for fn in filenames_new]

        if filenames_new != filenames:
            myButton2['state'] = 'normal'
            for i in range(0, len(filenames)):
                print("filenames new:", i, ":", filenames_new[i])
                my_listbox2.insert(END, filenames_new[i])

                my_listbox2.itemconfig(i, {'fg': 'blue'})
                if (i % 2) == 0:
                    my_listbox2.itemconfig(i, {'bg': '#f5f5f5'})

                if filenames_new[i] != filenames[i]:

                    # my_listbox2.insert(END, filenames_new[i])
                    my_listbox2.itemconfig(i, {'fg': 'green'})

                    my_listbox.itemconfig(i, {'fg': 'red'})

            x = 15
            if x == 123:
                for i in range(0, len(filenames)):
                    if filenames_new[i] != filenames[i]:

                        print("filenames change", i, ":", filenames_new[i])
                        # exec('Label%d=Label(root,text="Files changed:")\nLabel%d.grid(row=3, column=4)' %
                        #      (i, i))

                        # my_listbox2.insert(END, filenames_new[i])
                        # exec('Label%d=Label(root,text="New File Name is: "+"%s",fg="#006400")\nLabel%d.grid(row=3, column=0)' %
                        #      (i, filenames_new[i], i))

                return filenames_new
            else:
                print("Please Redo Entry")

        if sorted(filenames) == sorted(filenames_new):
            print(sorted(filenames))
            print(sorted(filenames_new))
            # i=10000
            # exec('Label%d=Label(root,text="Files Submitted All Adhear to Our Guidelines! Wohoo!",fg="#006400")\nLabel%d.grid(row=5,column=0)' %
            #     (i, i))

            # Message box to show complete no changes
            # messagebox.showinfo(
                # title='Alert: No Changes', message="No changes needed to be made at: " + path)
        return filenames_new
    def rename_files_in_dir(dir):
        """
        Walk a directory and rename all files in the path.
        """

        for (dirpath, dirnames, filenames) in os.walk(dir):
            i = 0

            # Rename the filenames
            filenames_new = new_names(filenames)
            # list_length = len(filenames_new)
            # oglist_length = len(filenames)
            for f_old, f_new in zip(filenames, filenames_new):

                f_old = os.path.join(dirpath, f_old)
                f_new = os.path.join(dirpath, f_new)

                print("Hello this is the fnew thing"+f_new)
                print("This is the filenames_new thing 0 array:")

                if f_old == f_new:

                    continue

                err("Renaming %s to %s\n" %
                    (os.path.abspath(f_old), os.path.abspath(f_new)))
                shutil.move(f_old, f_new)

    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]

        for d in dirs:

            print('HEY YOU OVER HERE!' + d)

            rename_files_in_dir(d)

    # messagebox.showinfo(title='Alert', message="Complete Changes at: " + path)



def fix():

    os.chdir(path)
    my_listbox.delete(0, END)
    my_listbox2.delete(0, END)
    retval = os.getcwd()

    print("Directory For fix %s" % retval)

    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write

    def new_names(filenames):
        """
        Generate new filenames for the given filenames
        """
        print(filenames)

        # print(filenames[0])
        for i in range(0, len(filenames)):
            print("filenames original", i, ":", filenames[i])
            if i == 0:
                exec('Label%d=Label(root,text="Files Submitted:")\nLabel%d.grid(row=3, column=0)' %
                     (i, i))

            # create items in listbox
            my_listbox.insert(END, filenames[i])
            my_listbox.itemconfig(i, {'fg': 'blue'})
            if (i % 2) == 0:
                my_listbox.itemconfig(i, {'bg': '#f5f5f5'})

        # Replace white space with underscores:
        filenames_new = (re.sub('\s+', '_', fn) for fn in filenames)
        # Replace white plus with plus:
        filenames_new = (re.sub('\\+', '_plus_',  fn) for fn in filenames_new)
        # Replace white comma with hyphen:
        filenames_new = (re.sub('\,', '-',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\(', '_',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\@', '_at_',  fn) for fn in filenames_new)
        # Replace white brackets with undescore:
        filenames_new = (re.sub('\&', '_and_',  fn) for fn in filenames_new)
        

        # filenames_new = (
        #     re.sub('\.*[.](?!txt$|jpg$|png$|tif$|bmp$|xlsx$|rtf$|jpeg$|docx$|doc$|odt$|xls$|pdf$|ods$|e57$|obj$|vrml$|mtl$|stl$|aac$|aif$|flac$|mp3$|ogg$|xml$|html$|sgml$|xhtml$|dwg$|dxf$|svg$|csv$|cfm$|vrml$|gml$|xsd$|vrml$|cpg$|dbf$|prj$|sbn$|sbx$|shp$|shx$|shp.xml$)[^.]*', '', fn) for fn in filenames_new)

        if var.get() == 1:
            # Alphabet For lowercase
            filenames_new = (re.sub('A', 'a',  fn) for fn in filenames_new)
            filenames_new = (re.sub('B', 'b',  fn) for fn in filenames_new)
            filenames_new = (re.sub('C', 'c',  fn) for fn in filenames_new)
            filenames_new = (re.sub('D', 'd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('E', 'e',  fn) for fn in filenames_new)
            filenames_new = (re.sub('F', 'f',  fn) for fn in filenames_new)
            filenames_new = (re.sub('G', 'g',  fn) for fn in filenames_new)
            filenames_new = (re.sub('H', 'h',  fn) for fn in filenames_new)
            filenames_new = (re.sub('I', 'i',  fn) for fn in filenames_new)
            filenames_new = (re.sub('J', 'j',  fn) for fn in filenames_new)
            filenames_new = (re.sub('K', 'k',  fn) for fn in filenames_new)
            filenames_new = (re.sub('L', 'l',  fn) for fn in filenames_new)
            filenames_new = (re.sub('M', 'm',  fn) for fn in filenames_new)
            filenames_new = (re.sub('N', 'n',  fn) for fn in filenames_new)
            filenames_new = (re.sub('O', 'o',  fn) for fn in filenames_new)
            filenames_new = (re.sub('P', 'p',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Q', 'q',  fn) for fn in filenames_new)
            filenames_new = (re.sub('R', 'r',  fn) for fn in filenames_new)
            filenames_new = (re.sub('S', 's',  fn) for fn in filenames_new)
            filenames_new = (re.sub('T', 't',  fn) for fn in filenames_new)
            filenames_new = (re.sub('U', 'u',  fn) for fn in filenames_new)
            filenames_new = (re.sub('V', 'v',  fn) for fn in filenames_new)
            filenames_new = (re.sub('W', 'w',  fn) for fn in filenames_new)
            filenames_new = (re.sub('X', 'x',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Y', 'y',  fn) for fn in filenames_new)
            filenames_new = (re.sub('Z', 'z',  fn) for fn in filenames_new)

            # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('([.](?![A-Za-z0-9]+$))', '-',  fn)
                         for fn in filenames_new)

        
        
        
        

        # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('[^a-zA-Z0-9._-]', '',  fn)
                         for fn in filenames_new)

        filenames_new = (re.sub('\-shp.xml', '.shp.xml', fn)
                        for fn in filenames_new)

        # Merge consecutive underscores for aesthetics
        filenames_new = [re.sub('_+', '_', fn) for fn in filenames_new]

        # if var2.get() == 1:
        #     with open("file_names.txt", "wt", encoding='utf-8') as output:
        #         output.write('\n'.join(filenames))
        #         output.write('\n')

        if filenames_new != filenames:
            for i in range(0, len(filenames)):
                print("filenames new:", i, ":", filenames_new[i])
                my_listbox2.insert(END, filenames_new[i])

                my_listbox2.itemconfig(i, {'fg': 'blue'})
                if (i % 2) == 0:
                    my_listbox2.itemconfig(i, {'bg': '#f5f5f5'})

                if filenames_new[i] != filenames[i]:

                    # my_listbox2.insert(END, filenames_new[i])
                    my_listbox2.itemconfig(i, {'fg': 'green'})

                    my_listbox.itemconfig(i, {'fg': 'red'})
                    myButton2['state'] = 'disabled'

            warn = messagebox.askquestion(
                "Found Issues", "We Have Found Incorrect Files, Do You Wish to Continue?", icon='warning')
            if warn == 'yes':
                for i in range(0, len(filenames)):
                    if filenames_new[i] != filenames[i]:

                        print("filenames change", i, ":", filenames_new[i])
                        exec('Label%d=Label(root,text="Files changed:")\nLabel%d.grid(row=3, column=4)' %
                             (i, i))

                        # my_listbox2.insert(END, filenames_new[i])
                        # exec('Label%d=Label(root,text="New File Name is: "+"%s",fg="#006400")\nLabel%d.grid(row=3, column=0)' %
                        #      (i, filenames_new[i], i))
                
                return filenames_new
            else:
                print("Please Redo Entry")

        if sorted(filenames) == sorted(filenames_new):
            print(sorted(filenames))
            print(sorted(filenames_new))
            
            exec('Label%d=Label(root,text="Files Submitted All Adhear to Our Guidelines! Wohoo!",fg="#006400")\nLabel%d.grid(row=5,column=0)' %
                 (i, i))

            # Message box to show complete no changes
            messagebox.showinfo(
                title='Alert: No Changes', message="No changes needed to be made at: " + path)

    def rename_files_in_dir(dir):
        """
        Walk a directory and rename all files in the path.
        """

        for (dirpath, dirnames, filenames) in os.walk(dir):
            i = 0

            # Rename the filenames
            filenames_new = new_names(filenames)
            # list_length = len(filenames_new)
            # oglist_length = len(filenames)
            for f_old, f_new in zip(filenames, filenames_new):

                f_old = os.path.join(dirpath, f_old)
                f_new = os.path.join(dirpath, f_new)

                print("Hello this is the fnew thing"+f_new)
                print("This is the filenames_new thing 0 array:")

                if f_old == f_new:

                    continue

                err("Renaming %s to %s\n" %
                    (os.path.abspath(f_old), os.path.abspath(f_new)))
                shutil.move(f_old, f_new)

            # # Rename the directories, and modify dirnames in place to aid os.walk
            # dirnames_new = new_names(dirnames)
            # for d_old, d_new in zip(dirnames, dirnames_new):

            #     d_old = os.path.join(dirpath, d_old)
            #     d_new = os.path.join(dirpath, d_new)

            #     if d_old == d_new:
            #         continue

            #     err("Renaming dir %s to %s\n" %
            #         (os.path.abspath(d_old), os.path.abspath(d_new)))
            #     shutil.move(d_old, d_new)

            # del dirnames[:]
            # dirnames.extend(dirnames_new)

    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]

        for d in dirs:

            print('HEY YOU OVER HERE!' + d)

            rename_files_in_dir(d)

    # messagebox.showinfo(title='Alert', message="Complete Changes at: " + path)

def printFiles():
    os.chdir(path)
    retval = os.getcwd()
    open("file_names.txt", "w", encoding='utf-8')

    print("Directory changed successfully %s" % retval)

    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write
    
    def print_files_in_directory(dir):
        paths = os.listdir(dir)
        abs_paths = [os.path.join(dir, p) for p in paths]
        # filter for paths that are files
        file_list = [p for p in paths if os.path.isfile(p)]
        fileCounter = 0
        for root, dirs, files in os.walk(dir):
            for file in files:    
                if file.endswith('.jpg'):
                    fileCounter += 1
        open("file_names.txt", "a+", encoding='utf-8').write('\n'.join(file_list))
        open("file_names.txt", "a+", encoding='utf-8').write('\n File_Names_Count:')
        open("file_names.txt", "a+", encoding='utf-8').write('\n'.join(str(fileCounter)) + 'jpg')
       

        # for (dirpath, dirnames, filenames) in os.walk(dir):
        #     # for i in range(0, len(filenames)):
        #         with open("file_names.txt", "a+", encoding='utf-8') as output:
        #             output.write('\n'.join(filenames))
        #             output.write('\n')

            # print(filenames)
            # with open("file_names.txt", "a+", encoding='utf-8') as output:
            #     output.write('\n'.join(filenames))
            #     output.write('\n')
            #     data = output.read(100)
            #     if len(data) > 0:

            #         output.write('\n'.join(filenames))
            #         output.write('\n')

#  all_files = root, dirs, files = next(os.walk(dir))

#         file = files[i]



#         text_file = open("file_names.txt", "wt", encoding='utf-8')
#         text_file.write(filenames)
#         text_file.close()
        
    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]

        for d in dirs:

         

            print_files_in_directory(d)

    
    return

myButton = Button(root, text="Run Check",
                  command=myClick)

myButton.grid(column=0, row=0, padx=5, pady=5, sticky='nsew')

myButton4 = Button(root, text="Select Directory To Check",
                  command=findDir)

myButton4.grid(column=1, row=1, padx=5, pady=5, sticky='nsew')

myButton2 = Button(root,state=DISABLED, text="fix",
                   command=fix)

myButton2.grid(columnspan=3,column=2, row=0, padx=5, pady=5, sticky='nsew')

var = IntVar()
var2 = IntVar()
c = Checkbutton(root, text="lowercase", variable=var).grid(
    column=1, row=0, padx=5, pady=5, sticky='nsew')

printList = Button(root, text="Print filenames",
                  command=printFiles).grid(column=4, row=4, padx=5, pady=5, sticky='nsew')

# printList = Checkbutton(root, text="print list of names", variable=var2).grid(
#     column=2, row=0, padx=5, pady=5, sticky='nsew')


submitlabel = Label(root, text="Files Submitted:").grid(row=1, column=0)
changedlabel = Label(root, text="New file names:").grid(row=1, column=1)


my_listbox2 = Listbox(root)
my_listbox2.grid(row=2, column=1, padx=5, pady=5, sticky='nsew', columnspan=4)


my_listbox = Listbox(root)
my_listbox.grid(row=2, column=0, padx=5, pady=5, sticky='nsew', columnspan=1)



root.mainloop()
