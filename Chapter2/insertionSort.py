# Chapter 2
# Insertion Sort Implementation
# Designed rigorously based on the pseudo-code
# With additions for properly formatted output
# Can be used as stand alone or called by importing and passing a list
# Made by V3rG1L, hope it helps you :)

global printComments
printComments = False

def pp(li):
    for i in li:
        print(str(i)+" ",  end='')
    print()

def pc(ln):
    if printComments:
        print(ln)

def sort(l):
    pc("Given array is as follows:")
    pp(l)
    pc("Now we sort it using Iteration Sort.")
    if len(l) == 1:
        pc("Array of size 1 is already sorted")
        pp(l)
        return
    pc("Length of array is: " + str(len(l)))
    for j in range(1, len(l)):
        key = l[j]
        pc("Key is: " + str(key) + " at position " + str(j))
        i = j - 1
        pc("Now we move the key leftward until the partial array is sorted")
        while i >= 0 and l[i] > key:
            pc("Now moving \'" + str(l[i]) + "\' at pos " + str(i) + " to pos " + str(i+1))
            l[i+1] = l[i]
            i = i - 1
        l[i+1] = key
        pc("Partial array is now sorted: ")
        if printComments:
            pp(l)
    pc("Full array is now sorted:")
    pp(l)

def main():
    li=[]
    li.append(31)
    li.append(41)
    li.append(59)
    li.append(26)
    li.append(41)
    li.append(58)
    sort(li)

if __name__ == "__main__":
    global printComments
    printComments=True
    main()
