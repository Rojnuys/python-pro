import random
import string


class PwdGenerator:
    @staticmethod
    def _check_length(min_length, max_length):
        if min_length < 1:
            raise ValueError("min_length must be greater or equal than 1")
        if min_length > max_length:
            raise ValueError("min_length must be less or equal than max_length")

    @staticmethod
    def _calculate_length(min_length, max_length):
        return random.randint(min_length, max_length)

    @staticmethod
    def get_random_symbol():
        return random.choice(string.ascii_letters + string.digits + string.punctuation)

    @staticmethod
    def _hard_base():
        return [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]

    @classmethod
    def easy(cls, min_length = 6, max_length = 10):
        cls._check_length(min_length, max_length)
        pwd_length = cls._calculate_length(min_length, max_length)
        return "".join([cls.get_random_symbol() for _ in range(pwd_length)])

    @classmethod
    def hard(cls, min_length = 6, max_length = 10):
        cls._check_length(min_length, max_length)
        if min_length < 6:
            raise ValueError("min_length for hard password must be greater or equal than 6")
        pwd_length = cls._calculate_length(min_length, max_length)
        pwd = cls._hard_base() + [cls.get_random_symbol() for _ in range(pwd_length - 4)]
        random.shuffle(pwd)
        return "".join(pwd)
