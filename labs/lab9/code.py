import boto3
import pycountry

client = boto3.client('comprehend')


def get_language_name(language_code):
    try:
        # Look up the language by its ISO 639-1 code
        language = pycountry.languages.get(alpha_2=language_code)
        return language.name if language else 'Unknown Language'
    except KeyError:
        return 'Unknown Language'


def detect_language(text):
    response = client.detect_dominant_language(Text=text)
    for language in response['Languages']:
        language_code = language['LanguageCode']
        confidence = round(language['Score']*100, 0)
        language = get_language_name(language_code)
        print(f'{language} detected with {confidence:.0f}% confidence')
    return 


def main():
    text = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."
    detect_language(text)


if __name__ == "__main__":
    main()