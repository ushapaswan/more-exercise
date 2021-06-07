# Cipher wheel with a function for finding an element in a list

# find_in_list function defined here but not called
def find_in_list(query, mainlist):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
            return index
# this should return the position of the "query" in the "mainlist"
                                                                                                                                                                                        

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# encrypt_message function defined here but not called
def encrypt_message(plain_msg):
    encrypt_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypt_msg = encrypt_msg + new_char
        else:
            encrypt_msg = encrypt_msg + character
    return encrypt_msg
def decrypt_message(encrypt_msg):
    decrypt_msg = ""
    for character in encrypt_msg:
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypt_msg = decrypt_msg + new_char
        else:
            decrypt_msg = decrypt_msg + character
    return decrypt_msg
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_msg = input("Enter message to encrypt??")
        print(encrypt_message(plain_msg))
    elif choice == 'd':
        encrypt_message = input("Enter message to decrypt?")
        print(decrypt_message(encrypt_message))
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break

