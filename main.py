import requests


def create_lang_abbr_map():
    """
    This function creates a dictionary that maps language abbreviations,
    "codes", used by detectlanguage.com to full language names.
    """
    r = requests.get("https://ws.detectlanguage.com/0.2/languages")
    return {x["code"]: x["name"] for x in r.json()}


lang_abbr_map = create_lang_abbr_map()


def get_advice():
    pass
    # remove `pass` and [FILL IN HERE]


def find_most_popular_advice(advice_list):
    """
    The `key` parameter of the `max` function takes a function to be
    applied to each element in the list. The `max` function then
    applies the key function to each element in the list with the higest
    result of the application of the key function.
    """
    return max(advice_list, key=lambda x: advice_list.count(x))


def format_lang_string(lang_str):
    """
    This function formats a string to be a parameter in a POST request
    to https://detectlanguage.com
    """
    lang_str = lang_str.replace(' ', '+')
    lang_str = 'q=' + lang_str
    return lang_str


def post_language_samples():
    headers = {"Authorization": "Bearer [REDACTED]"}
    lang_samples = ["Përshendetje Botë", "Русский компьютер", "Ahoj světe",
                    "ਕੰਪਿਊਟਰ ਵਿਗਿਆਨ", "مرحبا بالعالم", "Labas pasauli",
                    "Привет мир", "ਯੇਅ ਨਿਊ ਸ਼ੁਰੂਆਤ", "ہیلو دنیا",
                    "Salam dünya", "नमस्कार संसार", "Halló heimur",
                    "Беларускія Кампутарныя", "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ",
                    "Прывітанне Сусвет"]
    # [FILL IN HERE]


def get_lang_abbr_from_resp(http_resp):
    """
    This function takes a requests object containing a response from
    detectlanguage.com, parses it, and returns the abbreviation of
    the language detected.
    """
    return http_resp.json()["data"]["detections"][0]["language"]


if __name__ == "__main__":
    pass
    # Remove `pass` and [FILL IN HERE]

