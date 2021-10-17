def duplicate_zeros(arr) -> object:
    i = 0
    # duplicar os zeros sem modificar o  lenght do array
    while i < len(arr):
        # se for zero inserir no array
        if arr[i] == 0:
            arr.insert(i+1, 0)
            # remover o último item do array
            arr.pop(len(arr) -1)
            i+= 1
        i+= 1
    return arr
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
