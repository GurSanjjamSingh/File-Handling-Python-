def createFile(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        print(f"File '{filename}' created with content: {content}")

def replaceStr(filename, oldstring, newstring):
    try:
        with open(filename, 'r') as f:
            content = f.read()

            if oldstring in content:
                newContent = content.replace(oldstring, newstring)

                with open(filename, 'w') as f:
                    f.write(newContent)
                    print(f"String '{oldstring}' replaced with '{newstring}' in '{filename}'.")

    except FileNotFoundError:
        print(f"File {filename} is Missing")
        choice = input(("Do you Want to create a file? (y/n): "))
        if choice.lower() == "y":
            content = input("What do you want to write in the file? : ")
            createFile(filename, content)
            replaceStr(filename, oldstring, newstring)
        else:
            print("Exiting...")

# MAIN
filename = input("Enter text file name: ") + ".txt"
print("File name: ", filename)
oldstring = input("Enter string to replace: ")
print("Old string: ", oldstring)
newstring = input("Enter string to replace with: ")
print("New string: ",newstring)
replaceStr(filename, oldstring, newstring)

