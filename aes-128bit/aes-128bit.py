AES_S_BOX = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16] 
]

AES_INVERSE_S_BOX = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
]

AES_RCON = [["01", "02", "04", "08", "10", "20", "40", "80", "1b", "36"],
        ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00"],
        ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00"],
        ["00", "00", "00", "00", "00", "00", "00", "00", "00", "00"]
]


"""
Converts hexa decimal text into 4 x 4 state matrix
"""
def GetStateMatrix(PlainText):
    StateMatrix = [["0" for x in range(4)] for y in range(4)]
    PlainTextList=list(PlainText)
    index=0
    for i in range(4):
        for j in range(4): 
            StateMatrix[j][i]=PlainTextList[index]+PlainTextList[index+1] 
            index+=2
    return StateMatrix 

"""
Apply s-box to state matrix
"""
def GetSubBytes(StateMatrix):
    HexaArray=""
    SubBytesMatrix = [["0" for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4): 
            HexaArray=list(StateMatrix[i][j])
            if len(HexaArray)==4:
                SubBytesMatrix[i][j]=hex(AES_S_BOX[int(HexaArray[2],16)][int(HexaArray[3],16)] )
            elif len(HexaArray)==3 :
                SubBytesMatrix[i][j]=hex(AES_S_BOX[0][int(HexaArray[2],16)] )
            else:
                SubBytesMatrix[i][j]=hex(AES_S_BOX[int(HexaArray[0],16)][int(HexaArray[1],16)] )
    return SubBytesMatrix 

"""
Apply inverse s-box to state matrix
"""
def GetInverseSubBytes(StateMatrix):
    HexaArray=""
    InverseSubBytesMatrix = [["0" for x in range(4)] for y in range(4)]
    for i in range(4):
        for j in range(4): 
            HexaArray=list(StateMatrix[i][j])
            if len(HexaArray)==4:
                InverseSubBytesMatrix[i][j]=hex(AES_INVERSE_S_BOX[int(HexaArray[2],16)][int(HexaArray[3],16)] )
            elif len(HexaArray)==3 :
                InverseSubBytesMatrix[i][j]=hex(AES_INVERSE_S_BOX[0][int(HexaArray[2],16)] )
            else:
                InverseSubBytesMatrix[i][j]=hex(AES_INVERSE_S_BOX[int(HexaArray[0],16)][int(HexaArray[1],16)] )
    return InverseSubBytesMatrix 


"""
Perform the shift row step during encryption
"""
def GetShiftRows(SubBytesMatrix):
    i=0
    index=0
    for row in SubBytesMatrix:
        row=row[i:] + row[:i]
        SubBytesMatrix[index] = row
        index+=1
        i+=1 
    return SubBytesMatrix 


"""
Perform the inverse shift row step during decryption
"""
def GetInverseShiftRows(InverseSubBytesMatrix):
    i=0
    index=0
    for row in InverseSubBytesMatrix:
        row=row[-i:] + row[:-i]
        InverseSubBytesMatrix[index] = row
        index+=1
        i+=1 
    return InverseSubBytesMatrix


"""
Get Galios Number for Mix columns step
"""
def GaloisNumber(FirstNum, SecondNum):
    i = 0
    for counter in range(8):
        if SecondNum & 1: i ^= FirstNum
        BitSet = FirstNum & 0x80
        FirstNum <<= 1
        FirstNum &= 0xFF
        if BitSet:
            FirstNum ^= 0x1b
        SecondNum >>= 1
    return i


"""
Perform the Mix column step during encryption
"""
def GetMixColumns(ShiftRowsMatrix):
    fixed = [2, 1, 1, 3]
    row = [0, 3, 2, 1]
    coloumn = 0
    OutputArray = []
    for _ in range(4):
        for _ in range(4):
            OutputArray.append('%02x' % (GaloisNumber(int(ShiftRowsMatrix[row[0]][coloumn], 16), fixed[0]) ^GaloisNumber(int(ShiftRowsMatrix[row[1]][coloumn], 16), fixed[1]) ^ GaloisNumber(int(ShiftRowsMatrix[row[2]][coloumn], 16), fixed[2]) ^GaloisNumber(int(ShiftRowsMatrix[row[3]][coloumn], 16), fixed[3])))
            row = [row[-1]] + row[:-1]
        coloumn += 1
    ShiftRowsMatrix = [OutputArray[i:i+4] for i in range(0, 16, 4) ]
    MixColoumnsMatrix=[["0" for x in range(4)] for y in range(4)] 
    for i in range(4):
        for j in range(4):
            MixColoumnsMatrix[i][j]=ShiftRowsMatrix[j][i]
    return MixColoumnsMatrix 

"""
Perform the inversed Mix column step during decryption
"""
def GetInverseMixColumns(ShiftRowsMatrix):
    fixed = [14, 9, 13, 11]
    row = [0, 3, 2, 1]
    coloumn = 0
    OutputArray = []
    for _ in range(4):
        for _ in range(4):
            OutputArray.append('%02x' % (GaloisNumber(int(ShiftRowsMatrix[row[0]][coloumn], 16), fixed[0]) ^GaloisNumber(int(ShiftRowsMatrix[row[1]][coloumn], 16), fixed[1]) ^ GaloisNumber(int(ShiftRowsMatrix[row[2]][coloumn], 16), fixed[2]) ^GaloisNumber(int(ShiftRowsMatrix[row[3]][coloumn], 16), fixed[3])))
            row = [row[-1]] + row[:-1]
        coloumn += 1
    ShiftRowsMatrix = [OutputArray[i:i+4] for i in range(0, 16, 4) ]
    InverseMixColoumnsMatrix=[["0" for x in range(4)] for y in range(4)] 
    for i in range(4):
        for j in range(4):
            InverseMixColoumnsMatrix[i][j]=ShiftRowsMatrix[j][i]
    return InverseMixColoumnsMatrix 

"""
Generate list of N round keys
"""
def KeySchedule(StateMatrix):
    Keys=[]
    for num in range(10):
        if num > 0:
            StateMatrix= RoundKey
        RoundKey=[["0" for x in range(4)] for y in range(4)] 
        x=0
        index=0
        RowMatrix=[["0" for x in range(4)] for y in range(4)] 
        for i in range(4):
            for j in range(4):
                RowMatrix[i][j]=StateMatrix[j][i]
        state=RowMatrix

        Result=[["0" for x in range(4)] for y in range(4)]  
        for row in state:
            row=row[1:] + row[:1]
            state[index] = row
            index+=1
            x+=1
        state=GetSubBytes(state) 
        
        for i in range(4):
            Result[0][i]=hex(int(StateMatrix[i][0],16) ^ int(state[3][i],16) ^ int(AES_RCON[i][num],16) )
            
        for i in range(1,4):
            for j in range(4):
                Result[i][j] = hex(int(Result[i-1][j],16) ^ int(StateMatrix[j][i],16))
           
        for i in range(4):
            for j in range(4):
                RoundKey[i][j]=Result[j][i]
        
        Keys.append(RoundKey)
    
    return Keys

"""
Add N rounds keys
"""
def AddRoundKey(StateMatrix,KeyMatrix):
    RoundKey=[["0" for x in range(4)] for y in range(4)]
    
    for i in range(4):
        for j in range(4):
            RoundKey[j][i]=hex(int(StateMatrix[j][i],16) ^ int(KeyMatrix[j][i],16))
    return RoundKey  

def GetPlainTextMatrix(FinalMatrix):
    PlainText=""
    for i in range(4):
        for j in range(4):
            if len(FinalMatrix[j][i])==3:
                PlainText+='0' 
            PlainText+=FinalMatrix[j][i][2:]   
    return PlainText 

"""
Encrypt block of plain text
"""
def Encrypt(Key,PlainText):

    StateMatrix=GetStateMatrix(PlainText)
       
    KeyMatrix=GetStateMatrix(Key)
    
    RoundKeyMatrix= AddRoundKey(StateMatrix,KeyMatrix)
    
    KeyList = KeySchedule(KeyMatrix)
    
    # For first 9 rounds
    for i in range(9):
        SubBytesMatrix= GetSubBytes(RoundKeyMatrix)
        ShiftRowsMatrix= GetShiftRows(SubBytesMatrix)
        MixColoumnsMatrix=GetMixColumns(ShiftRowsMatrix)
        RoundKeyMatrix=AddRoundKey(MixColoumnsMatrix,KeyList[i])
        
    # for last round
    SubBytesMatrix= GetSubBytes(RoundKeyMatrix) 
    ShiftRowsMatrix=GetShiftRows(SubBytesMatrix)
    RoundKeyMatrix=AddRoundKey(ShiftRowsMatrix,KeyList[9])
    CipherText = GetPlainTextMatrix(RoundKeyMatrix)
    
    return CipherText 

"""
Decrypt block of cipher text
"""
def Decrypt(Key,CipherText):
    StateMatrix=GetStateMatrix(CipherText)
    KeyMatrix=GetStateMatrix(Key)
    KeyList=KeySchedule(KeyMatrix)
    RoundKeyMatrix = AddRoundKey(StateMatrix,KeyList[-1])
    index=8
    for i in range(9):
        if i == 0:
            InverseShiftRowsMatrix=GetInverseShiftRows(RoundKeyMatrix)
        else:
            InverseShiftRowsMatrix=GetInverseShiftRows(InverseKeyMixColumnsMatrix)

        InverseSubBytesMatrix=GetInverseSubBytes(InverseShiftRowsMatrix)
        RoundKeyMatrix=AddRoundKey(InverseSubBytesMatrix,KeyList[index])
        InverseKeyMixColumnsMatrix=GetInverseMixColumns(RoundKeyMatrix)
        index-=1
    
    InverseShiftRowsMatrix=GetInverseShiftRows(InverseKeyMixColumnsMatrix)
    InverseSubBytesMatrix= GetInverseSubBytes(InverseShiftRowsMatrix) 
    
    RoundKeyMatrix=AddRoundKey(InverseSubBytesMatrix,KeyMatrix)
    PlainText=GetPlainTextMatrix(RoundKeyMatrix)
    
    return PlainText


"""
Encrypt plain text and return cipher text
"""
def EncryptText(key, Text):
    
    en_key = ""
    spaces = 0
    
    en_key = key.encode('utf-8').hex()
    
    Text = Text.encode('utf-8').hex()
    
    cipher = ""   
    if len(Text) % 32 != 0:
        spaces = len(Text) % 32
    
    for i in range(spaces, 32):
        Text += '0'
    
    temp = ''
    for x in Text:
        temp = temp + x
        if len(temp) == 32:
            cipher += Encrypt(en_key,temp)
            temp = ""
   
    return cipher

"""
Decrypt cipher text and return plain text
"""
def DecryptText(key, Text):
    
    en_key = ""
    spaces = 0
    
    en_key = key.encode('utf-8').hex()
    
    plainText = ""
    temp = ""
    for x in Text:
        temp += x
        if len(temp) == 32:
            plainhex = Decrypt(en_key,temp)
            plainText += bytes.fromhex(plainhex).decode()
            temp = ""
   
    return plainText


PlainText="This is just an example of plain text"
Key="This is a secret key"


ct = EncryptText(Key, PlainText)

dt = DecryptText(Key, ct)

print("Plain Text:", PlainText)
print("Key:", Key)
print("Cipher Text:", ct)
print("Plain Text:", dt)
