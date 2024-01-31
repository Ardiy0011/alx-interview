#!/usr/bin/python3
"""function that reads stdin line by line and computes metrics"""


def validUTF8(data):
    """Helper function to check if a given byte is
     a valid UTF-8 continuation byte"""
    def isContinuation(byte):
        return (byte & 0b11000000) == 0b10000000
    i = 0
    while i < len(data):
        byte = data[i]

        if (byte & 0b10000000) == 0:
            i += 1

        elif (byte & 0b11100000) == 0b11000000:
            if i + 1 < len(data) and isContinuation(data[i + 1]):
                i += 2
            else:
                return False

        elif (byte & 0b11110000) == 0b11100000:
            if i + 2 < len(data) and isContinuation(
                data[i + 1]) and isContinuation(
                    data[i + 2]):
                i += 3
            else:
                return False

        elif (byte & 0b11111000) == 0b11110000:
            if i + 3 < len(data) and isContinuation(
                data[i + 1]) and isContinuation(
                    data[i + 2]) and isContinuation(data[i + 3]):
                i += 4
            else:
                return False
        else:
            return False

    return True
