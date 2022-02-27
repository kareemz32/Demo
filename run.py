import google_images_download
import retrain
import os #runs commands on command line
import shutil #for removing directories with items in it

#Deletes the trainingdataset
path = "trainingdataset"
if(os.path.isdir(path)):
	shutil.rmtree(path)

#Creates an empty trainingdataset
os.mkdir(path)

#Asks user what they'd like to compare
print("What 2 things are you trying to learn?")
print("Hit enter after each object.")
x = input()
y = input()

os.system('python google_images_download.py --keywords \"' + x + '\" --limit 30  -o \"trainingdataset\"')
os.system('python google_images_download.py --keywords \"' + y + '\" --limit 30  -o \"trainingdataset\"')

#Creates 2 folder of the items in the trainingdataset folder
os.system('python google_images_download.py --keywords \"' + x + '\" --limit 30  -o \"trainingdataset\"')
os.system('python google_images_download.py --keywords \"' + y + '\" --limit 30  -o \"trainingdataset\"')
#Runs the program to learn what they are
os.system("bash train.sh")
print("Please chose an image you'd like to indentify.")

#Identifies the image.
os.system("python classify.py");

