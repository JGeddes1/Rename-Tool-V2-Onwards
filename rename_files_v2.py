
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
from array import array

# Array that gets unique filenames put in for checking later on in code
unique_List = []

global count
global  noChangeLabel
global length
global listfiles
global list_all 
#list all used in the log sheet section 
list_all =unique_List

# print(str(list_all)+'THIS IS LIST ALL')
# setting up the root Tkinter 
root = Tk()

# Title of the Application Goes along top bar
root.title('ADS Rename Files Tool (Made By Jamie Geddes)')
i = 0
y = 0
global path
filecounter = 0
filecounter2 = 0

#Overall Function when select directory is clicked to do all the initial find directory and scan stuff
def myClick():

    # Initial variables in the function for scanning mainly
    #Sets the fix button to off initially
    myButton2['state'] = 'disabled'
    unique_List = []
    

# Find directory Function
    def findDir():
        global path # set global path for all future calls
        global currentDirectoryLabel # set current directory value
        path = filedialog.askdirectory(master='', initialdir='', title="Select your Source directory", mustexist=True)
        currentDirectoryLabel = Label(footer, text="Current Working Directory:")# resets text                                                                                                                                                                                    ").grid(column=0, row=7, padx=5, pady=5, sticky='w')
        currentDirectoryLabel = Label(footer, text="Current Working Directory: " + path).grid(column=0, row=7, padx=5, pady=5, sticky='w') # prints current dir + path
        
        
        
        #print('OPOP' + str(path))
        #If path is none or blank it pops up error and returns the path of none for further use
        if path == None or path == '':
            messagebox.showwarning('Error', 'No path selected, resetting..')

            # sys.exit("Error message")
            return path
        else:
            
            return path
        
    # Initialise function
    findDir()
    

    
    
    
    # make list blank each time click is run
    my_listbox.delete(0, END)
    my_listbox2.delete(0, END)
    # check directory
    # retval = os.getcwd()
    if path == '':
        return False
    print("Directory changed successfully %s" % path)  #check directory changed
    # Passes arguments of all the file paths
    parser = argparse.ArgumentParser(
        description="Rename all files in directory by replacing whitespace with underscores.")
    parser.add_argument('directories', metavar="DIR", nargs='*',
                        default=[path], help="directories to walk. Default: asks")
    err = sys.stderr.write
    # Testing out filenames counter for going into list box
    global numberFilesAlreadyGone
    global numberFilesAlreadyGone2
    numberFilesAlreadyGone = -1
    numberFilesAlreadyGone2 = -1

    def new_names(filenames):
        global numberFilesAlreadyGone
        global numberFilesAlreadyGone2
         
        
        # Generate new filenames for the given filenames
        
        # print(filenames)
        filelength = len(filenames)
        
        my_progress['value'] =50
        root.update_idletasks()
        time.sleep(0.02)
    
       # --FILENAME SCAN AND WHAT WOULD NEED TO REPLACE SECTION START --

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
        
   
        if var.get() == 1:
            
            # Alphabet For lowercase
            filenames_new = (re.sub('', '',  fn.lower()) for fn in filenames_new)

        if var3.get()==1:
            
            
            filenames_new = (re.sub('.JPG', '.jpg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.JPEG', '.jpeg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSV', '.csv',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.SHP', '.shp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.HTML', '.html',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIFF', '.tiff',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TXT', '.txt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PNG', '.png',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIF', '.tif',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.BMP', '.bmp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.RTF', '.rtf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOCX', '.docx',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOC', '.doc',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODT', '.odt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XLS', '.xls',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PDF', '.pdf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODS', '.ods',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.E57', '.e57',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.OBJ', '.obj',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DWG', '.dwg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DXF', '.dxf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSS', '.css',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XSD', '.xsd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XML', '.xml',  fn) for fn in filenames_new)


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

                # Merge consecutive hyphen and underscores after for aesthetics
        filenames_new = [re.sub('-_', '-', fn) for fn in filenames_new]
        

        # print('This is filenames array checker' + str(filenames))
        # print('This is filenames_new array checker' + str(filenames_new))

        # --FILENAME SCAN SECTION END --
        
        # Have to figure out how to add to array on each loop if want unique across folderpaths currently only works with chosen directory and not sub directories
        # Potentially create a if unique_list.length = filenames_new.length then put uniquelist into a global array? my_list = list(set(my_list))
        global list_all
        global duplicate_List
        list_all = []
        duplicate_List =[]
        for file in filenames_new:
            # UNQIUE LIST SECTION FOR LOG AND CHECKER
            if file not in unique_List:
                unique_List.append(file)
                # print('this is unique list'+str(unique_List))  
                list_all =unique_List 
                # print("This is list_all" + str(list_all))
            else:
                 duplicate_List.append(file)
        
        countDuplicate_List = len(duplicate_List)
        # IF COUNT DUPLICATE IS GREATER 0 IT WILL ALERT THERE IS DUPLICATES
        if countDuplicate_List > 0:
            messagebox.showinfo(title='Alert', message="Duplicate filenames when fix will take place please rename the following files before continuing " + str(duplicate_List))
        
        # IF NOT A CHANGE NEEDED
        noChangeLabel = Label(main_container, text="No Changes needed")
        noChangeLabel.grid(row=3, column=0)

        if noChangeLabel.winfo_exists() == 1:
            if filenames_new != filenames:
                noChangeLabel.destroy()
        noChangeLabel.destroy()    
        if filenames_new != filenames:
            # ACTIVATED BUTTON TO FIX IF FILENAMES DONT MATCH
            myButton2['state'] = 'normal'
            # ---LIST BOX INSERT SECTION --
            for i in range(0, filelength):
                    
                    numberFilesAlreadyGone2 = numberFilesAlreadyGone2 + 1
                    # print("filenames new:", i, ":", filenames_new[i])
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
                    
            # ---LIST BOX INSERT SECTION END --
        # IF FILENAMES ORIGINAL DONT HAVE TO CHANGE
        if filenames == filenames_new :

            global count
            
        
            # for f in filenames:
            #     filecounter + 1
            #     if var4.get() ==1:
            #         if "." not in filenames[filecounter]:
            #             print("This is no change"+str(noChangeLabel.winfo_exists))
        
            # LIST BOX INSERT SECTION IF SAME NAMES
            if var4.get() ==0:
                for i in range(0, filelength):

                    numberFilesAlreadyGone2 = numberFilesAlreadyGone2 + 1
                    # print("filenames new:", i, ":", filenames_new[i])
                    my_listbox2.insert(numberFilesAlreadyGone2, filenames_new[i] + ' ' + str(numberFilesAlreadyGone2))
                    my_listbox.insert(numberFilesAlreadyGone2, filenames[i] + ' ' + str(numberFilesAlreadyGone2))
                    my_listbox2.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                    my_listbox.itemconfig(numberFilesAlreadyGone2, {'fg': 'blue'})
                    

                    if (i % 2) == 0:
                        my_listbox2.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})
                        my_listbox.itemconfig(numberFilesAlreadyGone2, {'bg': '#f5f5f5'})
                    numberFilesAlreadyGone = numberFilesAlreadyGone + 1
                    count = numberFilesAlreadyGone
            # LIST BOX INSERT SECTION END
            # x = 15
            # if x == 123:
            #     for i in range(0, len(filenames)):
            #         if filenames_new[i] != filenames[i]:

            #             print("filenames change", i, ":", filenames_new[i])

            #     return filenames_new
            # else:
            #     print("Please Redo Entry")
        my_progress['value'] =100 #SETS THE PROGRESS BAR TO BE FULL AFTER EACH SCANNED FILE
        root.update_idletasks()
        time.sleep(0.02) #INBETWEEN TIME FOR PROGRESS BAR
        #CHECKING SORTED 
        # if sorted(filenames) == sorted(filenames_new):
            
        #     print(sorted(filenames))
        #     print(sorted(filenames_new))
        
        # Scan subdirectory checked will return filenames_new here instead of before so doesnt scan sub unless ticked
        if var2.get() == 1:
            
            return filenames_new
        
            
    def rename_files_in_dir(dir):
        """
        Actually Walks to a directory and rename all files in the path with the filename changes done prior.
        """
        
        
        for (dirpath,dirnames, filenames) in os.walk(dir):
            i = 0
            if var4.get() ==1:   
                rename_folders(dir)            
            # Rename the filenames
            filenames_new = new_names(filenames)

            for f_old, f_new in zip(filenames, filenames_new):
                
                f_old = os.path.join(dirpath, f_old)
                f_new = os.path.join(dirpath, f_new)

                if f_old == f_new:
                    
                    continue


    def rename_folders(dir):
            
            
                for(dirpath,dirnames, filenames) in os.walk(dir):


                    # Rename the directories, and modify dirnames in place to aid os.walk
                    dirnames_new = new_names(dirnames) # sends the directory names off to the new names function and runs so appears on listbox but could change
                    for d_old, d_new in zip(dirnames, dirnames_new):

                        d_old = os.path.join(dirpath, d_old)
                        d_new = os.path.join(dirpath, d_new)

                        if d_old == d_new:
                            continue

                    del dirnames[:]
                    dirnames.extend(dirnames_new)

    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]
    
        for d in dirs:
            rename_files_in_dir(d)

# FIX FUNCTION BEGINS AFTER CHECKS HERE IF BUTTON IS CLICKED
# Is mainly a code repition but with teh ability to actually allow filenames to be renamed in the directory not stopped
def fix():

    os.chdir(path)
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
        
        
        # print(filenames[0])
        for i in range(0, len(filenames)):
            print("filenames original list", i, ":", filenames[i])


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
        

        if var.get() == 1:
            # Alphabet For lowercase
            filenames_new = (re.sub('', '',  fn.lower()) for fn in filenames_new)

            # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('([.](?![A-Za-z0-9]+$))', '-',  fn)
                        for fn in filenames_new)

        if var3.get()==1:
            filenames_new = (re.sub('.JPG', '.jpg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.JPEG', '.jpeg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSV', '.csv',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.SHP', '.shp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.HTML', '.html',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIFF', '.tiff',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TXT', '.txt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PNG', '.png',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.TIF', '.tif',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.BMP', '.bmp',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.RTF', '.rtf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOCX', '.docx',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DOC', '.doc',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODT', '.odt',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XLS', '.xls',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.PDF', '.pdf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.ODS', '.ods',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.E57', '.e57',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.OBJ', '.obj',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DWG', '.dwg',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.DXF', '.dxf',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.CSS', '.css',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XSD', '.xsd',  fn) for fn in filenames_new)
            filenames_new = (re.sub('.XML', '.xml',  fn) for fn in filenames_new)


        # if var4.get() ==1:
        #     dirList = []
        #     for (dirpath, dirnames, filenames) in os.walk(dir):
        #         for d in dirnames:
        #             dirList.append(os.path.join(dirpath, d))
        #     return
            
        # Erase non-alphanumeric-period-underscore characters:
        filenames_new = (re.sub('[^a-zA-Z0-9._-]', '',  fn)
                         for fn in filenames_new)

        filenames_new = (re.sub('\-shp.xml', '.shp.xml', fn)
                        for fn in filenames_new)
        
        # Merge underscores after hyphen for aesthetics
        filenames_new = [re.sub(' - ', '-', fn) for fn in filenames_new]

        # Merge consecutive underscores for aesthetics
        filenames_new = [re.sub('_+', '_', fn) for fn in filenames_new]

        # Merge consecutive hyphen and underscores after for aesthetics
        filenames_new = [re.sub('-_', '-', fn) for fn in filenames_new]

        if filenames_new != filenames:
        
            for i in range(0, len(filenames)):
                if filenames_new[i] != filenames[i]:
                        print("filenames change list", i, ":", filenames_new[i])
                        return filenames_new
        
        # if sorted(filenames) == sorted(filenames_new):
        #     print(sorted(filenames))
        #     print(sorted(filenames_new))
            
        if var2.get() == 1:
            my_progress.stop()
            return filenames_new
        if var4.get() == 1:
            my_progress.stop()
            return filenames_new

        return filenames_new
    
    def rename_files_in_dir(dir):
        """
        Walk a directory and rename all files in the path.
        """
        if var2.get() == 0:
            for (dirpath, dirnames, filenames) in os.walk(dir):
           
                # Rename the filenames
                if var4.get() == 1:
                    files = [f for f in os.listdir('.') if os.path.isfile(f)]
                    filenames_new = new_names(files)
                
                filenames_new = new_names(os.listdir(dir))
                if not filenames_new:
                    print("Subdirectory renaming skipped.")
                    return
                # list_length = len(filenames_new)
                # oglist_length = len(filenames)
                for f_old, f_new in zip(os.listdir(dir), filenames_new):

                    f_old = os.path.join(dir, f_old)
                    f_new = os.path.join(dir, f_new)

                    print("Hello this is the fnew thing"+f_new)
                    print("This is the filenames_new thing 0 array:")

                    if f_old == f_new:

                        continue

                    err("Renaming %s to %s\n" %
                        (os.path.abspath(f_old), os.path.abspath(f_new)))
                    shutil.move(f_old, f_new)
        else:


            for (dirpath, dirnames, filenames) in os.walk(dir):
                i = 0

                # Rename the filenames
                filenames_new = new_names(filenames)
                
                if not filenames_new:
                    print("Subdirectory renaming skipped.")
                    return
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
        if var4.get() ==1:
            rename_dir(dir)
        messagebox.showinfo(
        "Fixed issues", "We Have Fixed Incorrect Files")
        myButton2['state'] = 'disabled'
    
    
    def rename_dir(dir):
        for (dirpath, dirnames, filenames) in os.walk(dir):
           
                
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

def printSubFiles():
    os.chdir(path)
    retval = os.getcwd()


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
        removalExcessiveChar = []
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
        documentation = []
        noExtList = []
        JPGlist=[]
        paths = os.listdir(dir)

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
            if  re.search(r'-_', f):
                removalExcessiveChar.append(paths)
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
            string_to_match='documentation'
            if string_to_match in paths:
                documentation.append(f)
                print('blargs')
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
        
        # logfile.write(format('Documentation files:', '<25') + str(len(documentation)) + '\n')
        displayReportText(documentation, 'Documentation Files = ' + str(len(documentation)))
        displayReportText(list_all, 'Files Overall = ' + str(len(list_all)))
        # displayReportText(duplicate_List, 'Duplicate Files = ' + str(len(duplicate_List)))
        displayReportText(spacesList, 'Spaces (includes folders) = ' + str(len(spacesList)))
        displayReportText(JPGlist, 'Uppercase JPG = ' + str(len(JPGlist)))
        displayReportText(removalExcessiveChar, 'Removal of -_ for readability = ' + str(len(removalExcessiveChar)))
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

        
    if __name__ == '__main__':
        args = parser.parse_args()
        dirs = [os.path.abspath(d) for d in args.directories]

        for d in dirs:


            print_files_in_directory(d)

    
    return
# --GUI SECTION CREATION BEGIN--
main_container = Frame(root)
main_container.grid()
main_container.columnconfigure(3, weight=1)
main_container.rowconfigure(3, weight=1)
root.resizable(False, False)

top_frame = Frame(main_container)
top_frame.grid(row=0,column=0)

top_left = Frame(main_container, bd=2)
top_left.grid(row=0, column=0, sticky='w')

top_right = Frame(main_container, bd=2)
top_right.grid(row=0, column=2, sticky='e')

top_centre = Frame(main_container, bd=2)
top_centre.grid(row=0, column=1)

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

# --GUI SECTION CREATION END--

# --BUTTONS START--
myButton = Button(top_left, text="Select Directory To Check",
                command=myClick, width=22)

myButton.grid(column=0, row=0, padx=5 ,pady=5, sticky='w')

myButton2 = Button(top_left,state=DISABLED, text="fix",
                command=fix, width=22)
myButton2.grid(column=5, row=0, padx=50, pady=5, sticky='nsew')


printListSubDir = Button(footer_right, text="Print directory info to textfile",
                command=printSubFiles,width=22).grid(column=2, row=4,  padx=8, pady=5, sticky='e')
# --BUTTONS END--
# TICK BOX START
var = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

c = Checkbutton(top_left, text="Lowercase all", variable=var).grid(
    column=1, row=0, padx=50, pady=5, sticky='nsew')

c = Checkbutton(top_left, text="Lowercase extension", variable=var3).grid(
    column=3, row=0, padx=50, pady=5, sticky='nsew')

c2 = Checkbutton(top_left, text="Scan subdir", variable=var2).grid(
    column=2, row=0, padx=50, pady=5, sticky='nsew')

c3 = Checkbutton(top_left, text="Scan to Fix Folders in Directory (only works with subdir ticked too)", variable=var4).grid(
    column=4, row=0, padx=50, pady=5, sticky='nsew')    
# TICK BOX END 



# LABELS

infoLabel = Label(footer, text="*Note this textfile will appear in the selected directory"
                ).grid(column=2, row=6,  padx=5, pady=5, sticky='e')

infoLabel2 = Label(footer, text="Blue = Files adhere, Red = Files do not match our policies, Green = New filenames"
                ).grid(column=0, row=6,  padx=5, pady=5, sticky='w')


submitlabel = Label(bottom_leftframe, text="Files Submitted:").grid(row=0, column=0)
changedlabel = Label(bottom_rightframe, text="New file names:").grid(row=0, column=0)


# progress bar
my_progress = ttk.Progressbar(footer_left, orient=HORIZONTAL, length=500, mode='determinate')
my_progress.grid(row=2, column=0,  sticky='w')

# LIST BOXES
my_listbox2 = Listbox(bottom_rightframe,  width=70, height=15)
my_listbox2.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')



my_listbox = Listbox(bottom_leftframe,  width=70, height=15)
my_listbox.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

root.mainloop()




# Would also like to thank all stack overflow results and github that helped create this