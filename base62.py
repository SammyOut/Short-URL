base62_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def encrypt_base62(index: int) -> str:
    result = []
    while index > 0:
        result.append(base62_string[index % 62])
        index //= 62

    return ''.join(result[::-1])


def decrypt_base62(encrypted: str) -> int:
    result = 0

    encrypted = encrypted[::-1]
    for i in range(len(encrypted)):
        result += (62 ** i) * base62_string.index(encrypted[i])

    return result
