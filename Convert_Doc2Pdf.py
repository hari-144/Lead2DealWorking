import sys
import os
import shutil
import comtypes.client
wdFormatPDF = 17

files_path = r"C:\Users\hrudh\Documents\Lead2DealWorking\Text-Annotator"
process_pdfs_path = r"C:\Users\hrudh\Documents\Lead2DealWorking\processed_files"

if not os.path.exists(files_path):
        os.makedirs(files_path)
           
if not os.path.exists(process_pdfs_path):
        os.makedirs(process_pdfs_path)
       
os.chdir(files_path)
os.getcwd()

word = comtypes.client.CreateObject('Word.Application')

for current_dir, dirs, files in  os.walk('.'):
    for file in files:
        fileName,FileExtn = os.path.splitext(file)
        if FileExtn == ".pdf":           

            shutil.copy(files_path+"\\"+file,process_pdfs_path+"\\"+file)

        elif FileExtn.startswith(".doc"):            
            in_file =  files_path+"\\"+file
            out_file = process_pdfs_path+"\\"+fileName+".pdf"
            doc = word.Documents.Open(in_file)
            doc.SaveAs(out_file, FileFormat=wdFormatPDF)
            doc.Close()
word.Quit()            

# from pdf2image import convert_from_path
# os.chdir(process_pdfs_path)
# os.getcwd()

# for current_dir, dirs, files in  os.walk('.'):
#     for file in files:
#         images = convert_from_path(process_pdfs_path+"\\"+file,poppler_path = r"C:\Users\Poppler\poppler-0.68.0_x86\poppler-0.68.0\bin")
#         fileName = os.path.splitext(file)[0]
#         for i in range(len(images)):  
#             # Save pages as images in the pdf
#             if not os.path.exists(images_path+"\\"+fileName):
#                 os.makedirs(images_path+"\\"+fileName) 
#             images[i].save(images_path+"\\"+fileName+'\\page'+ str(i+1) +'.jpg', 'JPEG')
