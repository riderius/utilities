""" Module for translate text to binary code and for translate binary code to text.
    Functions are taken from here:
        http://bit.do/functions_from_text2binary """


def text_to_binary(text: str) -> None:
    """

    Function for translate text to binary code.

    Args:
        text (str): A variable that stores text that will be converted to binary code.

    Returns:
        None: The function returns nothing.

    """

    text = bin(int.from_bytes(text.encode('utf-8'), 'big'))[2:]
    print(text.zfill(8 * ((len(text) + 7) // 8)))


def text_from_binary(text: str) -> None:
    """

    Function for translate binary code to text.

    Args:
        text (str): A variable that stores binary code that will be converted to normal text.

    Returns:
        None: The function returns nothing.

    """

    text = int(text, 2)
    print(text.to_bytes((text.bit_length() + 7) //
                        8, 'big').decode('utf-8') or '\0')


function = int(input('1)Text to Binary Code \n2)Binary Code to Text \n'))
if function == 1:
    input_text = input('Enter text:\n')
    text_to_binary(input_text)
elif function == 2:
    input_text = input('Enter text:\n')
    text_from_binary(input_text)
else:
    print('This function is NOT')
