import base64

print('      CEE ENCODER AND DECODER     \n')
while True:
    try:
        question = int(input('1. Encode your strings\n2. Decode your encoded strings\n3. Encode your text file\n4. Decode your text file\n5. Exit\nREPLY: '))
        if question == 1:
            print()
            encode = str(input('Enter your string to encode: '))
            string = encode.encode('utf-8')
            base_string = base64.b64encode(string)
            print('\nYour encoded string is: ', base_string.decode('utf-8'))
        elif question == 2:
            print()
            decode = str(input('Enter the encoded string to decode: '))
            base_string2 = base64.b64decode(decode)
            print('\nYour decoded string is:  ', base_string2.decode(), '\n')
        elif question == 3:
            print()
            text = str(input('Enter the text file to encode: '))
            read = open(text, 'r')
            encodetext = read.read()
            string = encodetext.encode('utf-8')
            base_string = base64.b64encode(string)
            print('\nYour encoded text string is: ', base_string.decode('utf-8'))
            read.close()
            while True:
                try:
                    q1 = str(input('Do you want to write the results to a text file? '))
                    if q1 == 'yes':
                        print()
                        q1a = str(input('Enter the name of the text file you want to write to: '))
                        writeencode = open(q1a, 'w')
                        writeencode.write(base_string.decode('utf-8'))
                        writeencode.close()
                        print('\nEncoded document has been saved to', q1a, '\n')
                        break
                    elif q1 == 'no':
                        print()
                        break
                    else:
                        print('Please enter yes or no')
                except ValueError:
                    print()
        elif question == 4:
            print()
            text = str(input('Enter the text file to decode: '))
            read = open(text, 'r')
            decodedtext = read.read()
            base_string2 = base64.b64decode(decodedtext)
            print('\nYour decoded text string is:  ', base_string2.decode(), '\n')
            read.close()
            while True:
                try:
                    q1 = str(input('Do you want to write the results to a text file? '))
                    if q1 == 'yes':
                        print()
                        q1a = str(input('Enter the name of the text file you want to write to: '))
                        writeencode = open(q1a, 'w')
                        writeencode.write(base_string2.decode())
                        writeencode.close()
                        break
                    elif q1 == 'no':
                        print()
                        break
                    else:
                        print('Please enter yes or no')
                except ValueError:
                    print()
        elif question == 5:
            print('Learn more from ceefoon. Thank you')
            break
        else:
            print('Choose the correct option')
    except ValueError:
        print('Choose the correct option')
    except FileNotFoundError:
        print('No such file named', text, 'was found in the directory.\n')