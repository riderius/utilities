""" Module for translate temp_text to binary code and
    for translate binary code to temp_text.
        Functions are taken from here:
            http://bit.do/functions_from_text2binary """


def text_to_bits(text: str) -> str:
    """ Function for translate temp_text to binary code. """

    text = bin(int.from_bytes(text.encode('utf-8'), 'big'))[2:]
    print(text.zfill(8 * ((len(text) + 7) // 8)))


def text_from_bits(text: str) -> str:
    """ Function for translate binary code to temp_text. """

    text = int(text, 2)
    print(text.to_bytes((text.bit_length() + 7) //
                        8, 'big').decode('utf-8') or '\0')


function = int(input('1)Text to Binary Code \n2)Binary Code to Text \n'))
if function == 1:
    input_text = input('Enter text:\n')
    text_to_bits(input_text)
elif function == 2:
    input_text = input('Enter text:\n')
    text_from_bits(input_text)
else:
    print('This function is NOT')
