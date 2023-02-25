import openai
import re
import os
from dotenv import load_dotenv



openai.api_key = "insert api key"

# Open the file and read its contents
with open('summary.txt', 'r') as file:
    data = file.read()

# Convert the data to a string
text = str(data)

# Set up the OpenAI GPT-3 model and prompt
model_engine = "text-davinci-002"
prompt = "Identify the key points in the following text based on the heading:\n\n" + text

# Set up the OpenAI API request
response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.5,
)

# Extract the key points from the API response
key_points = []
for choice in response.choices:
    text = choice.text
    key_points += re.findall("[^\n]+", text)

# Print the identified key points
print("Key Points: ")
for key_point in key_points:
    print("- " + key_point)