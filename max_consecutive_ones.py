def max_consecutive_ones(nums):
    # retornar a contagem máxima de 1s consecuivos
    # iniciar contagem
    count = 0
    # iniciar contagem máxima
    max_count = 0
    for n in nums:
        # se achar 1 aumentar contagem
        if n == 1:
            count += 1
        # resetar contagem se achar 0
        elif n == 0:
            count = 0
        # se achar um incrementar a contagem
        if count > max_count:
            max_count = count
    return max_count


print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))
