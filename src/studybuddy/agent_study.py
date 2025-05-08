from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    set_default_openai_client,
    set_tracing_disabled,
    OpenAIChatCompletionsModel

)
from openai import AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
import os


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key="AIzaSyC866MQEkEbRXZODnJ2G8PnFjvqipoR6ck",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)

set_tracing_disabled(True)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)


def studybuddy_agent():

    studybuddy = Agent(
        name="Studybuddy",
        instructions="""
        You are StudyBuddy,a helpful and friendly educational assistant.
        You help students understand academic concepts by explaining them in simple, clear language.
        Use examples and analogies when helpful.
        Never solve full assignments for students — focus on explaining and guiding.
        """

    )

    run_config = RunConfig(
        model =model,
        tracing_disabled =True
    )
    

    
    user_question = input("Ask StudyBuddy your question: ")
    result = Runner.run_sync(studybuddy, user_question, run_config=run_config)
    print(result.final_output)