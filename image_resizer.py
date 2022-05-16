# Import Libraries
from inspect import ArgSpec
import cv2 
import glob 
import argparse
import os

#z = input("Enter your existing file format")
#print("Existing format is: " + z)


#format = input("Enter format:")
#print("Format is: " + format)


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)



parser = argparse.ArgumentParser( )
#parser.add_argument('--path', type=dir_path)

parser.add_argument('--input_path', type=dir_path)
parser.add_argument('--output_path', type=dir_path)
parser.add_argument('--input_format', type= str)
parser.add_argument('--output_format', type=str)

subparser = parser.add_subparsers(dest='command')
scale = subparser.add_parser('scale')
dsize = subparser.add_parser('dsize')

scale.add_argument('--scale_percent' , type=int)
dsize.add_argument('--height' , type=int)
dsize.add_argument('--width' , type=int)



args = parser.parse_args()



dir='F2'

for file in glob.glob( args.input_path + '/*.'+ args.input_format):

    im = cv2.imread(file) 
    

    x= file.rsplit(".",1)[0]
    #print(x)
    #y= len (dir)
    y=( x[2:])
    print(y)
     
    
      
    parser = argparse.ArgumentParser()
    


    #args.parser.parse_args()

    if args.command == 'scale':
           print('Enter scale percent:', args.scale_percent) 
           
           width = int(im.shape[1] * args.scale_percent / 100)
           height = int(im.shape[0] * args.scale_percent / 100) 
           dimension = (width, height)
           output = cv2.resize(im,dimension)
           
    elif args.command == 'dsize':
          print('Enter height and width', args.height, args.width)
          dim = (args.width,args.height)
          output = cv2.resize(im,dim)
    
          
        
    cv2.imwrite ( args.output_path + y + '.' + args.output_format, output) 



 
