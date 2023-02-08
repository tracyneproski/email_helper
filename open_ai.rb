require('dotenv').config()
console.log(process.env)
require 'openai'
require 'json'

# Load the configuration file
config_file = "config.json"
config = JSON.parse(File.read(config_file))

# Set the API key from the configuration file
OpenAI::API.api_key = config["api_key"]

# Use the `Completion` API to generate text
model_engine = "code-davinci-002"
prompt = "The future of AI is"
max_tokens = 1024
completions = OpenAI::Completion.create(
  engine: model_engine,
  prompt: prompt,
  max_tokens: max_tokens,
  n: 1,
  stop: "."
)

# Print the generated text
puts completions.choices.first.text
