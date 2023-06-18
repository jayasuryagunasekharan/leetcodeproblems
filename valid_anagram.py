from collections import Counter


def valid_anagram_sol_1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hashmap_s, hashmap_t = {}, {}

    for str1 in s:
        if str1 in hashmap_s:
            hashmap_s[str1] = hashmap_s.get(str1)+1
        else:
            hashmap_s[str1] = 1

    for str1 in t:
        if str1 in hashmap_t:
            hashmap_t[str1] = hashmap_t.get(str1)+1
        else:
            hashmap_t[str1] = 1
    print(hashmap_t)
    print(hashmap_s)

    for i in hashmap_s:
        if hashmap_t.get(i) != hashmap_s.get(i):
            return False
    return True

def valid_anagram_sol_2(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

if __name__ == '__main__':
    value1 = valid_anagram_sol_1('anagram', 'nagamar')
    print('value1: ', value1)

    value2 = valid_anagram_sol_2('anagran', 'nagamar')
    print('value2: ', value2)