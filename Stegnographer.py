from PIL import Image
import stepic
def encoder():
    x=input("Enter the name of the image you want to open(with extension):")
    y=input("Enter the text you want to input:")
    z=input("Enter the name of output file(without extension):")
    y=y.encode("ascii")
    open1=Image.open(x)
    modify= stepic.encode(open1,y)
    modify.save(z+".png")
    print("Success")
def decoder():
    p=input("Enter the name of the file you want to decode(without extension):")
    p+=".png"
    open2= Image.open(p)
    decoded=stepic.decode(open2)
    print("Decoded text from the image:",decoded,"\n")
while True:
    print("Welcome to Python Stegonography")
    print("Please choose from the following options: \n 1.Encode Data \n 2.Decode Data \n 3.Exit")
    ant=int(input("Enter your choice:"))
    if ant==1:
        encoder()
    if ant==2:
        decoder()
    if ant>=3:
        print("Thank you for using the Stegnographer!")
        break