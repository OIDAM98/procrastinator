class Parser:
    @staticmethod
    def get_user_input(msg: str, max=3, validate_function=None) -> list[str]:
        if max <= 0:
            raise ValueError('max argument must be greater than 0')
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

    @staticmethod 
    def filter_empty_picks(picks: list[(list[str], any)]):
        def not_empty_pick(pick: (list[str], any)):
            return len(pick[0]) > 0
        return list(filter(not_empty_pick, picks))

    @staticmethod
    def generate_fav_list(input: list[str], msg: str) -> str:
        def choices_to_chatgpt(choices: list) -> list[str]:
            return list(map(lambda x: f"- {x}", choices))
        prepared_lst = [msg, *choices_to_chatgpt(input)]
        return '\n'.join(prepared_lst)