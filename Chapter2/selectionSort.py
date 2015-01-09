# Chapter 2
# Selection Sort Implementation
# Designed rigorously based on the pseudo-code
# With additions for properly formatted output
# Can be used as stand alone or called by importing and passing a list
# Made by V3rG1L, hope it helps you :)

# Uses the same format as Insertion sort algorithm since it looks pretty and I do not want to re-create code unnecessarily

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
    print("Given array is as follows:")
    pp(l)
    pc("Now we sort it using Selection Sort.")
    if len(l) == 1:
        pc("Array of size 1 is already sorted")
        pp(l)
        return
    pc("Length of array is: " + str(len(l)))
    for i in range(0, len(l)-1):
        key = i
        pc("Smallest element at start of this iteration is : " + str(l[key]) + " at position " + str(i))
        pc("Now we find the smallest element in rest of array and swap it with the key")
        for j in range(i, len(l)):
            if l[j] < l[key]:
                key = j
        pc("Now swapping \'" + str(l[i]) + "\' at pos " + str(i) + " with \'" + str(l[key]) + "\' at pos " + str(key))
        l[key], l[i] = l[i], l[key]
        pc("Array is not sorted upto position " + str(i))
        pp(l)
    print("Full array is now sorted:")
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
    printComments=True
    main()
