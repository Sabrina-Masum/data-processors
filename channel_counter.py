import cv2
import os
folder_path ='F2'
initial_count = 0

for image in os.listdir(folder_path) :
  os.listdir(folder_path)
  im  = cv2.imread(os.path.join (folder_path,image))
 
  #print(im)
  if im.any() != None:
   if(len(im.shape)<2):
     initial_count += 1  
     print('Total Number of grayscale images :' ,initial_count) 
   elif len(im.shape)==3:
         initial_count += 1
         
       
   else:
     print("other")

print ('Total Number of 3-channel images :' , initial_count) 



   
  
        

