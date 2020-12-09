
def vector_implementation():
    a = [1,2,3]
    print(len(a))
    if not []:
        print("empty list")
    a.append(4)
    print(a)
    a.insert(1, 11)
    print(a)
    a.insert(0,0)  # prepend
    print(a)
    print(a.pop())
    print(a)
    a.remove(0)  # delete
    print(a)
    a = [x for x in a if x != 11]  # remove (by value)
    print(a)
    print(a.index(2))  # find

if __name__ == "__main__":
    vector_implementation()