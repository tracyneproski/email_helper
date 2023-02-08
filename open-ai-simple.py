import openai   #pip install openai
import json

# Read the JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Extract the OpenAI API key from the config file
api_key = config['open-ai']

# Set the OpenAI API key
openai.api_key = api_key

def query(job, company):
    # Use the OpenAI API to generate a letter
    prompt = f'Write a polite letter as an applicant for the job position "{job}" at the company "{company}" using a semi-professional tone. The letter should be about 125 words long.'
    completions = openai.Completion.create(engine="code-davinci-002", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.3)

    # Extract the description from the response
    response = completions.choices[0].text

    return response

job = "full-stack developer"
company = "google"


letter = query(job, company)

print(f'Result: {letter}')