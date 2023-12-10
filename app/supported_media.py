from enum import Enum

class Multimedia(Enum):
    """
    Enumeration used for the supported media for the application.
    """
    TV_SHOW = 1
    MUSIC = 2
    ANIME = 3
    MOVIE = 4
    VIDEOGAME = 5
    def msg_format(self) -> str:
        """
        Get a human-readable formatted version of the multimedia category.

        Returns:
        - str: The formatted multimedia category name.
        """
        return self.name.replace('_', ' ').capitalize()
    
    @classmethod
    def categories(cls) -> str:
        """
        Get a formatted string listing all supported multimedia categories.

        Returns:
        - str: A comma-separated string listing multimedia categories.
        """
        return ', '.join([i.msg_format() for i in Multimedia])

    @classmethod
    def validate_option(cls, response: str) -> bool:
        """
        Validate if a given response corresponds to a valid multimedia category option.

        Parameters:
        - response (str): The user's response.

        Returns:
        - bool: True if the response is a valid multimedia category option, False otherwise.
        """
        return response.isdigit() and int(response) in [i.value for i in Multimedia] 
    
    @classmethod
    def formatted(cls) -> str:
        """
        Get a formatted string listing all multimedia categories with their corresponding values.

        Returns:
        - str: A formatted string listing multimedia categories with values.
        """
        fmt = [f"[{m.value}] {m.name.replace('_', ' ')}S" for m in Multimedia]
        return '\n'.join(fmt)

