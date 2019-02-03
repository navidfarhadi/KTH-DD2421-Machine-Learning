import monkdata as m
import dtree

def main():
    print("Assignment 1: ")
    print("MONK-1: " + str(dtree.entropy(m.monk1)))
    print("MONK-2: " + str(dtree.entropy(m.monk2)))
    print("MONK-3: " + str(dtree.entropy(m.monk3)))

    print("\n" + "Assignment 3: ")
    print("MONK-1: ")
    for i in range(6):
        print(str(dtree.averageGain(m.monk1,m.attributes[i])))
    
    print("MONK-2: ")
    for i in range(6):
        print(str(dtree.averageGain(m.monk2,m.attributes[i])))

    print("MONK-3: ")
    for i in range(6):
        print(str(dtree.averageGain(m.monk3,m.attributes[i])))

    print("\n" + "Assignment 5: ")
    print("MONK-1: ")
    monk1tree=dtree.buildTree(m.monk1, m.attributes)
    print(dtree.check(monk1tree, m.monk1))
    print(dtree.check(monk1tree, m.monk1test))

    print("MONK-2: ")
    monk2tree=dtree.buildTree(m.monk2, m.attributes)
    print(dtree.check(monk2tree, m.monk2))
    print(dtree.check(monk2tree, m.monk2test))

    print("MONK-3: ")
    monk3tree=dtree.buildTree(m.monk3, m.attributes)
    print(dtree.check(monk3tree, m.monk3))
    print(dtree.check(monk3tree, m.monk3test))

if __name__ == "__main__":
    main()