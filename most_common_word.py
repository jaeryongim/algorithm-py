"""
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

Example)
입력 -> paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
       banned = ["hit"]
출력 -> "ball"
"""
import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# 정규식에서 \w는 단어 문자를 뜻한다.
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]


"""
첫번째 풀이
"""
def most_common_world_1():
    result = dict()
    for w in words:
        if result.get(w) is None:
            result[w] = 1
        else:
            result[w] += 1

    return max(result, key=result.get)


"""
두번째 문제 풀이
defaultdict 을 사용할 경우 값이 없을 때 자동으로 1을 부여할 수 있게 된다.
즉, 값이 있는지 하나씩 검증하는 논리를 작성하지 않아도 된다.
"""
def most_common_world_2():
    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


"""
세번쨰 문제 풀이
두번쨰 문제 풀이와 방법은 같으나 마지막에 개수를 확인하는 방법이 조금 다르다.
collections의 Counter의 most_common 를 이용한다.
"""
def most_common_world_3():
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(most_common_world_1())
print(most_common_world_2())
print(most_common_world_3())
