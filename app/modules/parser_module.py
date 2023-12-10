import re
from app.supported_media import Multimedia
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

    @staticmethod
    def validate_saving_option(opt: str) -> bool:
        return opt.lower() in ('yes', 'no', 'n', 'y')

    @staticmethod
    def clean_recommendations(recommendations: list[str], choices: list[Multimedia]) -> list[str]:
        if len(choices) == 0:
            return Parser._clean_general_recommendations(recommendations)

        return Parser._clean_specific_recommendations(recommendations, choices)
    
    @staticmethod
    def _clean_specific_recommendations(recommendations: list[str], choices: list[Multimedia]) -> list[str]:
        regex = r"\d\."
        clean_recoms = []
        zipped = zip(choices, recommendations)
        for (cat, r) in zipped:
            lines = r.split('\n\n')
            only_recoms = filter(lambda x: re.match(regex, x), lines)
            remove_numbers = map(lambda l: l[3:], only_recoms)
            clean_recoms.append(f"{cat.msg_format()}:")
            for c in remove_numbers:
                clean_recoms.append(f"- {c}")
        
        return clean_recoms
    
    @staticmethod
    def _clean_general_recommendations(recommendations: list[str]) -> list[str]:
        clean_recoms = []
        for r in recommendations:
            lines = r.split('\n\n')[1:-1]
            items = list(map(lambda l: l.split('\n'), lines))
            for [cat, *recoms] in items:
                remove_numbers = map(lambda l: l[3:], recoms)
                clean_recoms.append(cat)
                for c in remove_numbers:
                    clean_recoms.append(f"- {c}")
        
        return clean_recoms