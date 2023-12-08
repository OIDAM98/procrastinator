class Parser:
    @staticmethod
    def get_user_picks(msg: str) -> list[str]:
        inputs = []
        print(msg)
        while len(inputs) < 3:
            user_input = input()
            if user_input == '':
                break
            else:
                inputs.append(user_input.strip())
        return inputs
