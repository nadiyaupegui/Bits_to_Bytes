#from class
def bits_to_bytes(bitstr):
    s = i = 0 #Declares s to be 00000000
    for b in bitstr: 
        s = (s >> 1) | (0, 0x80)[b] #Shift S to the right one it, and or it
                                    #with either 0 (if b is 0) or 0x80(if b is 1)
        i += 1 
        if i == 8:
            yield s #yeild the byte when there are 8 bits
            s = i = 0 #reset s to 0 for the next sequence of bits in s

    while i < 8:
        s >> 1
        i += 1
        yield s



#trying other things
def temp(bitstr):
    s = i = 0 #Declares s to be 00000000
    for b in bitstr: 
        s = (s >> 1) | (0, 0x80)[b] #Shift S to the right one it, and or it
                                    #with either 0 (if b is 0) or 0x80(if b is 1)
        i += 1 
        if i == 8:
            print(bin(int(s))) #trying to see what is being yielded
            s = i = 0 #reset s to 0 for the next sequence of bits in s

    while i < 8:
        s >> 1
        i += 1
        print(bin(int(s))) #trying to see what is being yielded in program 
