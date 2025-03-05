def main():
    print("Hello from python-dsa!")
    print("This is the infinite monkey theorem.")
    print("The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare.")
    print("In this case, we will use a random generator to simulate the monkeys.")
    print("The monkeys will generate random strings until they generate the target string.")

    import random
    import string           # Import the string module

    goal_string = "methinks it is like a weasel"

    def generate_string():
        return "".join(random.choices(string.ascii_lowercase + " ", k=len(goal_string)))
    

    def compare_string_with_goal_string(random_string, best_string_so_far):
        best_string_so_far = list(best_string_so_far)
        for i in range(len(goal_string)):
            if random_string[i] == goal_string[i]:
                best_string_so_far[i] = random_string[i]
        return "".join(best_string_so_far)
    
    #     return sum([1 for i in range(len(goal_string)) if string[i] == goal_string[i]])
    


    def go_through_attempts():
        attempts = 0
        best_string_so_far = '____________________________'
        while True:
            attempts += 1
            random_string = generate_string()
            best_string_so_far = compare_string_with_goal_string(random_string, best_string_so_far)
            if best_string_so_far == goal_string:
                print(f"Attempt {attempts}: {best_string_so_far}")
                break
            else:
                print(f"Attempt {attempts}: {best_string_so_far}")
        return attempts
    
    go_through_attempts()


if __name__ == "__main__":
    main()
