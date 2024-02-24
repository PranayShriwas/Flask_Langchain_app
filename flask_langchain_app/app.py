# Import necessary modules
from flask import Flask, render_template, request
import openai

# Set up Flask app
app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for processing user input
@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get user input from the form
        user_prompt = request.form['user_prompt']

        # Generate response using OpenAI's LangChain
        response = generate_response(user_prompt)

        # Display the response on the webpage
        return render_template('index.html', user_prompt=user_prompt, response=response)
    except Exception as e:
        # Handle general errors
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', user_prompt=user_prompt, error_message=error_message)

# Function to interact with OpenAI's LangChain
def generate_response(prompt):
    try:
        # Use OpenAI's completion API
        response = openai.Completion.create(
            engine="davinci",  # Specify the engine
            prompt=prompt,
            max_tokens=100,  # Adjust max tokens based on your preference
            temperature=0.7,  # Adjust temperature based on your preference
        )

        # Extract and return the generated text
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        # Handle OpenAI API errors
        error_message = f"OpenAI API error: {str(e)}"
        return error_message

# Run the Flask app
if __name__ == "_main_":
    app.run(debug=True)