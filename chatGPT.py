import os
import openai
openai.api_key = 'Your API key'

response = ''
while True:
  ask = input("User: ")
  print()
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": 'Senior software engineer who is an expert in python and gives detailed guidance and code examples'},
      {"role": "assistant", "content": response},
      {"role": "user", "content": ask}
    ]
  )
  response = completion.choices[0].message.content
  print(f'chatGPT: {response}' )
  print()
