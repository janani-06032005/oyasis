import random
import string


def main():
    print("###Password Generator###\n")

    inc_small_chars = input("1/5. Include Small Letters(0/1): ").strip()
    inc_cap_chars = input("2/5. Include Capital Letters(0/1): ").strip()
    inc_digits = input("3/5. Include Integers(0/1): ").strip()
    inc_special_char = input("4/5. Include Special Characters(0/1): ").strip()

    inc_pattern = inc_small_chars + inc_cap_chars + inc_digits + inc_special_char
    if inc_pattern == "0000":
        print("\nNothing selected to create password.")
        return

    pass_len = int(input("5/5. Max Length Of Password: "))

    password_generator(pass_len, inc_pattern)

    print("END")
    return


def password_generator(pass_len, inc_pattern):
    password = ""
    chars = pass_len

    # getting occurances of each included character
    occur_small_chars = 0
    occur_cap_chars = 0
    occur_digits = 0
    occur_special_chars = 0

    if int(inc_pattern[0]) == 1:
        occur_small_chars = random.randint(0, chars)
        chars = chars - occur_small_chars

    if int(inc_pattern[1]) == 1:
        occur_cap_chars = random.randint(0, chars)
        chars = chars - occur_cap_chars

    if int(inc_pattern[2]) == 1:
        occur_digits = random.randint(0, chars)
        chars = chars - occur_digits

    if int(inc_pattern[3]) == 1:
        occur_special_chars = random.randint(0, chars)
        chars = chars - occur_special_chars

    # creating password
    password = (
        password
        + "".join(random.sample(string.ascii_lowercase, k=occur_small_chars))
        + "".join(random.sample(string.ascii_uppercase, k=occur_cap_chars))
        + "".join(random.sample(string.digits, k=occur_digits))
        + "".join(random.sample(string.punctuation, k=occur_special_chars))
    )

    # shuffling the characters
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    print("\nPassword: ", password)

    action = input("Recreate Password?(0/1): ")
    if action == "1":
        password_generator(pass_len, inc_pattern)

    return


main()