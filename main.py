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
    advice = list()

    for _ in range(0, 50):
        r = requests.get('https://api.adviceslip.com/advice')
        advice.append(str(r.json()))

    print(f"most common advice: {find_most_popular_advice(advice)}")


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
    headers = {"Authorization": "Bearer 80b4ffd09ed8d997433f36a621dc9d62"}

    lang_samples = ["Përshendetje Botë", "Русский компьютер", "Ahoj světe",
                    "ਕੰਪਿਊਟਰ ਵਿਗਿਆਨ", "مرحبا بالعالم", "Labas pasauli",
                    "Привет мир", "ਯੇਅ ਨਿਊ ਸ਼ੁਰੂਆਤ", "ہیلو دنیا",
                    "Salam dünya", "नमस्कार संसार", "Halló heimur",
                    "Беларускія Кампутарныя", "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ",
                    "Прывітанне Сусвет"]

    lang_results = list()
    for ls in lang_samples:
        r = requests.post('https://ws.detectlanguage.com/0.2/detect',
                          headers=headers, params=format_lang_string(ls))
        abbr = get_lang_abbr_from_resp(r)
        lang_results.append((ls, lang_abbr_map[abbr]))

    return lang_results


def get_lang_abbr_from_resp(http_resp):
    """
    This function takes a requests object containing a response from
    detectlanguage.com, parses it, and returns the abbreviation of
    the language detected.
    """
    return http_resp.json()["data"]["detections"][0]["language"]


def find_language_appearing_most(lang_results):
    abbrs = [x[1] for x in lang_results]
    most_freq_abbr = max(abbrs, key=lambda x: abbrs.count(x))
    return [x for x in lang_results if x[1] == most_freq_abbr]


if __name__ == "__main__":

    get_advice()
    print(find_language_appearing_most(post_language_samples()))
