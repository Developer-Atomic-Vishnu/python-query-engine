# Documentation for the Frontend Application

![Image of the Web Application](./look.png)

### Detailed Overview:

The frontend is created using the Open-Source Framework called Streamlit. The Frontend is basically a chatbot that receives the query/prompt from the user and forwards it to the backend.

Internally as soon as the user sents the prompt it is forwarded to the Azure Functions's API to handle the response for us. Also for the temporary period of time, the message and the response is been saved in the dictionary to remember the history of the user. As soon as the user refreshes the page it, wipes out all the history and starts again, because we don't use the database to store the Conversation between the user and the GPT-35-turbo 0613-version.

Going into the depth of the sending of the prompt, essentially what happens is, The Streamlit send a post request to the Azure Functions's API with the prompt and its value in the following format:

```python
url = 'https://example.com'
data = {
"prompt": f"{prompt}"
}
response = requests.post(url, json=data)
```

As soon as we receive the response from the Azure Functions, we display it in the markdown format.

Also we have the Clear Button that empties the dictionary that contains the history of the messages.

In future we might Integrate it with the Super-AGI for the purpose of using multiple agents and models to communicate and develop the user specific prompt to get the proper response from the model.

# Installation and Setup for the application:

The following code can be currently able to run over any machine, and can be accessed at the local host that is run by default and can be manually configured to any ip address and port using the following command:

```bash
streamlit run your_app.py --server.port 8080 --server.address 192.168.1.100
```

The Application can be used by following the below steps:

- Step 1: Get the python over to your system.

```bash
sudo apt install python3
```

- Step 2: Install the required Libraries.

```bash
pip install -r requirements.txt
```

- Step 3: Replace your credentials such as the Azure Functions master key url, API-KEY, API-ENDPOINT with actual values.

- Step 4: Run the following command, being in the main folder to run the application.

```bash
streamlit run your_app.py --server.port 8080 --server.address 192.168.1.100
```

Thats it now your application should be running . . .