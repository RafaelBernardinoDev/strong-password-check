from strenght_check import validator


if __name__ == "__main__":
    pass_input = input("Insira uma senha para checkar a sua força: ")
    if validator(pass_input):
        print('Strong Password!')
    else: 
        print("Weak Password!")