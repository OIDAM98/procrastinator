#!/usr/bin/env python3

# Based on the brain_module facilitated for the Capstone Project

import os
from dotenv import load_dotenv
import openai

class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        load_dotenv()
        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        openai.api_key = self.api_key

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "This is the behavior of chatGPT"
    
    def request_openai(self, message, role="system") -> str:
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        # Create a chat completion with the provided message and role
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": role, "content": message}]
        )

        # Return the message content from the API response
        return response.model_dump()["choices"][0]["message"]["content"]

    def ask_recom(self, message: str) -> str:
        """
        API Request to OpenAI. Mainly used to get recommendations from the user.

        Args:
        - message (str): 

        Returns:
        - str: The response from OpenAI API.
        """
        return self.request_openai(message, "user")

    def tell_list(self, message: str) -> str:
        """
        API Request to OpenAI.
        Inteded to show the list of picks from the user.

        Args:
        - message (str): A list depicting the chosen picks from the user.
        Will be the base for following recommendations.

        Returns:
        - str: The response from OpenAI API. Most commonly comments about the list passed.
        """
        final = f"{message}\nCan you comment something about this list?"
        return self.request_openai(final, "user")

    def opening_message(self) -> str:
        """
        Used to open the interaction between the user and OpenAI API.
        Sets up the API as a recommender for the application, using the system role.

        Returns:
        - str: A welcoming message from OpenAI API.
        """
        message = "You are a someone that knows a lot about TV shows, movies, music, videogames, and anime. I want some media recommendations on those topics, but first introduce yourself."
        return self.request_openai(message)

    def closing_message(self) -> str:
        """
        Used to finish the interaction between the user and OpenAI API.
        Mimics a closing and thanking message from the user to the recommender.

        Returns:
        - str: A goodbye message from OpenAI API.
        """
        message = "Thanks a lot for the recommendations! Will keep them in mind. That's all I need now."
        return self.request_openai(message, "user")
