import subprocess


#convert odt ot .zip & last line will convert it back to odt
subprocess.call("mv *.odt final.zip", shell=True)
subprocess.call('ls', shell=True)

#this part will extract 1 file from the .xml

subprocess.call("unzip -j final.zip content.xml", shell=True)
subprocess.call('ls', shell=True)
#this part edits the last content.xml file (from last line)
#i need it to read the file...

# creating a variable and storing the text
# that we want to search
#-------------------#
search_text = "xfg"
  
# creating a variable and storing the text
# that we want to add
replacement_text = "William Snatcher"
  
# Opening our text file in read only
# mode using the open() function
with open(r'content.xml', 'r') as file:
  
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
  
    # Searching and replacing the text
    # using the replace() function
    data = data.replace(search_text, replacement_text)
  
# Opening our text file in write only
# mode to write the replaced content
with open(r'content.xml', 'w') as file:
  
    # Writing the replaced data in our
    # text file
    file.write(data)
  
# Printing Text replaced
print("Text replaced")

#-----------------#
#read file then find and replace text in file and rewrite file?



#subpart finds /xfg && replaces the variable with x
#might automate the flags too so that i can make this part more accessible

#this part overwrites .xml in chosen zip file using zip -j *.zip content.xml

subprocess.call("sudo zip final.zip -oq content.xml -o", shell=True)
#final part turns .zip to .odt again

 
subprocess.call("sudo mv final.zip final.odt", shell=True)

