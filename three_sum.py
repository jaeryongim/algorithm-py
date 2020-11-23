"""
세수의 합
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
example
입력 -> [-1, 0, 1, 2, -1, -4]
출력 ->
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
from typing import List


def brute_force(nums: List[int]) -> List[List[int]]:
    result = []
    # sort의 시간 복잡도는 O(nlogn)
    nums.sort()
    # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i], nums[j], nums[k]))

    return result

def two_point(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(0, len(nums) - 2):
        # 중복 값 건너 뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 인 경우 이므로 정답 및 스킵처리
                # sum이 0일 경우 어느 한쪽만 이동하는 경우는 불가능이므로 left, right 모두 움직인다.
                results.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results


print(brute_force([-1, 0, 8, -4, -4]))
print('-------------------------')
print(two_point([-1, 0, 8, -4, -4]))
