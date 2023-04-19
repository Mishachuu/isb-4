import hashlib

OPTIONS = {
    'hash': '70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473',
    'initial_digits': '446674',
    'last_digits': '1378',
}


def check_hash(x: int) -> int:
    """Функция, которая проверяет соответствие хеша надйенного числа, с данным нам хешем

    Args:
        x (int): номер карты

    Returns:
        int: номер карты
    """
    return x if hashlib.sha256(f'{OPTIONS["initial_digits"]}{x}{OPTIONS["last_digits"]}'.encode()).hexdigest() == f'{OPTIONS["hash"]}' else False


def algorithm_luna(number: int) -> bool:
    """функция, которая проверяет номер карты используя алгоритм Луна

    Args:
        number (int): номер

    Returns:
        bool: соответствует/не соответствует
    """
    number = str(number)
    if len(number) != 6:
        return False
    check = 8
    bin = [int(i) for i in OPTIONS['initial_digits']]
    code = [int(i) for i in number]
    end = [int(i) for i in OPTIONS['last_digits']]
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
