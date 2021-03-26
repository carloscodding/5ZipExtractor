from zipfile import ZipFile

import time 

from tqdm import tqdm 

import os

print("Welcome To 5Zip Extractor")

print("*******************************")
print("Contacts")
print("Discord: _carlos#8479")

print("******************************")

def zipextractor():
  
  zipname = os.listdir("input")
  
  
  for x in zipname:
    
    if ".zip" in x:
      with ZipFile("input//" + x,"r") as zip:
        
        # Extract
        
        print("Extracting " + x)
      
        try:
          os.mkdir("output//" + x.replace(".zip",""))
        
        except:
          
          zip.extractall("output//" + x.replace(".zip",""))
          
          print("Extracted With Sucess")
        
        

zipextractor()
