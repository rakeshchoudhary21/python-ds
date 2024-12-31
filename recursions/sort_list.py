
def sort(nums: list) :
    if not len(nums) : return

    item = nums.pop()
    sort(nums)
    insert_at_right_place(item, nums)

def insert_at_right_place(item :int, nums :list):
    if not len(nums) or item >= nums[-1]:
        nums.append(item)
    else:
        last = nums.pop()
        insert_at_right_place(item ,nums)
        nums.append(last)

if __name__ == '__main__':
    nums = [2,1,2,1,4,6]
    sort(nums)
    print(nums)


