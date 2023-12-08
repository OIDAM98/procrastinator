from enum import Enum

class Multimedia(Enum):
    TV_SHOW = 1
    MUSIC = 2
    ANIME = 3
    MOVIE = 4
    VIDEOGAME = 5
    @classmethod
    def validate_option(cls, response: str) -> bool:
        return response.isdigit() and int(response) in [i.value for i in Multimedia] 
    
    @classmethod
    def formatted(cls) -> str:
        fmt = [f"[{m.value}] {m.name.replace('_', ' ')}S" for m in Multimedia]
        return '\n'.join(fmt)
