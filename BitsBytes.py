def B2B_Big(bitarr):
    s = i = 0 #Declares s to be 00000000
    for b in bitarr: 
        s = (s >> 1) | (0, 0x80)[b] #Shift S to the right one it, and or it
                                    #with either 0 (if b is 0) or 0x80(if b is 1)
        i += 1 
        if i == 8:
            yield s
            s = i = 0 #reset s to 0 for the next sequence of bits in s

    while ((i < 8)and(i > 0)):
       s >>= 1
       i += 1
       yield s 


#This one needs to be used for string. Returns the message
#character bytes in reverse order of the message
def B2B_Little(bitarr):
    s = i = 0 #Declares s to be 00000000
    bitarr = bitarr[::-1]
    for b in bitarr: 
        s = (s >> 1) | (0, 0x80)[b] #Shift S to the right one it, and or it
                                    #with either 0 (if b is 0) or 0x80(if b is 1)
        i += 1 
        if i == 8:
            yield s
            s = i = 0 #reset s to 0 for the next sequence of bits in s

    while ((i < 8)and(i > 0)):
       s >>= 1
       i += 1
       yield s


#Turns a message into an array of bits based on ASCII code
def bits(message):
    a = list()
    for char in message:
        b = ord(char)
        i = 0
        while (i < 8):
            if ((b>>7)%2 == 1):
                a.append(1)
            else:
                a.append(0)
            b <<= 1
            i += 1
    return a
            
        
