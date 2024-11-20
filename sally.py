from os import killpg


def maxProfit(prices):

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
            print(profit)

def rotate(nums, k):

    return nums[-k:] + nums[:-k]


def containsDuplicate(nums):

    print(nums)
    dict = {}

    for i in range(len(nums)):
        print(i)
        print(nums[i])
        if nums[i] in dict.keys():
            dict[nums[i]] += 1
        else:
            dict[nums[i]] = 1


    for v in dict.values():
        if v > 1:
            return True


    print('\ndict: {}'.format(dict))
    return False





if __name__ == '__main__':
    # prices = [7, 6, 4, 3, 1]
    # prices = [1,2,3,4,5]
    # prices = [7,1,5,3,6,4]
    # maxProfit(prices)

    # nums = [1,2,3,4,5,6,7]
    # k = 3
    # nums = [-1, -100, 3, 99]
    # k = 2
    # print(rotate(nums, k))


#     nums=[1,1,1,3,3,4,3,2,4,2]
    nums = [1,2,3,4]
    # nums = [1,2,3,1]
    print(containsDuplicate(nums))

