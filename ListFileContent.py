import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  myList =[]
  with open (filename) as file:
    fullname = os.path.join(directory,filename)
    print(fullname)
    if not os.path.isdir(fullname):
      myList.append(fullname)

  # Return the list of files in the new directory
  return myList

print(new_directory("PythonPrograms", "script.py"))