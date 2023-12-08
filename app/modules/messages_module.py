from app.supported_media import Multimedia
class Messages:

    @staticmethod
    def welcome() -> str:
        return """Welcome to Procrastinator!
We'll give you some media recommendations based on your existing preferences.
Right now we only support Movies, TV Shows, Videogames, Artists / Bands, and Anime recommendations.
To provide you with the best possible choices to procrastinate on, we brought in an expert:
Just beware, he only knows about stuff up to 2022!
He hasn't been up to date with the latest, but hopefully with the greatest he has.
"""

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
        return "What about your picks for TV shows."

    @staticmethod
    def anime_user() -> str:
        return "And what about anime."

    @staticmethod
    def music_user() -> str:
        return "Any bands or artists that you danced to?"

    @staticmethod
    def videogame_user() -> str:
        return "Finally, have you been playing any videogames recently? Or maybe your favorites."

    @staticmethod
    def save_recommendations() -> str:
        return """Would you like to save the recommendations to a text file?
That way you can add everything to your Wish lists!
"""

    @staticmethod
    def ask_recommendations() -> str:
        return f"""What is something you would like a recommendation on?
Choose up to 3 of the following options.
    - Enter the numbers separated by a comma
Or you can leave it empty to get a general recommendation.
{Multimedia.formatted()}
"""

    @staticmethod
    def closing() -> str:
        return """Hope you enjoyed your recommendations.
And that you have something to add to your favourite catalog!
Feel free to come back anytime.
"""

    @staticmethod
    def get_media_msg(media: Multimedia) -> str:
        match media:
            case Multimedia.TV_SHOW:
                return Messages.shows_user()
            case Multimedia.MUSIC:
                return Messages.music_user()
            case Multimedia.ANIME:
                return Messages.anime_user()
            case Multimedia.MOVIE:
                return Messages.movie_user()
            case Multimedia.VIDEOGAME:
                return Messages.videogame_user()
