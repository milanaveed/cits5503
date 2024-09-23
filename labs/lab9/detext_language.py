import boto3
import pycountry
import math

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
        confidence = math.floor(language['Score']*100)
        language = get_language_name(language_code)
        print(f'{language} detected with {confidence}% confidence')
    return 


def main():
    # text = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."
    # detect_language(text)
    print("Detecting language of the text1:")
    english_text = "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799."
    detect_language(english_text) 

    print("Detecting language of the text2:")
    spanish_text = "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha."
    detect_language(spanish_text)

    print("Detecting language of the text3:")
    french_text = "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir"
    detect_language(french_text)

    print("Detecting language of the text4:")
    italian_text = "L'amor che move il sole e l'altre stelle."
    detect_language(italian_text)


if __name__ == "__main__":
    main()