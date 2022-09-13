"""
https://leetcode.com/problems/longest-palindromic-substring/
"""
import collections
from collections import deque


def longest_palindromic_substring(s: str) -> str:
    dic = collections.defaultdict(int)
    for idx, e in enumerate(s):
        for k in range(idx, len(s) + 1):
            strs = s[idx:k]
            if strs == '' or dic.get(strs) is not None:
                continue
            if is_palindrome(strs):
                dic[strs] = len(strs)
    return max(dic, key=dic.get)

def is_palindrome(s: str):
    deq = deque()
    for e in s:
        deq.append(e)

    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False
    return True


# time limit
# s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
s = "babad"
print(longest_palindromic_substring(s))
# is_palindrome(s)
