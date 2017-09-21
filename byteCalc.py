from math import exp

LARGESIZE =1024
SMALLSIZE = 1000
BITS = 8

# kb to bytes
# MB to bytes
# TB to byte
# TB to MB
"""
    1 Byte = 8 Bits
    1 KB = 1000 Bytes
    1 MB = 1000 * 1000 Bytes
    1 GB = 1000 * 1000 * 1000 Bytes
    1 TB = 1000 * 1000 * 1000 * 1000 Bytes
"""
def choiceone(): # Convert KB to Bytes
    bitcalc =  int(input("How many KB would you like to convert to Bytes? "))
    print("\n")
    print("Assuming a number of 1,024 for calculations, the conversion would be as follows:")
    kb2bytes = (bitcalc * LARGESIZE)
    print(" Converting", bitcalc, "KB to Bytes =", kb2bytes,"Bytes")

    print("\n")

    print("Assuming a number of 1,000 for calculations, the conversion would be as follows:")
    kb2bytesSmall = (bitcalc * SMALLSIZE)
    print(" Converting", bitcalc, "KB to Bytes =", kb2bytesSmall,"Bytes")


def choicetwo(): #Convert MB to Bytes
    bitcalc =  int(input("How many MB would you like to convert to Bytes? "))
    print("\n")
    print("Assuming a number of 1,024 for calculations, the conversion would be as follows:")
    mb2bytes = (bitcalc * pow(LARGESIZE,2)/1000)
    print(" Converting", bitcalc, "MB to Bytes =", int(mb2bytes),"Bytes")

    print("\n")

    print("Assuming a number of 1,000 for calculations, the conversion would be as follows:")
    mb2bytesSmall = (bitcalc * pow(SMALLSIZE,2)/1000)
    print(" Converting", bitcalc, "MB to Bytes =", int(mb2bytesSmall), "Bytes")


def choicethree(): # Convert TB to Bytes
    bitcalc =  int(input("How many TB would you like to convert to Bytes? " ))
    print("\n")
    print("Assuming a number of 1,024 for calculations, the conversion would be as follows:")
    tb2bytes = (bitcalc * pow(LARGESIZE,4))
    print(" Converting", bitcalc, "TB to Bytes =", tb2bytes,"Bytes")


    print("\n")

    print("Assuming a number of 1,000 for calculations, the conversion would be as follows:")
    tb2bytesSmall = (bitcalc * pow(SMALLSIZE,4))
    print(" Converting", bitcalc, "TB to Bytes =", tb2bytes,"Bytes")


def choicefour(): # Convert TB to MB
    bitcalc =  int(input("How many TB would you like to convert to Bytes? " ))
    print("\n")
    print("Assuming a number of 1,024 for calculations, the conversion would be as follows:")
    tb2mb = (bitcalc * pow(LARGESIZE,2))
    print(" Converting ", bitcalc, " TB to MB = ", tb2mb, "Mb")

    print("\n")

    print("Assuming a number of 1,000 for calculations, the conversion would be as follows:")
    tb2mbSmall =  (bitcalc * pow(SMALLSIZE,2))
    print(" Converting ", bitcalc, "TB to MB =", tb2mbSmall, "Mb")


print("To convert KB, choose option 1\nTo convert MB, choose option 2\nTo convert TB, choose option 3\nTo convert TB to MB, choose option 4\n")
convertChoice = str(input("Please choose an option to convert that into Bits: "))

while True:
    if convertChoice =="1":
        choiceone()
        break
    if convertChoice =="2":
        choicetwo()
        break
    if convertChoice =="3":
        choicethree()
        break
    else:
        print("Invalid Choice")
        print("To convert TB, choose option 1\nTo convert GB, choose option 2\nTo convert MB, choose option 3\n")
        convertChoice = str(input("Please choose an option to convert that into Bits: "))
