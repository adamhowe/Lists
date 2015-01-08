



def search(searchList,numbers):
    found = False
    counter = 0
    while not found and counter < len(numbers):
        if numbers[counter] == searchList:
            found = True
        else:
            counter = counter + 1
    return found
            
                    

#Main Program   
numbers = ["one","two","three","four","five"]
searchList = input("Search: ")
searchList= searchList.lower()
found = search(searchList,numbers)


if found:
    print("Found")
else:
    print("Not Found")
