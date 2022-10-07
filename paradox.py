import random


def monty_hall(iter_count):
    with_change = 0
    without_change = 0
    for i in range(0, iter_count):
        variants = [1, 2, 3]
        correct_answer = random.randrange(1, 4)
        choose_variant = random.randrange(1, 4)
        delete_variant = random.randrange(1, 4)
        while delete_variant == correct_answer or delete_variant == choose_variant:
            delete_variant = random.randrange(1, 4)
        variants.remove(delete_variant)
        variants.remove(choose_variant)
        new_choose_variant = variants[0]
        if new_choose_variant == correct_answer:
            with_change += 1
        if choose_variant == correct_answer:
            without_change += 1
    return with_change / iter_count * 100, without_change / iter_count * 100


def birthday(iter_count):
    coincident_count = 0
    for i in range(0, iter_count):
        birthday_list = []
        for j in range(0, 23):
            birthday_list.append(random.randrange(1, 337))
        for n, birthday_value in enumerate(birthday_list):
            coincidence_found = False
            for k, check_birthday_value in enumerate(birthday_list):
                if n == k:
                    continue
                if birthday_value == check_birthday_value:
                    coincident_count += 1
                    coincidence_found = True
                    break
            if coincidence_found:
                break

    return coincident_count / iter_count * 100
