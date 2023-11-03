from PIL import Image
import numpy

def FileToImage(myFile,mySize):
    a=open(myFile).read()
    myArray=[int('0b'+a[i:i+8],2) for i in numpy.arange(0,len(a),8)]
    if (len(myArray)!=mySize[0]*mySize[1]):
        print("The image size and array don't seem to match")
        exit(1)
    im = Image.new('L', mySize)
    im.putdata(myArray)
    return im

def ImageToString(myFile):
    img=Image.open(myFile)
    img.show()
    (a,b)=img.size
    if (type(img.getpixel((2,2)))!=type(1)):
        print("Image must be monochrome")
        exit(1)
    myString=""
    for i in range(0,a):
        for j in range(0,b):
#            img.getpixel((i,j))
            myString=myString+str(numpy.binary_repr(img.getpixel((i,j)),width=8))
#            print(numpy.binary_repr(img.getpixel((i,j)),width=8))            
    return myString

#file needs to be a bunch of 1 and 0
img=FileToImage("toPrint3",(64, 64))
img.show()
myString=ImageToString("fix2.jpg")
print(myString)
exit(1)

