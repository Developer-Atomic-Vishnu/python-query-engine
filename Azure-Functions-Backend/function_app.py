# Import necessary libraries
import azure.functions as func  # For creating Azure Functions
import logging  # For logging messages
import os  # For interacting with environment variables
from dotenv import load_dotenv  # For loading variables from .env file
from openai import AzureOpenAI  # For interacting with the OpenAI API

# Load variables from .env file (e.g., API keys)
load_dotenv()

# Create an Azure Function app with admin-level authentication
app = func.FunctionApp(http_auth_level=func.AuthLevel.ADMIN)

# Define an HTTP-triggered function
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
   """Handles incoming HTTP requests and calls OpenAI for a response."""

   logging.info('Python HTTP trigger function processed a request.')  # Log a message

   # Get the prompt from the query string or request body
   box1 = req.params.get('prompt')  # Try getting prompt from query parameters
   if not box1:  # If not found in query parameters
       try:
           req_body = req.get_json()  # Attempt to get prompt from request body
       except ValueError:
           pass  # Ignore if request body is not valid JSON
       else:
           box1 = req_body.get('prompt')  # Extract prompt from request body if available

   # Create an OpenAI API client using environment variables
   client = AzureOpenAI(
       api_key=os.getenv("OPENAI_API_KEY"),  # Load API key from .env file
       api_version="2023-07-01-preview",  # Specify API version
       azure_endpoint="<YOUR-OPENAI-ENDPOINT>",  # Azure endpoint
   )

   # Call the OpenAI API to generate a response based on the prompt
   completion = client.chat.completions.create(
       model="<YOUR-DEPLOYMENT-NAME>",  # Specify the OpenAI model to use
       messages=[
           {
               "role": "user",  # Set the role of the first message as "user"
               "content": box1  # Include the prompt in the message
           }
       ]
   )

   # Extract the generated response from the API response
   answer = completion.choices[0].message.content

   # Return the response as an HTTP response
   if answer:  # If a response was generated
       return func.HttpResponse(f"{answer}")
   else:  # If no response was generated
       return func.HttpResponse(
           "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
           status_code=200
       )
