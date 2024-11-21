def words_generator(count: int):
    if count > 10_000 or count <= 0:
        raise ValueError("Count must be less than 10000 and greater than 0.")
    with open("unique_words.txt", "r") as file:
        while count > 0:
            count = count - 1
            yield file.readline().strip()
