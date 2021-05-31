# BOJ 11655
import sys


def encrypt(word):
    encrypted_word = []
    for i in range(len(word)):
        if ord(word[i]) >= ord("A") and ord(word[i]) <= ord("Z"):
            if ord(word[i]) - 13 >= ord("A"):
                encrypted_word.append(chr(ord(word[i]) - 13))
            else:
                encrypted_word.append(chr(ord(word[i]) - 13 + 26))
        elif ord(word[i]) >= ord("a") and ord(word[i]) <= ord("z"):
            if ord(word[i]) - 13 >= ord("a"):
                encrypted_word.append(chr(ord(word[i]) - 13))
            else:
                encrypted_word.append(chr(ord(word[i]) - 13 + 26))
        else:
            encrypted_word.append(word[i])
    return "".join(encrypted_word)


word = input()
print(encrypt(word))