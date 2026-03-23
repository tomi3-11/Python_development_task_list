import random 

def main():
    secret = secret_number()
    attempt = 0
    max_attempt = 5
    while True:
        guess = int(input("Guess: "))

        if guess == secret:
            print("Congratulations.")
            attempt += 1
            break
        elif guess < secret:
            print("Too low")
            attempt += 1
        elif guess > secret:
            print("Too high")
            attempt += 1

        if attempt >= max_attempt:
            print("You have exeeded the maximum allowed attempts.")
            print(f"\nThe secret number was {secret}.")
            break


def secret_number():
    secret = random.randint(1, 100)

    return secret


if __name__ == "__main__":
    main()
