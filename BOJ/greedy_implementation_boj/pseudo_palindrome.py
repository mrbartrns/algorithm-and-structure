# BOJ 17609 유사 회문
import sys

sys.stdin = open('../input.txt', 'r')
si = sys.stdin.readline


def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left <= right:
        if word[left] != word[right]:
            new_word1 = is_pseudo_palindrome(word, left, right - 1)
            new_word2 = is_pseudo_palindrome(word, left + 1, right)
            if not new_word1 and not new_word2:
                return 2
            return 1
        left += 1
        right -= 1
    return 0


def is_pseudo_palindrome(word, left, right):
    while left <= right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


n = int(si())
for _ in range(n):
    word = si().strip()
    print(is_palindrome(word))
