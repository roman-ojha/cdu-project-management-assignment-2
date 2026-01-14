def encrypt_text():
    pass


def decrypt_text():
    pass


def main():
    print("1) Encrypt Text: \n2) Decrypt Text: \n")
    encrypt = int(input("Enter option 1 or 2:"))

    if encrypt == 1:
        encrypt_text()
    elif encrypt == 2:
        decrypt_text()
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()
