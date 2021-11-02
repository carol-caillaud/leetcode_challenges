# retorne o quadrado de cada número, n ** 2, clasificado em ordem não decrescente
def sortedSquares(nums): # função para ordenar o square array
    i = 0
    for n in nums:
        nums[i] = n ** 2 #converter os elementos em seus valores em quadrado
        n += 1
    nums.sort() # retorna a lista ordenada e muda o array
        
    return nums

print(sortedSquares([-7,-3,2,3,11]))