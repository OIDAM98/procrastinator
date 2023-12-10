import re
from app.supported_media import Multimedia
class Parser:
    """
    Class for interactions with User using the commandline.
    Intended to both get inputs and validate them depending on the context of each one.
    """
    @staticmethod
    def get_user_input(msg: str, max=3, validate_function = None) -> list[str]:
        """
        Gets user input in a list format. The max argument defines the maximum number of
        responses that the user can give, and the length of the return.
        
        Args:
        - msg (str): Message to be printed out to user.
        - max (int): Maximum number of responses a user can give. This number must be greater than 0.
        - validate_function (str -> bool): Optional validation function to check if user input is valid.

        Returns:
        - list[str]: User input in a list form.

        """
        if max <= 0:
            raise ValueError('max argument must be greater than 0')
        inputs = []
        print(msg)
        while len(inputs) < max:
            user_input = input("> ").strip()
            if user_input == '':
                break
            elif validate_function:
                if validate_function(user_input) == False:
                    print("You entered an invalid choice. Try again.")
                    continue
            inputs.append(user_input)
        return inputs

    @staticmethod 
    def filter_empty_picks(picks: list[(list[str], Multimedia)]) -> list[(list[str], Multimedia)]:
        """
        Removes the empty picks from a given list of choices.
        This happens because an empty list of picks on any category of media
        is due to the user not choosing to get recommendations for it.
        
        Args:
        - picks (list[(list[str], any)]): List of inputs given by the user by each category.

        Returns:
        - list[(list[str], any)]:

        """
        def not_empty_pick(pick: (list[str], any)):
            return len(pick[0]) > 0
        return list(filter(not_empty_pick, picks))

    @staticmethod
    def generate_fav_list(input: list[str], msg: str) -> str:
        """
        Formats a given list of picks from the user and a message header.
        Intended format is the following:
        '{msg}
        - {input[0]}
        - {input[1]}
        ...
        '
        Meant to be used as message for OpenAI API interaction.

        Args:
        - input (list[str]): 
        - msg (str): Message to be used as header of the format.

        Returns:
        - str: String of formatted message.

        """
        def choices_to_chatgpt(choices: list) -> list[str]:
            return list(map(lambda x: f"- {x}", choices))
        prepared_lst = [msg, *choices_to_chatgpt(input)]
        return '\n'.join(prepared_lst)

    @staticmethod
    def validate_saving_option(opt: str) -> bool:
        """
        Used to verify if the input given is one of the following options:
        - Yes
        - No
        - Y
        - N
        
        Args:
        - opt (str): Input from the user.

        Returns:
        - bool: If the input is one of the valid options.

        """
        return opt.lower() in ('yes', 'no', 'n', 'y')

    @staticmethod
    def clean_recommendations(recommendations: list[str], choices: list[Multimedia]) -> list[str]:
        """
        Clean the message recommendations from OpenAI API to get only the recommendation part.
        Meant to be used as both a summary of the session and as saving input.
        Depending on the size of the recommendation choices that the user selected, will be the
        cleaning strategy, as the OpenAI API response is different if the user wanted specific
        recommendations or a more general one.
        
        Args:
        - recommendations (list[str]):
        - choices (list[Multimedia]): 

        Returns:
        - list[str]: List of only the recommendations given by OpenAI API and their multimedia categories.

        """
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