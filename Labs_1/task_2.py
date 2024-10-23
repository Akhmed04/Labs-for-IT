# TODO Найдите количество книг, которое можно разместить на дискете
len_books = 4 * 25 * 50 * 100
max_len = 1024 * 1024 * 1.44
len_in_one = 0
while (int(max_len) > len_books):
    max_len -= len_books
    len_in_one += 1

print("Количество книг, помещающихся на дискету:", len_in_one)
