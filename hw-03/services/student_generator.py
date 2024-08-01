from faker import Faker


def generate_student():
    faker = Faker()
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "password": faker.password(),
        "birthday": faker.date_of_birth(minimum_age=18, maximum_age=60).strftime("%m/%d/%Y"),
    }
