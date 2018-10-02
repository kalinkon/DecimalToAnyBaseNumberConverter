def base10toAny(number_to_convert, to_base):

   # change to any Base number

    NUM_DICT = {
        10: 'a',
        11: 'b',
        12: 'c',
        13: 'd',
        14: 'e',
        15: 'f',
        16: 'g',
        17: 'h',
        18: 'i',
        19: 'j',
        20: 'k',
        21: 'l',
        22: 'm',
        23: 'n',
        24: 'o',
        25: 'p',
        26: 'q',
        27: 'r',
        28: 's',
        29: 't',
        30: 'u',
        31: 'v',
        32: 'w',
        33: 'x',
        34: 'y',
        35: 'z'}

    result_code = ''
    input_number = number_to_convert

    while input_number != 0:

        remainder = input_number % to_base

        if remainder > 9:
            result_code = result_code + NUM_DICT.get(remainder)
        else:
            result_code = result_code + str(remainder)

        input_number = int(input_number / to_base)
    return result_code[::-1].upper()


if __name__ == "__main__":
    
    while True:
        number_to_convert = int(input("Enter the decimal number you want to converted "))
        to_base = int(input("Enter the base number you want the number to be converted to: "))
        print(str(number_to_convert)+ " is " + base10toAny(number_to_convert, to_base) + " in Base " + str(to_base) )

        break_flag = True

        while True:
            try_again = input("want to try again y/n :")

            if try_again is "y":
                break_flag = False
                break
            elif try_again is "n":
                break_flag = True
                break
            else:
                print("give a valid input")

        if break_flag is True:
            break
