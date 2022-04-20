def check_arithmetic_subarrays(nums, l, r):
    answer = []
    for i, j in zip(l, r):
        temp = sorted(nums[i:j + 1])
        answer.append(len(set([temp[x + 1] - temp[x] for x in range(len(temp) - 1)])) == 1)
    return answer


if __name__ == '__main__':
    print(check_arithmetic_subarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))
