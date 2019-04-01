"""This program gets the string with duplicate characters
then compresses/decompress this string by the RLE."""


def compression(mystr):
    """This function compresses string with duplicate characters."""
    counter_of_ch = 0
    compressed_string = ''
    for i in range(len(mystr)):
        ch = mystr[i]
        counter_of_ch += 1
        if i == len(mystr) - 1:
            compressed_string = compressed_string + str(counter_of_ch) + ch
            break
        else:
            if ch == mystr[i + 1]:
                pass
            else:
                compressed_string = compressed_string + str(counter_of_ch) + ch
                counter_of_ch = 0
    return compressed_string


def decompression(compressed_string):
    """This function decompresses string with duplicate characters."""
    decompressed_srting = ''
    if compressed_string != '':
        for i in range(0, len(compressed_string), 2):
            num = int(compressed_string[i])
            ch = compressed_string[i + 1]
            decompressed_srting = decompressed_srting + num * ch
    else:
        print('This string is empty!')
    print(decompressed_srting)


if __name__ == '__main__':
    your_str = 'AAAAAAFFFFFFFJJJJJJ'
    compression(your_str)
    decompression(compression(your_str))
