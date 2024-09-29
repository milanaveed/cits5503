import boto3

# Create boto3 clients for S3 and Rekognition
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

# Define the S3 bucket and images
bucket_name = '22756463-lab9'  # Replace with your actual bucket name if different
images = ['images/urban.jpg', 'images/beach.jpg', 'images/faces.jpg', 'images/text.jpg']

# Function to analyze labels in the image
def detect_labels(image):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image}},
        MaxLabels=10
    )
    print(f"\nLabels detected in {image}:")
    for label in response['Labels']:
        print(f"{label['Name']} - {label['Confidence']:.2f}%")

# Function to check for inappropriate content in the image (moderation)
def detect_moderation_labels(image):
    response = rekognition.detect_moderation_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image}}
    )
    print(f"\nModeration labels detected in {image}:")
    if not response['ModerationLabels']:
        print("No inappropriate content detected.")
    for label in response['ModerationLabels']:
        print(f"{label['Name']} - {label['Confidence']:.2f}%")

# Function to perform facial analysis (e.g., emotion detection, gender, etc.)
def detect_faces(image):
    response = rekognition.detect_faces(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image}},
        Attributes=['ALL']
    )
    print(f"\nFacial analysis for {image}:")
    if not response['FaceDetails']:
        print("No faces detected.")
    for face in response['FaceDetails']:
        emotions = ', '.join([emotion['Type'] for emotion in face['Emotions'] if emotion['Confidence'] > 90])
        print(f"Face detected with emotions: {emotions}")
        print(f"Gender: {face['Gender']['Value']}")
        print(f"Age range: {face['AgeRange']['Low']} - {face['AgeRange']['High']}")

# Function to detect and extract text from the image
def detect_text(image):
    response = rekognition.detect_text(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image}}
    )
    print(f"\nText detected in {image}:")
    if not response['TextDetections']:
        print("No text detected.")
    for text in response['TextDetections']:
        if text['Type'] == 'LINE':
            print(f"Detected text: {text['DetectedText']}")

# Run analyses for each image
for image_name in images:
    print(f"\n--- Analyzing {image_name} ---")
    
    detect_labels(image_name)
    
    detect_moderation_labels(image_name)
    
    if 'faces' in image_name:
        detect_faces(image_name)  # Use facial analysis for the faces.jpg image
    
    if 'text' in image_name:
        detect_text(image_name)  # Use text extraction for the text.jpg image
