# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# >>> func("papa")
# 6
# >>> func("sova")
# 9


from hashlib import sha1


def substrings(data):
    hash_list = [sha1(bytes(data, encoding='utf-8')).hexdigest()]
    cnt = 0
    for i in range(len(data)):
        substr = ''
        for j in range(i, len(data)):
            substr += data[j]
            if sha1(bytes(substr, encoding='utf-8')).hexdigest() not in hash_list:
                hash_list.append(sha1(bytes(substr, encoding='utf-8')).hexdigest())
                cnt += 1
    return cnt


print(substrings('sova'))
print(substrings('papa'))

# не уверена, правильно ли я поняла задание
