class Parser:
    @staticmethod
    def get_user_input(msg: str, max=3, validate_function=None) -> list[str]:
        inputs = []
        print(msg)
        while len(inputs) < max:
            user_input = input("> ")
            if user_input == '':
                break
            elif validate_function:
                if validate_function(user_input) == False:
                    print("You entered an invalid choice. Try again.")
                    continue
            inputs.append(user_input.strip())
        return inputs
