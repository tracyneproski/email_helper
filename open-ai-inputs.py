import openai   #pip install openai
import json

# Read the JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Extract the OpenAI API key from the config file
api_key = config['open-ai']

# Set the OpenAI API key
openai.api_key = api_key

def query(to, tone, reason1, reason2, reason3, additionalContext, intendedResult):
    # Use the OpenAI API to generate a letter
    prompt = f'Please write a "{tone}" email to "{to}" about "{reason1}" and "{reason2}" and "{reason3}". Here is some extra context: "{additionalContext}". I hope to achieve "{intendedResult}" with this email.'
    completions = openai.Completion.create(engine="code-davinci-002", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.3)

    # Extract the description from the response
    response = completions.choices[0].text

    return response

# Prompt the user for the job position and company name
print("\nThis script will help you write an email. Please follow the prompts.\n\n")
to = input("To: ")
tone = input("Tone: ")
reason1 = input("Reason 1: ")
reason2 = input("Reason 2: ")
reason3 = input("Reason 3: ")
additionalContext = input("Additional Context: ")
intendedResult = input("Intended Result: ")


letter = query(to, tone, reason1, reason2, reason3, additionalContext, intendedResult)

print(f'Result: {letter}')