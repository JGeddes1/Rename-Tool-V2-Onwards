
import datetime
import re
import os
import shutil
import argparse
import sys
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
from typing import Counter
from unicodedata import name
# shows dialog box and return the path

global count
global  noChangeLabel
global length
# class MyApp:
#     def __init__(self, parent):
#         self.myParent = parent

#         self.main_container = Frame(parent, bg="green")
#         self.main_container.grid()

#         self.top_frame = Frame(self.main_container)
#         self.top_frame.grid()

#         self.top_left = Frame(self.top_frame, bd=2)
#         self.top_left.grid(row=0, column=0)

#         self.top_right = Frame(self.top_frame, bd=2)
#         self.top_right.grid(row=0, column=2)

#         self.top_left_label = Label(self.top_left, bd=2, bg="red", text="Top Left", width=22, anchor=W)
#         self.top_left_label.grid(row=0, column=0)

#         self.top_right_label = Label(self.top_right, bd=2, bg="blue", text="Top Right", width=22, anchor=E)
#         self.top_right_label.grid(row=0, column=0)

#         self.bottom_frame = Frame(self.main_container, bd=2)
#         self.bottom_frame.grid(row=2, column=0)

#         self.text_box = Text(self.bottom_frame, width=40, height=5)
#         self.text_box.grid(row=0, column=0)
root = Tk()


# root.geometry("550x280")
# confiugures column 0 to stretch with a scaler of 1.

# # # confiugures row 0 to stretch with a scaler of 1.
# root.rowconfigure(0, weight=1)
# # # confiugures column 0 to stretch with a scaler of 1.
# root.columnconfigure(1, weight=1)
# # # confiugures row 0 to stretch with a scaler of 1.
# root.rowconfigure(1, weight=1)
# # # confiugures column 0 to stretch with a scaler of 1.
# root.columnconfigure(2, weight=1)
# # # confiugures row 0 to stretch with a scaler of 1.
# root.rowconfigure(2, weight=1)
# # root.resizable(False, False)

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
global path
# root.iconbitmap('icon.ico')


def myClick():
    # global path
    myButton2['state'] = 'disabled'
    
    def step():
        for x in range(5):
            my_progress['value'] +=20
            root.update_idletasks()
            
    
    


    def findDir():
        global path
        global currentDirectoryLabel
        path = filedialog.askdirectory(master='', initialdir='', title="Select your Source directory", mustexist=True)
        currentDirectoryLabel = Label(footer, text="Current Working Directory:                                                                                                                                                                                              ").grid(column=0, row=7, padx=5, pady=5, sticky='w')
        currentDirectoryLabel = Label(footer, text="Current Working Directory: " + path).grid(column=0, row=7, padx=5, pady=5, sticky='w')
        
        # print(path) turn into label at some point
        
        print('OPOP' + str(path))
        if path == None or path == '':
            messagebox.showwarning('Error', 'No path selected, resetting..')

            # sys.exit("Error message")
            return path
        else:
            
            return path
        
    
    findDir()
    

    
    
    # step()
    # maek list blank each time click is run
    my_listbox.delete(0, END)
    my_listbox2.delete(0, END)
    # check directory
    # retval = os.getcwd()
    if path == '':
        return False
    print("Directory changed successfully %s" % path)

    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write
    print(path)
    global numberFilesAlreadyGone
    global numberFilesAlreadyGone2
    numberFilesAlreadyGone = -1
    numberFilesAlreadyGone2 = -1
    def new_names(filenames):
        global numberFilesAlreadyGone
        global numberFilesAlreadyGone2
         
        """
        Generate new filenames for the given filenames
        """
        print(filenames)
        filelength = len(filenames)
        
        my_progress['value'] =50
        root.update_idletasks()
        time.sleep(0.02)
        # print(filenames[0])
        # for i in range(0, filelength):
            
            
        #     print("filenames original", i, ":", filenames[i])
        #     if i == 0:
        #         exec('Label%d=Label(root,text="Files Submitted:")\nLabel%d.grid(row=3, column=0)' %
        #              (i, i))
        #     numberFilesAlreadyGone = numberFilesAlreadyGone + 1
        #     # create items in listbox
        #     my_listbox.insert(numberFilesAlreadyGone, filenames[i] + '' +str(numberFilesAlreadyGone))
            
           
            
        #     my_listbox.itemconfig(numberFilesAlreadyGone, {'fg': 'blue'})
        #     if (numberFilesAlreadyGone % 2) == 0:
        #         my_listbox.itemconfig(numberFilesAlreadyGone, {'bg': '#f5f5f5'})

            


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
            filenames_new = (re.sub('', '',  fn.lower()) for fn in filenames_new)

        if var3.get()==1:
            
            
            filenames_new = (re.sub('.JPG', 'jpg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.JPEG', 'jpeg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSV', 'csv',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.SHP', 'shp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.HTML', 'html',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIFF', 'tiff',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TXT', 'txt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PNG', 'png',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIF', 'tif',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.BMP', 'bmp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.RTF', 'rtf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOCX', 'docx',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOC', 'doc',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODT', 'odt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XLS', 'xls',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PDF', 'pdf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODS', 'ods',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.E57', 'e57',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.OBJ', 'obj',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DWG', 'dwg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DXF', 'dxf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSS', 'css',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XSD', 'xsd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XML', 'xml',  fn) for fn in filenames_new)
            
            
            

            # filenames_new = (re.sub('JPG', 'jpg',  fn) for fn in filenames_new)
            # filenames_new = (re.sub('JPEG', 'jpeg',  fn) for fn in filenames_new)
            
                
            # for fn in filenames_new:
            #     i=0
            #     filenames_new_list = list(filenames_new)
            #     print ('hello this is filenames list --->   ', filenames_new_list)
            #     print ('hello this is filenames fn --->   '+ fn)
            #     file = fn
            #     basename, ext = fn.split('.')
            #     print(basename + 'this is basename')
            #     print(ext + 'this is ext')
            #     newname = []
            #     fixedname = basename + '.' + ext.lower()
            #     newname.insert(i,fixedname) 
            #     print('this is fixced name list'+list(fixedname))
            #     # print(newname + 'this is new name')
            #     # filenames_changed = newname
            #     filenames_new[i] = newname[i]
            # #     i=+1
            # print('this is fnnnn'+fn)
                    
                    
            # print ('hello this is filenames list --->   ',  list(filenames_new))
            #     # string_test = str(filenames_new)
                # string_newname = str(newname)
                # filenames_new = (re.sub(string_test, string_newname,  fn) for fn in filenames_new)
                # print(fn +'this is after doing shit')
                
            
            
                # filenames_new = (re.sub('', newname,  fn) for fn in filenames_new)

                # result = fn.split('.')
                # filename = ".".join(result[0:-1]).lower() + '.' + result[-1].upper()
                # filenames_new = (re.sub(filenames_new, filename,  fn) for fn in filenames_new)
            

            

   
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
        
        noChangeLabel = Label(main_container, text="No Changes needed")
        noChangeLabel.grid(row=3, column=0)
        
        if noChangeLabel.winfo_exists() == 1:
            if filenames_new != filenames:
                noChangeLabel.destroy()
                print("HELP ME IM WORKING BUT NOT DELETING")
        noChangeLabel.destroy()    
        if filenames_new != filenames:
            myButton2['state'] = 'normal'
            
            for i in range(0, filelength):
                
                numberFilesAlreadyGone2 = numberFilesAlreadyGone2 + 1
                print("filenames new:", i, ":", filenames_new[i])
                my_listbox2.insert(numberFilesAlreadyGone2, filenames_new[i] + ' ' + str(numberFilesAlreadyGone2))
                my_listbox.insert(numberFilesAlreadyGone2, filenames[i] + ' ' + str(numberFilesAlreadyGone2))
                my_listbox2.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                my_listbox.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                if (i % 2) == 0:
                    my_listbox2.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})
                    my_listbox.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})

                if filenames_new[i] != filenames[i]:
                    my_listbox2.delete(numberFilesAlreadyGone2)
                    my_listbox.delete(numberFilesAlreadyGone2)
                    wrongfilecount = 0
                    wrongfilecount +=1
                    my_listbox2.insert(0, filenames_new[i] + ' ' + str(numberFilesAlreadyGone2))
                    # my_listbox2.insert(END, filenames_new[i])
                    my_listbox2.itemconfig(0, {'fg': 'green'})
                    
                    
                    my_listbox.insert(0, filenames[i] + ' ' + str(numberFilesAlreadyGone2))
                    my_listbox.itemconfig(0, {'fg': 'red'})
                    
        if filenames == filenames_new :
            # noChangeLabel = exec('Label%d=Label(root,text="No Changes needed")\nLabel%d.grid(row=3, column=0)' %
                    #   (1000000, 1000000))
            global count
            
            
            
            
            
            print("This is no change"+str(noChangeLabel.winfo_exists))
           
            

            for i in range(0, filelength):
                
                numberFilesAlreadyGone2 = numberFilesAlreadyGone2 + 1
                print("filenames new:", i, ":", filenames_new[i])
                my_listbox2.insert(numberFilesAlreadyGone2, filenames_new[i] + ' ' + str(numberFilesAlreadyGone2))
                my_listbox.insert(numberFilesAlreadyGone2, filenames[i] + ' ' + str(numberFilesAlreadyGone2))
                my_listbox2.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                my_listbox.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                if (i % 2) == 0:
                    my_listbox2.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})
                    my_listbox.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})
                numberFilesAlreadyGone = numberFilesAlreadyGone + 1
                count = numberFilesAlreadyGone
                # my_listbox.insert(END, filenames[i] + '0')
                # my_listbox2.insert(END, filenames[i])
                # my_listbox2.itemconfig(numberFilesAlreadyGone, {'fg': 'blue'})
                # my_listbox.itemconfig(numberFilesAlreadyGone, {'fg': 'blue'})
                
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
        my_progress['value'] =100
        root.update_idletasks()
        time.sleep(0.02)
        
        if sorted(filenames) == sorted(filenames_new):
            
            print(sorted(filenames))
            print(sorted(filenames_new))

            # exec('Label%d=Label(root,text="Files Submitted All Adhear to Our Guidelines! Wohoo!",fg="#006400")\nLabel%d.grid(row=5,column=0)' %
            #      (i, i))

            # Message box to show complete no changes
            # messagebox.showinfo(
            #     title='Alert: No Changes', message="No changes needed to be made at: " + path)
        if var2.get() == 1:
            
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
            if var4.get() ==1:

                # Rename the directories, and modify dirnames in place to aid os.walk
                dirnames_new = new_names(dirnames) # sends the directory names off to the new names function and runs so appears on listbox but could change
                for d_old, d_new in zip(dirnames, dirnames_new):

                    d_old = os.path.join(dirpath, d_old)
                    d_new = os.path.join(dirpath, d_new)

                    if d_old == d_new:
                        continue

                    err("Renaming dir %s to %s\n" %
                        (os.path.abspath(d_old), os.path.abspath(d_new)))
                    shutil.move(d_old, d_new)

                del dirnames[:]
                dirnames.extend(dirnames_new)

                # err("Renaming %s to %s\n" %
                #     (os.path.abspath(f_old), os.path.abspath(f_new)))
                # shutil.move(f_old, f_new)

    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]
    
        for d in dirs:

            print('HEY YOU OVER HERE!' + d)

            rename_files_in_dir(d)

    # messagebox.showinfo(title='Alert', message="Complete Changes at: " + path)



def fix():

    

    os.chdir(path)
    # my_listbox.delete(0, END)
    # my_listbox2.delete(0, END)
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
            # if i == 0:
                # exec('Label%d=Label(root,text="Files Fixed:")\nLabel%d.grid(row=3, column=0)' %
                #     (i, i))
            # # create items in listbox
            # my_listbox.insert(END, filenames[i])
            # my_listbox.itemconfig(i, {'fg': 'blue'})
            # if (i % 2) == 0:
            #     my_listbox.itemconfig(i, {'bg': '#f5f5f5'})

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
            filenames_new = (re.sub('', '',  fn.lower()) for fn in filenames_new)

            # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('([.](?![A-Za-z0-9]+$))', '-',  fn)
                         for fn in filenames_new)

        
        
        if var3.get()==1:
            filenames_new = (re.sub('.JPG', 'jpg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.JPEG', 'jpeg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSV', 'csv',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.SHP', 'shp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.HTML', 'html',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIFF', 'tiff',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TXT', 'txt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PNG', 'png',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIF', 'tif',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.BMP', 'bmp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.RTF', 'rtf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOCX', 'docx',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOC', 'doc',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODT', 'odt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XLS', 'xls',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PDF', 'pdf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODS', 'ods',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.E57', 'e57',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.OBJ', 'obj',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DWG', 'dwg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DXF', 'dxf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSS', 'css',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XSD', 'xsd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XML', 'xml',  fn) for fn in filenames_new)
            # \.*[.](?!txt$|jpg$|png$|tif$|bmp$|xlsx$|rtf$|jpeg$|docx$|doc$|odt$|xls$|pdf$|ods$|e57$|obj$|vrml$|mtl$|stl$|aac$|aif$|flac$|mp3$|ogg$|xml$|html$|sgml$|xhtml$|dwg$|dxf$|svg$|csv$|cfm$|vrml$|gml$|xsd$|vrml$|cpg$|dbf$|prj$|sbn$|sbx$|shp$|shx$)', '', fn) for fn in filenames_new)
            # for fn in filenames:
            #     print ('hello')
            #     file = fn
            #     basename, ext = file.split('.')
            #     print(basename + 'this is basename')
            #     print(ext + 'this is ext')
            #     newname = basename + '.' + ext.lower()
            #     print(newname + 'this is new name')
            #     filenames_changed = newname
            #     filenames_new = (re.sub(filenames, filenames_changed,  fn) for fn in filenames_new)


        if var4.get() ==1:
            dirList = []
            for (dirpath, dirnames, filenames) in os.walk(dir):
                for d in dirnames:
                    dirList.append(os.path.join(dirpath, d))
            return
            
        # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('[^a-zA-Z0-9._-]', '',  fn)
                         for fn in filenames_new)

        filenames_new = (re.sub('\-shp.xml', '.shp.xml', fn)
                        for fn in filenames_new)
        
        # Merge underscores after hyphen for aesthetics
        filenames_new = [re.sub(' - ', '-', fn) for fn in filenames_new]

        # Merge consecutive underscores for aesthetics
        filenames_new = [re.sub('_+', '_', fn) for fn in filenames_new]

        

        # if var2.get() == 1:
        #     with open("file_names.txt", "wt", encoding='utf-8') as output:
        #         output.write('\n'.join(filenames))
        #         output.write('\n')

        if filenames_new != filenames:
            # for i in range(0, len(filenames)):
            #     print("filenames new:", i, ":", filenames_new[i])
            #     my_listbox2.insert(END, filenames_new[i])

            #     my_listbox2.itemconfig(i, {'fg': 'blue'})
            #     if (i % 2) == 0:
            #         my_listbox2.itemconfig(i, {'bg': '#f5f5f5'})

            #     if filenames_new[i] != filenames[i]:

            #         # my_listbox2.insert(END, filenames_new[i])
            #         my_listbox2.itemconfig(i, {'fg': 'green'})

            #         my_listbox.itemconfig(i, {'fg': 'red'})
            #         myButton2['state'] = 'disabled'

            # warn = messagebox.askquestion(
            #     "Found Issues", "We Have Found Incorrect Files, Do You Wish to Continue?", icon='warning')
            # if warn == 'yes':
            for i in range(0, len(filenames)):
                if filenames_new[i] != filenames[i]:
                        
                    print("filenames change", i, ":", filenames_new[i])
                    # exec('Label%d=Label(root,text="Files changed:")\nLabel%d.grid(row=3, column=4)' %
                    #          (i, i))
                             

                        # my_listbox2.insert(END, filenames_new[i])
                        # exec('Label%d=Label(root,text="New File Name is: "+"%s",fg="#006400")\nLabel%d.grid(row=3, column=0)' %
                        #      (i, filenames_new[i], i))
                
                # if i == (len(filenames)-1):
                #     # messagebox.showinfo(
                #     # "Fixed issues", "We Have Fixed Incorrect Files")
                #     # myButton2['state'] = 'disabled'
                    
                # return filenames_new
            else:
                print("Please Redo Entry")
        
        if sorted(filenames) == sorted(filenames_new):
            print(sorted(filenames))
            print(sorted(filenames_new))
            
            
            # exec('Label%d=Label(root,text="Files Submitted All Adhear to Our Guidelines! Wohoo!",fg="#006400")\nLabel%d.grid(row=5,column=0)' %
            #      (i, i))

            # # Message box to show complete no changes
            # messagebox.showinfo(
            #     title='Alert: No Changes', message="No changes needed to be made at: " + path)
        if var2.get() == 1:
            my_progress.stop()
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

        messagebox.showinfo(
        "Fixed issues", "We Have Fixed Incorrect Files")
        myButton2['state'] = 'disabled'
        
        if var4.get() ==1:
            # Rename the directories, and modify dirnames in place to aid os.walk
            dirnames_new = new_names(dirnames)
            for d_old, d_new in zip(dirnames, dirnames_new):

                d_old = os.path.join(dirpath, d_old)
                d_new = os.path.join(dirpath, d_new)

                if d_old == d_new:
                    continue

                err("Renaming dir %s to %s\n" %
                    (os.path.abspath(d_old), os.path.abspath(d_new)))
                shutil.move(d_old, d_new)

            del dirnames[:]
            dirnames.extend(dirnames_new)

    

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
    print('IMWAITING')
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
       
    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]

        for d in dirs:

         

            print_files_in_directory(d)

    
    return
        # for (dirpath, dirnames, filenames) in os.walk(dir):
        #     # for i in range(0, len(filenames)):
        #         with open("file_names.txt", "a+", encoding='utf-8') as output:
        #             output.write(''.join(dirpath))
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



def printSubFiles():
    os.chdir(path)
    retval = os.getcwd()

    # Initialisation
    totalFilesize = 0
    extStr = ''
    extMap = {}
    fileList = []
    fileListName = []
    dirList = []
    allList = []
    spacesList = []
    ampList = []
    plusList = []
    quoteList = []
    commaList = []
    parenthList = []
    otherCharList = []
    dupFileList = []
    systemFileList = []
    emptyFileList = []
    doubleExtList = []
    noExtList = []
        

    outputDir = path
    # open("file_names.txt", "w", encoding='utf-8')

    print("Directory changed successfully %s" % retval)

    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write
    
    def print_files_in_directory(dir):
        # Function to add extensions to a map
        def setExtMap(f):
            filename, ext = os.path.splitext(os.path.basename(f))
            if ext not in extMap:
                extMap[ext] = 1
            else:
                noExt = extMap[ext]
                extMap[ext] = noExt + 1

                # Function to write text to the log file for the report
        def displayReportText(list, text):
            if len(list) > 0:
                logfile.write('\n' + text + '\n')
                for f in list:
                    logfile.write(f + '\n')
        
        totalFilesize = 0
        extStr = ''
        extMap = {}
        fileList = []
        fileListName = []
        dirList = []
        allList = []
        spacesList = []
        ampList = []
        plusList = []
        quoteList = []
        commaList = []
        parenthList = []
        otherCharList = []
        dupFileList = []
        systemFileList = []
        emptyFileList = []
        doubleExtList = []
        noExtList = []
        JPGlist=[]
        paths = os.listdir(dir)
        # abs_paths = [os.path.join(dir, p) for p in paths]
        # # filter for paths that are files
        # file_list = [p for p in paths if os.path.isfile(p)]
        # fileCounter = 0
        # for root, dirs, files in os.walk(dir):
        #     for file in files:    
        #         if file.endswith('.jpg'):
        #             fileCounter += 1
        # open("file_names.txt", "a+", encoding='utf-8').write('\n'.join(file_list))
        # open("file_names.txt", "a+", encoding='utf-8').write('\n File_Names_Count:')
        # open("file_names.txt", "a+", encoding='utf-8').write('\n'.join(str(fileCounter)) + 'jpg')
       

        for (dirpath, dirnames, filenames) in os.walk(path):
            # for i in range(0, len(filenames)):

            for d in dirnames:
                dirList.append(os.path.join(dirpath, d))
            for f in filenames:
                fileList.append(os.path.join(dirpath, f))
                fileListName.append(f)
            
        # Add dirList and fileList into allList
        allList.extend(dirList)
        allList.extend(fileList)
        # Iterate over the files / directories and search for chars
        for paths in allList:
            f = os.path.basename(paths)
            if ' ' in f:
                spacesList.append(paths)
            if '&' in f:
                ampList.append(paths)
            if '+' in f:
                plusList.append(paths)
            if '\'' in f:
                quoteList.append(paths)
            if ',' in f:
                commaList.append(paths)
            if 'JPG' in f:
                JPGlist.append(paths)
            if '(' in f or ')' in f:
                parenthList.append(paths)
            if '|' in f or '/' in f or '?' in f or '[' in f or ']' in f or '"' in f or ':' in f or ';' in f or '<' in f or '>' in f or '%' in f or '^' in f or '@' in f or '#' in f or '$' in f or '{' in f or '}' in f or '~' in f or '=' in f:
                otherCharList.append(paths)
                    # Iterate over the files
        for paths in fileList:
            f = os.path.basename(paths)
            # Search for system files
            if f.startswith("."):
                systemFileList.append(paths)
            # Search for files with no extension    
            elif re.search("^[^.]+$", f):
                noExtList.append(paths)
            # Get a dictionary of file extensions and their frequencies
            elif re.search("^[^.]+\.[^.]+$", f):
                setExtMap(f)
                
                
            # Search for files with more than one extension
            else:
                doubleExtList.append(paths)
                setExtMap(f)
                
            # Search for duplicate filenames    
            if fileListName.count(f) > 1:
                dupFileList.append(paths)
            # Get the total filesize and search for empty files   
            filesize = os.path.getsize(paths)
            totalFilesize = totalFilesize + filesize
            if filesize == 0:
                emptyFileList.append(paths)
      
        # Change extension map into a string 
        for ext, noExt in extMap.items():
            if extStr != '':
                extStr = extStr + '  '
            extStr = extStr + ext[1:] + ': ' + str(noExt) 

        # Create logfile - add index on the end if it already exists
        d = datetime.date.today().strftime("%Y_%m_%d")
        outputFile = os.path.join(outputDir, 'output_' + d + '.log')
        i = 0 
        while os.path.exists(outputFile):
            i = i + 1
            outputFile = os.path.join(outputDir, 'output-' + str(i) + '_' + d + '.log')
        logfile = open(outputFile, mode='w')

        # Write ouput to file
        logfile.write(format('Date:', '<25') + datetime.datetime.now().strftime("%d/%m/%Y (%H:%M)") + '\n')
        logfile.write(format('Input Directory:', '<25') + path + '\n')
        logfile.write(format('Output File:', '<25') + outputFile + '\n')
        logfile.write(format('Directories:', '<25') + str(len(dirList)) + '\n')
        logfile.write(format('Files:', '<25') + str(len(fileList)) + '\n')
        logfile.write(format('Directories and Files:', '<25') + str(len(dirList) + len(fileList)) + '\n')
        logfile.write(format('Total Filesize:', '<25') + str("{:,}".format(totalFilesize)) + ' bytes\n')
        logfile.write(format('Extensions:', '<25') + extStr + '\n')
        displayReportText(spacesList, 'Spaces (includes folders) = ' + str(len(spacesList)))
        displayReportText(JPGlist, 'Uppercase JPG = ' + str(len(JPGlist)))
        displayReportText(ampList, 'Ampersands = ' + str(len(ampList)))
        displayReportText(plusList, 'Plus or Minus Signs = ' + str(len(plusList)))
        displayReportText(doubleExtList, 'Multiple Extensions (or Full Stop) = ' + str(len(doubleExtList)))
        displayReportText(noExtList, 'No Extension = ' + str(len(noExtList)))
        displayReportText(quoteList, 'Single Quotes = ' + str(len(quoteList)))
        displayReportText(commaList, 'Commas = ' + str(len(commaList)))
        displayReportText(parenthList, 'Parenthesis = ' + str(len(parenthList)))
        displayReportText(otherCharList, 'Other Characters = ' + str(len(otherCharList)))
        displayReportText(dupFileList, 'Duplicate Files = ' + str(len(dupFileList)))
        displayReportText(systemFileList, 'System Files = ' + str(len(systemFileList)))
        displayReportText(emptyFileList, 'Empty Files = ' + str(len(emptyFileList)))
                
        logfile.close()
        logfile = open(outputFile, 'r')
        logfileoutput = logfile.read()
        logfile.close()
        print(logfileoutput)
        os.startfile(str(outputFile))
        # os.system('"W:\\users\\jgg513\\ADS-Easy\\test\\output-11_2022_09_27.log"')  
                #     # output.write('\n'.join(filenames))
                #     output.write('\n')

                # with open("file_names.txt", "a+", encoding='utf-8') as output:
                #     output.write(''.join(dirpath).join(dirnames).join(filenames))
                #     # output.write('\n'.join(filenames))
                #     output.write('\n')
            
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

main_container = Frame(root)
main_container.grid()
main_container.columnconfigure(3, weight=1)

main_container.rowconfigure(3, weight=1)
# # # confiugures column 0 to stretch with a scaler of 1.
# main_container.columnconfigure(1, weight=1)
# main_container.columnconfigure(2, weight=1)
# main_container.columnconfigure(3, weight=1)
# # # confiugures row 0 to stretch with a scaler of 1.
# main_container.rowconfigure(1, weight=1)
# main_container.rowconfigure(2, weight=1)
# main_container.rowconfigure(3, weight=1)
# # # confiugures column 0 to stretch with a scaler of 1.
# main_container.columnconfigure(2, weight=1)
# # # confiugures row 0 to stretch with a scaler of 1.
# main_container.rowconfigure(2, weight=1)
root.resizable(False, False)


top_frame = Frame(main_container)
top_frame.grid(row=0,column=0)

top_left = Frame(main_container, bd=2)
top_left.grid(row=0, column=0, sticky='w')

top_right = Frame(main_container, bd=2)
top_right.grid(row=0, column=2, sticky='e')

top_centre = Frame(main_container, bd=2)
top_centre.grid(row=0, column=1)


myButton = Button(top_left, text="Select Directory To Check",
                  command=myClick, width=22)

myButton.grid(column=0, row=0, padx=5 ,pady=5, sticky='w')

myButton2 = Button(top_left,state=DISABLED, text="fix",
                   command=fix, width=22)
myButton2.grid(column=5, row=0, padx=50, pady=5, sticky='nsew')

var = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

c = Checkbutton(top_left, text="lowercase", variable=var).grid(
    column=1, row=0, padx=50, pady=5, sticky='nsew')

c = Checkbutton(top_left, text="lowercase extension", variable=var3).grid(
    column=3, row=0, padx=50, pady=5, sticky='nsew')

c2 = Checkbutton(top_left, text="subdir", variable=var2).grid(
    column=2, row=0, padx=50, pady=5, sticky='nsew')

c3 = Checkbutton(top_left, text=" or fix folders only if ticked", variable=var4).grid(
    column=4, row=0, padx=50, pady=5, sticky='nsew')    

centre_frame = Frame(main_container, bd=2)
centre_frame.grid(row=1, column=0)

bottom_leftframe = Frame(centre_frame, bd=2)
bottom_leftframe.grid(row=1, column=0, sticky='w')

bottom_rightframe = Frame(centre_frame, bd=2)
bottom_rightframe.grid(row=1, column=1, sticky='e')

footer = Frame(main_container, bd=2)
footer.grid(row=2, column=0, sticky='w')

footer_left = Frame(footer, bd=2)
footer_left.grid(row=0, column=0, sticky='w')


footer_right= Frame(footer, bd=2)
footer_right.grid(row=0, column=2, sticky='w')


# photo = PhotoImage(file = "icon.ico")
    
# printList = Button(footer_right, text="Print Current Directory Files",
#                   command=printFiles,width=22).grid(column=3, row=4,  padx=8, pady=5, sticky='e')

# # printList = Checkbutton(root, text="print list of names", variable=var2).grid(
# #     column=2, row=0, padx=5, pady=5, sticky='nsew')
printListSubDir = Button(footer_right, text="Print drectory info to textfile",
                command=printSubFiles,width=22).grid(column=2, row=4,  padx=8, pady=5, sticky='e')

infoLabel = Label(footer, text="*Note this textfile will appear in the selected directory"
                  ).grid(column=2, row=6,  padx=5, pady=5, sticky='e')

infoLabel2 = Label(footer, text="Blue = Files adhere, Red = Files do not match our policies, Green = New filenames"
                  ).grid(column=0, row=6,  padx=5, pady=5, sticky='w')


submitlabel = Label(bottom_leftframe, text="Files Submitted:").grid(row=0, column=0)
changedlabel = Label(bottom_rightframe, text="New file names:").grid(row=0, column=0)


# progress bar
my_progress = ttk.Progressbar(footer_left, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.grid(row=2, column=0,  sticky='w')

my_listbox2 = Listbox(bottom_rightframe,  width=70, height=15)
my_listbox2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
# my_scrollbar2 = Scrollbar(my_listbox2, orient=VERTICAL)
# my_scrollbar2.config(command = my_listbox2.yview)
# my_scrollbar2.pack(side=RIGHT, fill= Y)


my_listbox = Listbox(bottom_leftframe,  width=70, height=15)
my_listbox.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
# my_scrollbar = Scrollbar(my_listbox, orient=VERTICAL)
# my_scrollbar.config(command = my_listbox.yview)
# my_scrollbar.pack(side=RIGHT, fill= Y)


# myapp = MyApp(root)
root.mainloop()




# Would also like to thank all stack overflow results and github that helped create this