from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables from the .env file
load_dotenv()

# Initialize ChatGroq using the correct keyword argument and model name
model = ChatGroq(model="openai/gpt-oss-20b")    


print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")


choice = int(input("Tell your response :- "))
if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

message =[
     SystemMessage(content=mode),
]


print("----------------- welcom type 0 to exit the application-----------------")
while True:
    user_input = input("You: ")
    message.append(HumanMessage(content=user_input))
    if user_input == "0":
        break
        
    response = model.invoke(message)
    message.append(AIMessage(response.content))
    
    # Print the response inside the loop so you can see it immediately
    print(f"AI: {response.content}\n")