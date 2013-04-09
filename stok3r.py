#Stok3r is a batch processing script for Slic3r by Mark Benson - https://github.com/MarkJB
#
# Useage: stok3r.py -p|--path c:\path\to\stls -c|--config c:\path\to\slic3r\config.ini -a|--auto n
#
# where n = a delay in seconds
#
# also stok3r.py -h|--help
#
# Scans the current directory or path supplied for STL files, calls slic3r with slic3r defaults or settings
# specified in a config.ini files and slices any stl files found.
#
# Can be told to automatically scan for new stls every n seconds (default is 10).
# WARNING! When run with the -a|--auto flag stls will be deleted after slic3r completes.
# v0.01
#
# April 2013
#
# CCNC licence. All other rights reserved or some such...
#
# This thing is free. No support offered or implied unless I feel like it. No liability accepted if this thing goes mental and eats your cat (or files).
#
# TODO: Clean up and remove duplicated code
# 

# Import required functions
import os #listdir
import sys #command line args and exit
import subprocess #call executable
import time #sleep

# Process command line args

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

pathToScan = ""
configFile = ""
loadOption = ""
pathSeperator = "\\"
scanFlag = False
scanInterval = 10 #default scan interval in seconds
pathToSlic3r = "Z:\\Reprap\\Slic3r\\" #set the path to slic3r-console.exe if not already in your path variable

for i in range(1, len(sys.argv)):
   
   if str(sys.argv[i]) == "--config":
      configFile = str(sys.argv[(i+1)])
      #print "Input to --config = " + configFile
   
   if str(sys.argv[i]) == "-c":
      configFile = str(sys.argv[(i+1)])
      #print "Input to -c = " + configFile
   
   if str(sys.argv[i]) == "--path":
      pathToScan = str(sys.argv[(i+1)])
      #print "Input to --path = " + pathToScan
      
   if str(sys.argv[i]) == "-p":
      pathToScan = str(sys.argv[(i+1)])
      #print "Input to -p = " + pathToScan
      
   if str(sys.argv[i]) == "--auto":
      scanFlag = True
      #print "Number of args = " + str(len(sys.argv))
      if (len(sys.argv))%2 > 0:
         #print "Odd"
         scanInterval = sys.argv[(i+1)]
         #print "Interval value supplied is " + str(scanInterval)
      elif (len(sys.argv))%2 == 0:
         #print "Even"
         print "Scan interval value not suppled. Using default of " + str(scanInterval) + " seconds." 
      
   if str(sys.argv[i]) == "-a":
      scanFlag = True
      #print "Number of args = " + str(len(sys.argv))
      if (len(sys.argv))%2 > 0:
         #print "Odd"
         scanInterval = sys.argv[(i+1)]
         #print "Interval value supplied is " + str(scanInterval)
      elif (len(sys.argv))%2 == 0:
         #print "Even"
         print "Scan interval value not suppled. Using default of " + str(scanInterval) + " seconds." 
  
   if str(sys.argv[i]) == "--help":
      print "batchproc.py options"
      print ""
      print " -c|--config file     Slic3r generated config file to specify slic3r settings"
      print ""
      print " -p|--path path       Path to scan for stl files. Default is to scan current directory"
      print ""
      print " -a|--auto n          Automatically scan for and slice stl files every n seconds. Default is 10 seconds. Note: stls are deleted from the specified directory once they have been sliced."
      print ""
      print " -h|--help            Show this basic help file"
      print ""
      sys.exit()

   if str(sys.argv[i]) == "-h":
      print "batchproc.py options"
      print ""
      print " -c|--config file     Slic3r generated config file to specify slic3r settings"
      print ""
      print " -p|--path path       Path to scan for stl files. Default is to scan current directory"
      print ""
      print " -a|--auto n          Automatically scan for and slice stl files every n seconds. Default is 10 seconds. Note: stls are deleted from the specified directory once they have been sliced."
      print ""      
      print " -h|--help            Show this basic help file"
      print ""
      sys.exit()

# Set config file by arg or use slic3r defaults
if configFile == "":
   print ""
   print "Config file not supplied as command line argument - slic3r will use its defaults."
   print ""
elif configFile != "":
   #print "Config supplied: " + configFile
   loadOption = "--load"
   

# Get list of all content in the current directory
print pathToScan
if pathToScan == "":
   print ""
   print "Path to scan option not supplied - using current directory."
   print ""
   pathToScan = "."

directoryContent = os.listdir(pathToScan)

# Funtion to parse a list and return a list containing only stl file names
def checkExtension (inputList):
   stlFileList = []
   for i in range(0, len(inputList)):
      
      if inputList[i].endswith("stl"):
         stlFileList.append(inputList[i])
   return stlFileList

# Call funtion to check for stl files      
stlFileList = checkExtension(directoryContent)
#print stlFileList

# Call slic3r-console.exe

if scanFlag == False:
   
   numberOfFilesToSlice = len(stlFileList)
   if numberOfFilesToSlice > 0:
      #print str(numberOfFilesToSlice) + " files to slice"
      for i in range(0, numberOfFilesToSlice):
         print ""
         print str(numberOfFilesToSlice - int(i)) + " files left to slice"
         print ""
         #print "Command to execute: " + pathToSlic3r + "slic3r-console.exe " + pathToScan + pathSeperator + stlFileList[i] + " " + loadOption + " " + configFile 
         #print ""
         subprocess.call([pathToSlic3r + "slic3r-console.exe", pathToScan + pathSeperator + stlFileList[i], loadOption, configFile])
elif scanFlag == True:
   
   #Scan directory
   #Convert files if there are any
   #Delete stls after conversion
   #Start interval timer
   #Rinse and repeat
   
   while True:
      directoryContent = os.listdir(pathToScan)
      stlFileList = checkExtension(directoryContent)
      numberOfFilesToSlice = len(stlFileList)
      if numberOfFilesToSlice > 0:
         #print str(numberOfFilesToSlice) + " files to slice"
         for i in range(0, numberOfFilesToSlice):
            print ""
            print str(numberOfFilesToSlice - int(i)) + " files left to slice"
            print ""
            print "Command to execute: " + pathToSlic3r + "slic3r-console.exe " + pathToScan + pathSeperator + stlFileList[i] + " " + loadOption + " " + configFile 
            #print ""
            subprocess.call([pathToSlic3r + "slic3r-console.exe", pathToScan + pathSeperator + stlFileList[i], loadOption, configFile])
            #print "Delete file " + pathToScan + pathSeperator + stlFileList[i]
            #print ""
            try:
               os.remove(pathToScan + pathSeperator + stlFileList[i])
            except OSError, e:
               print "Files not found. Already deleted?"
               pass
               
      #print "Scanning directory again in " + scanInterval + " seconds"
      time.sleep(int(scanInterval))
      
