##################################################################
# PYTHON SCRIPT TO ENCRYPT OFFSETS INSIDE TWEAK.XM
# https://github.com/joeyjurjens
# This has been made for https://github.com/joeyjurjens/iOS-Mod-Menu-Template-for-Theos
# You may need to customize this script for your tweak.xm
# You also need to handle the decryption on your own.
# NOTE: XOR encryption is not the best encryption, but handling the decryption good should be enough.
###################################################################

import re

# Change those two to your own numbers, make sure they are different from each other!
# Make sure you puth for both a 19 numbers long number, else it will fuck up.
# If you change these, also open Utils.h & change them there too with the same values you have here.
cryptBaseOne = 1959173450275472825
cryptBaseTwo = 8264919756289164628

def encrypt_offset(offset):
    return str((int(offset, 16) + cryptBaseOne) ^ cryptBaseTwo)

# Translation of this pattern:
# Offset can contain numbers & characters --> [0-9a-fA-F]
# Length of offset: 9 --> {9}
    # I haven't met any game with larger/shorter offsets.
# Must end with: ',' or '}' or ')' --> [,})]
    # Last offset in switch will end with '}'
    # multiple offsets in array is ','
    # getRealOffset ends with ')'
    # NOTE: Use a macro for MSHookFunction, as you need to handle decryption, my template has HOOK()
pattern = re.compile(r'(0x[0-9a-fA-F]{9})[,})]')

def find_offsets_in_file():
    with open("Tweak.xm", "rt") as file:
        data = file.read()
        matches = pattern.finditer(data)
        hasPrintedCredits = False

        for match in matches:
            # Just cause it's cool to print things :kappa:
            if not hasPrintedCredits:
                print("="*43)
                print("OFFSET ENCRYPTION TOOL MADE BY JOEYJURJENS")
                print("="*43)
                hasPrintedCredits = True

            offsetString = match.group(1)
            print("Offset found: %s " % offsetString)
            print("Encrypting offset now...")           
            data = data.replace(offsetString, encrypt_offset(offsetString))
            print("New Offset: %s" % encrypt_offset(offsetString))

        # Write the new data to the file.
        write_new_data_to_file(data)            


def write_new_data_to_file(data):
    with open("Tweak.xm", "wt") as file:
        file.write(data)
        file.close()

# Find the offsets in tweak.xm
find_offsets_in_file()