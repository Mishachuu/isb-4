def algoritm_luna(number: int) -> bool:
    number = str(number)
    if len(number) != 6:
        return False
    bin = [4, 4, 6, 6, 7, 4]
    end = [1, 3, 7]
    check = 8
    code = [int(i) for i in number]
    all_number = bin+code+end
    all_number = all_number[::-1]
    for i, num in enumerate(all_number):
        if i % 2 == 0:
            mul = num*2
            if mul > 9:
                mul -= 9
            all_number[i] = mul
    total_sum = sum(all_number)
    rem = total_sum % 10
    check_sum = 10 - rem if rem != 0 else 0
    return number if check_sum == check else False
