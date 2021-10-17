def find_even_numbers(nums) -> int:
    res = 0
    # retornar números par de dígitos
    for n in nums:
        if len(str(n)) % 2 == 0:
            res += 1
    return res
