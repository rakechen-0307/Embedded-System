from typing import ByteString

# Input bytes
# input_bytes = b'\x00\x01\x00\x02\x00\x03'
MAG_DATA = [0, 0, 0]


def print3axis(input_bytes: ByteString):
    if len(input_bytes) != 6:
        print("Data must be a byte string of length 6")
        return
    # Convert input_bytes to an array of six b'\xXX'
    byte_array = [input_bytes[i:i+1] for i in range(len(input_bytes))]

    # Concatenate byte_array[i] and byte_array[i+1] for i = 0, 2, 4 ...
    concatenated_bytes = [byte_array[i] + byte_array[i+1]
                          for i in range(0, len(byte_array), 2)]

    for i in range(0, len(concatenated_bytes)):

        # Convert byte object to decimal integer
        decimal_int = int.from_bytes(concatenated_bytes[i], byteorder='big')

        # Interpret byte_obj as two's complement
        if decimal_int > 32767:
            decimal_int = decimal_int - 65536

        # Print the decimal integer using f-string
        print(f"Byte: {concatenated_bytes[i]}, Decimal: {decimal_int}")
        MAG_DATA[i] = decimal_int


data = b'\x00\x01\x00\x02\x00\x03'
print3axis(data)
