print("===============================")
print("                  APRIL AI ASSISTANT")
print("===============================")

name = input("What is your name? ")
age = input("What is yoour age? ")
print(f"Hello {name}, {age}, Welcome! I am April.")

message_count = 0
while True:
    user_input = input("\nyou: ")



    if user_input.lower() == "hello":
        print("April: How can i help you!")
        break
        


print("===============================")
print("                  APRIL AI ASSISTANT")
print("===============================")

name = input("what is your name? ")
print(f"Hello {name}, I am April.")


while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("April: Goodbye!")
        break

    if user_input.strip() == "":
        print("April: Please enter a message.")
        continue

    message_count += 1

    if user_input.lower() == "hello":
        print("April: Hello! How can I help you?")
        continue

    print(f"April: You said {user_input}")