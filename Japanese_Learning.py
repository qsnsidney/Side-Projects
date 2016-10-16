'''
Section 1: Preparation
-- lists containing all the hanzi & duyin; keys of the dictionaries
-- dictionaries containing the complete information from the text files
-- A (nested) list working as a stack for the redo function; element in the format of [hanzi, duyin, indicator] 
'''

# Only duyin's list & dictionary will be generated at the beginning since it is easier to sort
listhanzi = []
dichanzi = {}
listduyin = []
dicduyin = {}

stack = []

f = open('duyin.txt', 'r')
for line in f:
    a = line.split()
    listduyin.append(a[0])
    dicduyin[a[0]] = a[1:]
    
'''    for hanzi in a[1:]:
        if i not in listhanzi:
            listhanzi.append(hanzi)'''

'''for i in listhanzi:
    # i is a hanzi
    for j in dichanzi(i):
        if j not in listduyin:
            listduyin.append(j)'''
        
#----------------------------------------------

'''
Section 2: Function Definition

'''


# Function 1: output the updated files of hanzi and duyin
def output(ld, dd):   
    f.close()
    ld.sort()
    # Generate the updated list (ordered) and dictionary (unordered) corresponding to hanzi
    for duyin in ld:
        dd[duyin].sort()
        for hanzi in dd[duyin]:
            if hanzi not in listhanzi:
                listhanzi.append(hanzi)
                dichanzi[hanzi] = [duyin]
            else: # if hanzi in listhanzi
                if duyin not in dichanzi[hanzi]:
                    dichanzi[hanzi].append(duyin)
                else: # if duyin in dichanzi[duyin]
                    pass
    
    f1 = open('hanzi.txt', 'w')
    f2 = open('duyin.txt', 'w')
    
    for duyin in ld:
        f2.write(duyin + '    ')
        for i in range(len(dd[duyin]) - 1):
            f2.write(dd[duyin][i] + '    ')
        f2.write(dd[duyin][-1] + '\n')
    f2.close()

    for hanzi in listhanzi:
        f1.write(hanzi + '    ')
        dichanzi[hanzi].sort()
        print(len(dichanzi[hanzi]))
        for j in range(len(dichanzi[hanzi]) - 1):
            print('aaaaa')
            f1.write(dichanzi[hanzi][j] + '    ')
        f1.write(dichanzi[hanzi][-1] + '\n')            
    f1.close()
 


#----------------------------------------------


# Function 2: give the unsorted, updated list and dictionary of duyin
def adding(ld, dd):
    while True:
        x = raw_input("***\ninput format: 汉字 读音 | q-quit, u-undo, r-remove\n***\n")
        # x = raw_input('input:\n')
        a = x.split()
        if x == 'q':    # quit
            output(ld, dd)
            return
        elif len(a) == 2: # normal adding operation
            hanzi = a[0]
            duyin = a[1]
            if duyin in ld:
                if hanzi not in dd[duyin]:
                    dd[duyin].append(hanzi)
                    a.append('h')
                    #add the hanzi to the existing duyin
                else:
                    a.append('n')
                    #do nothing
            else: #duyin not in ld
                ld.append(duyin)
                dd[duyin] = [hanzi]
                a.append('d')
                # add the duyin to list2 and add an entry to dic2
            stack.append(a)
        elif x == 'u':  # undo
            if len(stack) != 0:
                print(dd)
                u = stack.pop()
                print(u)
                if u[2] == 'n':
                    pass
                elif u[2] == 'h':
                    dd[u[1]].remove(u[0])
                else:
                    del dd[u[1]]
                    ld.remove(u[1])
            else:
                print('Nothing to undo')
        elif x == 'r':  # remove
            r = raw_input('###\nEnter the entry you want to remove\n###\n')
            rr = r.split()
            if len(rr) != 2:
                print('###\nINVALID INPUT\n###')
            elif rr[1] not in ld:
                print('Entry not exists')
            else:
                if rr[0] in dd[rr[1]]:
                    if len(dd[rr[1]]) == 1:
                        del dd[rr[1]]
                        ld.remove(rr[1])
                    else: 
                        dd[rr[1]].remove(rr[0])
                else:
                    print('Entry not exists')
        else:           # invalid input
            print('###\nINVALID INPUT\n###')


#--------------------------------------

'''
Section 3: Main Program
'''
adding(listduyin, dicduyin)

'''
f1.close()

listduyin.sort()


# Generate the updated list (ordered) and dictionary (unordered) corresponding to hanzi
for duyin in listduyin:
    dicduyin[duyin].sort()
    for hanzi in dicduyin[duyin]:
        if hanzi not in listhazi:
            listhanzi.append(hanzi)
            dichanzi[hanzi] = [duyin]
        else: # if hanzi in listhanzi
            if duyin not in dichanzi[duyin]:
                dichanzi[duyin].append(duyin)
            else: # if duyin in dichanzi[duyin]
                pass
'''
