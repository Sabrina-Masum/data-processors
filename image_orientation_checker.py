
import cv2
import os
import pandas as pd
import glob


folder_path ='F2'


for image in os.listdir(folder_path) :
        os.listdir(folder_path)
        im  = cv2.imread(os.path.join (folder_path,image))
        h,w,c= im.shape
        
        if  w < h:
            potpath='Potrait Images'
            cv2.imwrite(os.path.join (potpath,image),im)
            pot_file_list = os.listdir('Potrait Images')
            df = pd.DataFrame(pot_file_list,columns={'Potrait'})
            

        elif w==h:
            sqpath='Square Images'
            cv2.imwrite(os.path.join (sqpath,image),im)
            sq_file_list = os.listdir('Square Images')
            df2 = pd.DataFrame(sq_file_list,columns={'Square'})
            
                
        else:
    
            landpath= 'Landscape Images'
            cv2.imwrite (os.path.join (landpath,image),im)
            land_file_list = os.listdir('Landscape Images')
            df3= pd.DataFrame(land_file_list, columns={'Landscape'})
            
           
            

print(df)  
print(df2) 
print(df3)

#col_names= ['potrait','land']
x= pd.concat([
   pd.concat([df, df2,df3], axis=1  )])

print(x)
   
x.to_csv('Orientation_Checker_CSV.csv' , index=False )

#print('Landscape' , land_file_list)       
#print('Potrait' , pot_file_list)    



                