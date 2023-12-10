
from datetime import datetime
from app.modules.messages_module import Messages
from app.modules.chatgpt_module import ChatGPT
from app.supported_media import Multimedia
from app.modules.parser_module import Parser

def get_user_picks() -> list[(list[str], Multimedia)]:
    return [
        (Parser.get_user_input(Messages.get_media_msg(i)), i)
        for i in Multimedia
    ]

def package_favs(favs: list[(list[str], Multimedia)], summary=False) -> str:
    msgs = []
    for (media, cat) in favs:
        msg = f"{cat.msg_format()}:" if summary else Messages.get_chatgpt_msg(cat)
        msgs.append(Parser.generate_fav_list(media, msg))
    return '\n'.join(msgs)

def get_recom_choices() -> list[Multimedia]:
    recom_options = Parser.get_user_input(msg=Messages.ask_recommendations(), validate_function=Multimedia.validate_option)
    return [Multimedia(int(r)) for r in recom_options]

def get_chatgpt_recom(picks: list[Multimedia]) -> list[str]:
    if len(picks) == 0:
        return [client.ask_recom(Messages.get_recm_msg())]

    return [client.ask_recom(Messages.get_recm_msg(pick)) for pick in picks]

def print_session_summary(favs: list[str], summary: list[str]) -> None:
    prepared = package_favs(favs, True)
    recomms = '\n'.join(summary)

    print("Here's a brief summary of this session!")
    print("These were your chosen picks to get recommended on:")
    print(prepared)
    print("These were the recommendations you were given by our expert:")
    print(recomms)

def save_recommendations(recoms: list[str]) -> None:
    print("Saving recommendations to recommendations.txt")
    with open('recommendations.txt', 'w') as f:
        f.write(f"Recommendations for {datetime.now()}:\n")
        for r in recoms:
            f.write(r)
            f.write('\n')
    print('Your recommendations have been saved!')

if __name__ == '__main__':
    client = ChatGPT()

    print(Messages.welcome_message())
    print(client.opening_message())
    print('------\n')
    print(Messages.ask_about_user())
    fav_media = Parser.filter_empty_picks(get_user_picks())

    fav_msg = package_favs(fav_media)
    print("Now let's see what the expert says about your favourite media!")
    print("This may take a few seconds, so wait a little please")
    print(client.tell_list(fav_msg))

    choices = get_recom_choices()
    print("Please wait a few seconds while we get our expert's recommendations!")
    recommendations = get_chatgpt_recom(choices)
    for i in recommendations:
        print(i)

    summary = Parser.clean_recommendations(recommendations, choices)
    save_opt = Parser.get_user_input(Messages.saving_message(), 1, Parser.validate_saving_option)[0].lower()
    if save_opt == 'y' or save_opt == 'yes':
        save_recommendations(summary)

    print_session_summary(fav_media, summary)
    print('\n------')
    print(Messages.closing_message())
    print(client.closing_message())
