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
    if len(s) < 2 or s == s[::-1]:
        return True
    return False


# time limit
# s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
# s = "dsqspnkrvrhqzqvovbofdzqishgtcrvckluzpwesvartjhljqdphdupktoxdffvoqupuxmehikegjnwuheoafgqrtvuzphkikaixnjmhepeqorzjzgnrxxxirhjvboijbzftxhvtrdmbcvysxscvqmgifipwujvvktithqthujpxwwgamwqkxnnxiymtuvtyzafbxybalnjboaiyrxedviesmzzwgagilndguylskdikiocvqmjmfykakuiihuqurgqqirjoccqoixegyspftktguitqtixcsywycutcaedusndombnfzpgoklqzzqlkogpzfnbmodnsudeactucywyscxitqtiugtktfpsygexioqccojriqqgruquhiiukakyfmjmqvcoikidkslyugdnligagwzzmseivdexryiaobjnlabyxbfazytvutmyixnnxkqwmagwwxpjuhtqhtitkvvjuwpifigmqvcsxsyvcbmdrtvhxtfzbjiobvjhrixxxrngzjzroqepehmjnxiakikhpzuvtrqgfaoehuwnjgekihemxupuqovffdxotkpudhpdqjlhjtravsewpzulkcvrctghsiqzdfobvovqzqhrvrknpsqsd"
# s = "vthbaypbzzfrgeqkfsazhvocumiiblrrcxprqhpdkifncwazfrhmimewubfxmgehebepiuhkvghnbtvyckioxavjcezgbpztkimjmugprtwhsbthytmznfdihgtiuogiixshdqhczbkhswgfqfeaxajozaazczvfbnhzgazmcvplwutfdoatytwxpoxyzggjysobgdkurqdocpakcaxzvfcpagipbqfdfwhzitlezfpdhayrroztwgfqmcfkrphzehxbyioqxxvusvhqktmdovrwlijwjdxccylqqhbfbsmmjpgknxpivysnvedjmnasjtaufzdopjmzfubyxcrfqwaulbqnhezmtaygstdtldkqeeeeqkdltdtsgyatmzehnqbluawqfrcxybufzmjpodzfuatjsanmjdevnsyvipxnkgpjmmsbfbhqqlyccxdjwjilwrvodmtkqhvsuvxxqoiybxhezhprkfcmqfgwtzorryahdpfzeltizhwfdfqbpigapcfvzxackapcodqrukdgbosyjggzyxopxwtytaodftuwlpvcmzagzhnbfvzczaazojaxaefqfgwshkbzchqdhsxiigouitghidfnzmtyhtbshwtrpgumjmiktzpbgzecjvaxoikcyvtbnhgvkhuipebehegmxfbuwemimhrfzawcnfikdphqrpxcrrlbiimucovhzasfkqegrfzzbpyabhtv"
s = "babad"
# print(longest_palindromic_substring(s))


# is_palindrome(s)

# abc = "abc"
# print(abc[::-1])
#
def longest_palindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s

    def expand(left: int, right: int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    result = ''
    for i in range(len(s) - 1):
        e1 = expand(i, i + 1)
        e2 = expand(i, i + 2)
        print(e1, e2)
        result = max(result, e1, e2, key=len)
    return result

print(longest_palindrome(s))
