import openai_secret_manager
import openai
import requests

# Set up the OpenAI API key
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

# Open the file and read its contents
with open('summary.txt', 'r') as file:
    data = file.read()

# Convert the data to a string
input_text = str(data)

# Define the Slides API request parameters
slides_engine = "davinci"
slides_prompt = (f"Create a PowerPoint presentation with the following slides:\n\n"
                 f"{input_text}\n\n"
                 f"The presentation should have a title slide and 2-3 content slides.")
slides_max_tokens = 2048
slides_n = 1
slides_stop = None
slides_temperature = 0.5

# Generate the PowerPoint slides using the Slides API
slides_response = openai.Completion.create(
    engine=slides_engine,
    prompt=slides_prompt,
    max_tokens=slides_max_tokens,
    n=slides_n,
    stop=slides_stop,
    temperature=slides_temperature
)

# Extract the generated slides from the API response
slides = [choice.text for choice in slides_response.choices]

# Define the URL for the PowerPoint template
template_url = "https://example.com/template.pptx"

# Define the URL for the generated PowerPoint slides
output_url = "https://example.com/output.pptx"

# Generate the final PowerPoint presentation by merging the template with the generated slides
response = requests.post(
    "https://api.mergeapi.com/v1/merge/pptx",
    headers={"Authorization": secrets["merge_api_key"]},
    json={
        "template": {"url": template_url},
        "data": {"slides": slides},
        "output": {"url": output_url},
    },
)

# Check if the merge request was successful
if response.status_code == 200:
    print("PowerPoint slides generated successfully!")
else:
    print(f"Error generating PowerPoint slides: {response.json()['message']}")
