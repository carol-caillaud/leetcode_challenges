def remove_duplicates (nums):
    duplicates = []
    i = 0
    k = 0
    while(i < len(nums)):
        if nums[i] in duplicates:
            nums.pop(i)
            i -= 1
        else:
            k += 1
            duplicates.append(nums[i])
        i += 1
    print(nums)

#for não acessa index
#for não percorre a lista ao cont