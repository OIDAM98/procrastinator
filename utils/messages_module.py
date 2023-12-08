
class Messages:

    @staticmethod
    def welcome() -> str:
        return """Welcome!"""

    @staticmethod
    def ask_about_user() -> str:
        return """Tell me a bit more about you.
What have you been recently consuming or
about your favorite picks in general!
You can leave it empty if you don't want any recommendation
based on that category.
You can enter at most 3 picks and press enter after each one to confirm it.
"""

    @staticmethod
    def movie_user() -> str:
        return "Tell me a bit more about movies."

    @staticmethod
    def shows_user() -> str:
        return "What about your picks for tv shows."

    @staticmethod
    def anime_user() -> str:
        return "And what about anime."

    @staticmethod
    def music_user() -> str:
        return "Any bands, songs or artists that you danced to?"

    @staticmethod
    def videogame_user() -> str:
        return "Finally, have you been playing recently? Or your favorites."

    @staticmethod
    def save_recommendations() -> str:
        return "Would you like to save the recommendations to a text file?"

    @staticmethod
    def ask_recommendations() -> str:
        return """What is somwthing you would like a recommendation on?
Choose up to 3 of the following options.
    - Enter the numbers separated by a comma
Or you can leave it empty to get a general recommendation.
[1] Anime
[2] Videogames
[3] Movies
[4] TV Shows
[5] Music
"""

    @staticmethod
    def closing() -> str:
        return """Hope you enjoyed your recommendations.
And that you have something to add to your favourite catalog!
Feel free to come back anytime.
"""