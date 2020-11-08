"""
두수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 '인덱스'를 반환하라
example
입력 -> [2, 7, 11, 15], target = 9
출력 -> [0, 1]
"""
from typing import List, Tuple


def two_sum(inputs: List[int], target: int) -> List[int]:
    # return use_brute_force(inputs, target)
    # return use_in_operator(inputs, target)
    return use_dict_type(inputs, target)

def use_brute_force(source: List[int], target: int) -> List[int]:
    source_length = len(source)
    for i in range(0, source_length):
        for j in range(i + 1, source_length):
            if source[i] + source[j] == target:
                return [i, j]
    raise Exception('not exist')

def use_in_operator(source: List[int], target: int) -> Tuple[int, int]:
    # 타겟에서 첫 번째 값을 뺸 값 target - n이 존재하는지 탐색하는 문제로 변경
    # brute_force와 시간 복잡도는 O(n^2)로 같지만
    # 파이썬의 내부 함수로 구현된 in이 파이썬 레벨에서 비교하는 연산 속도보다 월등히 빠르다.
    for i, n in enumerate(source):
        complement = target - n
        if complement in source[i + 1:]:
            return source.index(n), source[i + 1:].index(complement) + (i + 1)
    raise Exception('not exist')

def use_dict_type(source: List[int], target: int) -> Tuple[int, int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, n in enumerate(source):
        nums_map[n] = i

    for i, n in enumerate(source):
        if target - n in nums_map and i != nums_map[target - n]:
            return source.index(n), nums_map[target - n]
    print(nums_map)


inputs = [2, 7, 11, 15]
target = 26
print(two_sum(inputs, target))
print(type(two_sum(inputs, target)))

