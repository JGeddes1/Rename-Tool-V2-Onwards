import os
import pandas as pd


path = "W:\\users\\jgg513\\test\\paths"
files = os.listdir(path)



for eachfile in files:
    if eachfile.endswith(".xlsx"):
        cleanfilename =eachfile.replace(".xlsx", "")
        xlfile = pd.ExcelFile(os.path.join(path,eachfile))
        sheets = xlfile.sheet_names
        for eachsheet in sheets:
            sheetdata = xlfile.parse(eachsheet)
            csvname = cleanfilename + "-" + eachsheet + ".csv"
            sheetdata.to_csv(csvname, index = False)
