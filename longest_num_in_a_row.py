def longest_num(arr):
    """
    В функцию передается список чисел. 
    Функция вернет самую большуй подстроку этого списка в которой
    повторяется один и тот же элемент, а также вернет его индекс.
    
    """
    best = ''
    sub = ''
    start_index = 0                 
    for ind, elem in enumerate(arr):
        for n in arr[ind:]:
            if n == elem:
                sub += ' ' + str(n)
                if len(sub) > len(best):
                    best = sub
                    start_index = ind
            else:
                sub = ''
                break
    return f'Answer - {best}\nIndex = {start_index}'