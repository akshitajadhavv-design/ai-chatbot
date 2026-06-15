import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 AI Assistant with Memory! Type 'quit' to exit")
print("-" * 50)

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Remember everything the user tells you."}
]

while True:
    question = input("You: ").strip()
    if question.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    if not question:
        continue
    conversation_history.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    ai_response = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_response})
    print(f"AI: {ai_response}")
    print("-" * 50)
response = chain.invoke({"job_title": "Data Analyst"})
prompt | llm  # This is called a CHAIN