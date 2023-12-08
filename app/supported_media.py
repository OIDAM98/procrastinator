from enum import Enum

class Multimedia(Enum):
    TV_SHOW = 1
    MUSIC = 2
    ANIME = 3
    MOVIE = 4
    VIDEOGAME = 5
    @classmethod
    def validate_option(cls, response: str) -> bool:
        return response.isdigit() and int(response) > 0 and int(response) < 5
    @classmethod
    def parse_option(cls, response: str):
        match response:
            case "1":
                return Multimedia.TV_SHOW
            case "2":
                return Multimedia.MUSIC
            case "3":
                return Multimedia.ANIME
            case "4":
                return Multimedia.MOVIE
            case "5":
                return Multimedia.VIDEOGAME
        
