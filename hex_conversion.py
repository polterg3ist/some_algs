def conversion(dec, nsystem):
    res = []
    nums = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 
    6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 
    13: 'D', 14: 'E', 15: 'F'}
    
    while True:
        if dec // nsystem >= 1:
            num = dec // nsystem
            n = dec - (nsystem * num)
            if nsystem == 16:
                res.append(nums[n])
            else:
                res.append(str(n))
            dec = num
        else:
            res.append(nums[dec])
            break
    result = ''.join(reversed(res))
    return result

print(conversion(148, 16))
