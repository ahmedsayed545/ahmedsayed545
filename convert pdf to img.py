poppler_path=r"C:\Users\ahmed\Downloads\New folder\Release-22.04.0-0\poppler-22.04.0\Library\bin"

pdf_path = r"D:\certifiaction\freelancing.pdf"

from pdf2image import convert_from_path
pages=convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)

import os 

saving_folder=r"D:\certifiaction"
c=1
for page in pages:
   img_name=f"img-{c}.png"
   page.save(os.path.join(saving_folder,img_name),"png")
   c+=1 
    