import os
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import LLMChain

from dotenv import load_dotenv
load_dotenv()

class Quizset(BaseModel):
    set_nr: int = Field(description="Number of the Quiz-Set") 
    question: str = Field(description="A quiz question")
    answers: dict = Field(description="The corresponding answers to the questions")
    correct_answer: str = Field(description="The correct answer")

parser = PydanticOutputParser(pydantic_object=Quizset)

os.environ['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')

chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

system_template="You are a Quizmaster asking {level} questions in the area of {thema}. Always create a new question"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template="Create {set_nr} sets of quiz questions to the given topic and return it each together with {number_of_answers} answers of which one is the correct answer. Indicate which answer is the correct one.\n{format_instructions}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=chat, prompt=chat_prompt)

if __name__ == "__main__":
    print(chain.run(level="easy", thema="Switzerland", number_of_answers="2", set_nr=2, format_instructions=parser.get_format_instructions()))
