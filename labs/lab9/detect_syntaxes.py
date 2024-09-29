import boto3

# Create a client to interact with AWS Comprehend
client = boto3.client('comprehend')

# Function to detect syntaxes in a given text in a specific language
def detect_syntaxes(text, language_code):
    response = client.detect_syntax(Text=text, LanguageCode=language_code)
    syntaxes = response['SyntaxTokens']
    
    # Print the first 60 characters of the text to provide context in the output
    print(f"Text: {text[:60]}...")
    
    # Print each syntax token detected in the text
    for syntax in syntaxes:
        print(f"Token: {syntax['Text']}, Part of Speech: {syntax['PartOfSpeech']['Tag']}, Confidence: {syntax['PartOfSpeech']['Score']:.2f}")
    
    print('-' * 80)
    return response

def main():
    # Sample texts in different languages, each with an associated language code
    texts = [
        {"text": "The French Revolution was a period of social and political upheaval in France and its colonies beginning in 1789 and ending in 1799.", "language": "en"},
        {"text": "El Quijote es la obra más conocida de Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso hidalgo don Quijote de la Mancha a comienzos de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. En 1615 aparecería la segunda parte del Quijote de Cervantes con el título de El ingenioso caballero don Quijote de la Mancha.", "language": "es"},
        {"text": "Moi je n'étais rien Et voilà qu'aujourd'hui Je suis le gardien Du sommeil de ses nuits Je l'aime à mourir Vous pouvez détruire Tout ce qu'il vous plaira Elle n'a qu'à ouvrir L'espace de ses bras Pour tout reconstruire Pour tout reconstruire Je l'aime à mourir", "language": "fr"},
        {"text": "L'amor che move il sole e l'altre stelle.", "language": "it"}
    ]

    # Loop through each text and detect its key phrases
    for instance in texts:
        detect_syntaxes(instance["text"], instance["language"])

if __name__ == "__main__":
    main()