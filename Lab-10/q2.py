def count_vowels(s):
    count = sum(1 for i in s.lower()  if i in "aieou")
    return f"count: {count}"
if __name__ == "__main__":
    s = input()
    print(count_vowels(s))