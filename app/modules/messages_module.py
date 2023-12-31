from app.supported_media import Multimedia

class Messages:

    @staticmethod
    def welcome_message() -> str:
        return _WELCOME
    
    @staticmethod
    def ask_about_user() -> str:
        """
        Get a message prompting the user for their multimedia choices.

        Returns:
        - str: The message asking the user about their multimedia picks.
        """
        return _ASK_ABOUT_USER
    
    @staticmethod
    def ask_recommendations() -> str:
        """
        asdfsdf
        """
        return _ASK_RECOMMENDATIONS.format(Multimedia.formatted())

    @staticmethod
    def closing_message() -> str:
        return _CLOSING

    @staticmethod
    def saving_message() -> str:
        """
        Returns the message to be displayed when asking the user to save the recommendations.
        """
        return _SAVE_RECOMMENDATIONS

    @staticmethod
    def get_media_msg(media: Multimedia) -> str:
        """
        Get a user-specific message for a given multimedia category.

        Parameters:
        - media (Multimedia): The multimedia category for which the user-specific message is requested.

        Returns:
        - str: The user-specific message.

        Raises:
        - ValueError: If the provided multimedia category is not supported.
        """
        match media:
            case Multimedia.TV_SHOW:
                return _SHOWS_USER
            case Multimedia.MUSIC:
                return _MUSIC_USER
            case Multimedia.ANIME:
                return _ANIME_USER
            case Multimedia.MOVIE:
                return _MOVIE_USER
            case Multimedia.VIDEOGAME:
                return _VIDEOGAME_USER
            case _:
                raise ValueError(f"Unsupported multimedia category: {media}")

    @staticmethod
    def get_chatgpt_msg(media: Multimedia) -> str:
        """
        Get a message related to send to ChatGPT for a specific multimedia category.

        Parameters:
        - media (Multimedia): The multimedia category for which the ChatGPT message is requested.

        Returns:
        - str: The ChatGPT message.

        Raises:
        - ValueError: If the provided multimedia category is not supported.
        """
        match media:
            case Multimedia.TV_SHOW:
                return _SHOWS_CHATGPT
            case Multimedia.MUSIC:
                return _MUSIC_CHATGPT
            case Multimedia.ANIME:
                return _ANIME_CHATGPT
            case Multimedia.MOVIE:
                return _MOVIE_CHATGPT
            case Multimedia.VIDEOGAME:
                return _VIDEOGAME_CHATGPT
            case _:
                raise ValueError(f"Unsupported multimedia category: {media}")

    @staticmethod
    def get_recm_msg(media: Multimedia = None) -> str:
        """
        Generate a recommendation message based on the specified multimedia category.
        
        Args:
        - media (Multimedia): Multimedia category for which a recommendation is requested.
        If None, a general recommendation for all categories will be provided.

        Returns:
        - (str): The recommendation message.

        """
        msg = "Using the same list that I gave you, can you now recommend me something"
        ending = "please? At least 3 or 4 things"
        if media == None:
            return f"{msg} in {Multimedia.categories()} to consume, {ending} per category."
        else:
            return f"{msg} specific to {media.msg_format()}, {ending}."

# Private constants for the module

_WELCOME = """Welcome to Procrastinator!
We'll give you some media recommendations based on your existing preferences.
Right now we only support Movies, TV Shows, Videogames, Artists / Bands, and Anime recommendations.
To provide you with the best possible choices to procrastinate on, we brought in an expert:
Just beware, he only knows about stuff up to 2022!
He hasn't been up to date with the latest, but hopefully with the greatest he has.
"""

_ASK_ABOUT_USER = """Tell me a bit more about you.
What have you been recently consuming or
about your favorite picks in general!
You can leave it empty if you don't want any recommendation
based on that category.
You can enter at most 3 picks for each category.
Press enter after each one to confirm your choice.
"""

_MOVIE_USER = "Tell me a bit more about movies."
_SHOWS_USER = "What about your picks for TV shows."
_ANIME_USER = "And what about anime."
_MUSIC_USER = "Any bands or artists that you danced to?"
_VIDEOGAME_USER = "Finally, have you been playing any videogames recently? Or maybe your favorites."

_MOVIE_CHATGPT = "These are the movies I have enjoyed:"
_SHOWS_CHATGPT = "These are the TV shows that I have enjoyed:"
_ANIME_CHATGPT = "These are the Anime shows that I have enjoyed:"
_MUSIC_CHATGPT = "Here are some bands or artists I have enjoyed:"
_VIDEOGAME_CHATGPT = "Here are some videogames that I have enjoyed:"

_ASK_RECOMMENDATIONS = """What is something you would like a recommendation on?
Choose up to 3 of the following options.
Or you can leave it empty to get a general recommendation.
{0}
"""

_SAVE_RECOMMENDATIONS = """Would you like to save the recommendations to a text file?
That way you can add everything to your Wish lists!
Enter either [y/n] or [Yes/No]
"""
_CLOSING = """Hope you enjoyed your recommendations.
And that you have something to add to your favourite catalog!
Feel free to come back anytime.
"""
