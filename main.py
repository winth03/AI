from transformers import pipeline
from transformers.pipelines.conversational import Conversation

pipe = pipeline('conversational', model='microsoft/DialoGPT-medium')

prompt = input('You : ')
convo = Conversation(prompt)
while prompt != "bye":
    if len(convo.generated_responses) != 0:
        prompt = input('You : ')
        convo.add_user_input(prompt)
    response = pipe(convo)
    print(response)
