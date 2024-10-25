# Lab 5

# AI/SageMaker/Machine learning model (Lab 8) 
Steps for using SageMaker:
- install libraries for running jupyter notebooks and training
  - install and run jupyter notebooks
  - install ipykernel for jupyter to run python code
  - install libraries for training: sagemaker, pandas, numpy
- prepare a sagemaker session:
   - get the SageMaker execution role ARN
   - create a S3 bucket for holding input and output
- prepare dataset:
   - download, inspect, preprocess dataset (transform, create categorical variables, convert categorical variables to dummy variables, drop columns, convert boolean columns to numeric)
   - split into training, validation and test dataset
   - upload train and validation datasets to S3 bucket
- set up name and configuration (hyperparameters ranges, tuning strategy, total number of training jobs, max number of parallel jobs, metrics used for tuning) for the tuning job
- specify the machine learning algorithm used for tuning job (retrieve training image, specify S3 paths for datasets, define input data for training and validation channels, specify output location, define compute resou1rces, specify IAM role, static hyperparameters for the algorithm, stopping condition)
- launch the tuning job 

# AI/Comprehend/Rekognition (Lab 9)
**Entities**: pieces of information extracted from texts. They are _objects, concepts, or categories_ such as places, organisations, names, dates, and quantities. For example, "Sam was born in France," "Sam" is a person, "France" is location. These are entities in this sentence.

**Keyphrases**: meaningful *pieces of text* that capture the *main ideas* of a paragraph or article. They are generally nouns, verbs or phrases that summarise key concepts or central topics in the text. For example, in a sentence about cats' daily routine, the key phrases might be "cat", "sleep", "eat", "play" and "grooming".

**Syntaxes**: the rules of how words are arranged to form sentences. It is about the structure of sentences and determines how different parts of speech, e.g. nouns, verbs, pronouns and adjectives combine to convey clear messages. For example, in the sentence "The cat is cute", "cat" is the subject, "is" is the verb, "cute" is the adjective. This sentence follows the basic structure "subject + linking verb + predicate adjective".

**How to use Rekognition**:
- create S3 bucket and upload images to it
- perform operations like detect_labels, detect_moderation_labels, detect_faces, detect_text.

s3.upload_file(Filename, Bucket, Key): (local file path, bucket name, destination path in S3)

