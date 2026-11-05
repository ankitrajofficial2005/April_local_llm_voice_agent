
import requests
import time

# --------------------------------
# 1. Configuration
# --------------------------------

URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:4b"

# --------------------------------
# 2. User information
# --------------------------------

user_name = input("Enter your name: ").strip()

if not user_name:
    user_name = "User"

# --------------------------------
# 3. System prompt and conversation
# --------------------------------

system_message = {
    "role": "system",
    "content": (
        f"You are April, a helpful local AI assistant. "
        f"The user's name is {user_name}. "
        "Explain concepts in simple, beginner-friendly language. "
        "Teach step by step. "
        "Give hints before complete coding solutions. "
        "Review code and explain mistakes clearly. "
        "Respond in the same language as the user."
    )
}

messages = [system_message]

# --------------------------------
# 4. Welcome message
# --------------------------------

print(f"\nApril: Hello {user_name}! I am April.")
print("April: How can I help you today?")
print("\nType 'exit' to quit.")
print("Type 'clear' to clear conversation.")
print("Type 'name' to check your name.")

# --------------------------------
# 5. Message counter
# --------------------------------

message_count = 0

# --------------------------------
# 6. Main conversation loop
# --------------------------------

while True:

    user_input = input("\nYou: ").strip()

    # Exit command
    if user_input.lower() == "exit":
        print("\nApril: Goodbye!")
        break

    # Empty input handling
    if not user_input:
        print("April: Please enter something.")
        continue

    # Clear conversation
    if user_input.lower() == "clear":
        messages = [system_message]
        print("April: Conversation cleared!")
        continue

    # Name command
    if user_input.lower() == "name":
        print(f"April: Your name is {user_name}.")
        continue

    # --------------------------------
    # 7. Add user message to history
    # --------------------------------

    messages.append({
        "role": "user",
        "content": user_input
    })

    message_count += 1

    # --------------------------------
    # 8. Prepare API payload
    # --------------------------------

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "think": False
    }

    # --------------------------------
    # 9. Send request to Ollama
    # --------------------------------

    start_time = time.time()

    try:

        response = requests.post(
            URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        # --------------------------------
        # 10. Extract AI response
        # --------------------------------

        data = response.json()

        assistant_reply = data["message"]["content"]

        print(f"\nApril: {assistant_reply}")

        # --------------------------------
        # 11. Save assistant response
        # --------------------------------

        messages.append({
            "role": "assistant",
            "content": assistant_reply
        })

        end_time = time.time()

        print(
            f"\n[Response time: "
            f"{end_time - start_time:.2f} seconds]"
        )

    # --------------------------------
    # 12. Error handling
    # --------------------------------

    except requests.exceptions.Timeout:
        print("April: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("April: Cannot connect to Ollama.")
        print("Please check whether Ollama is running.")

    except requests.exceptions.RequestException as error:
        print(f"April: API error: {error}")

    except (KeyError, ValueError) as error:
        print(f"April: Response parsing error: {error}")

# --------------------------------
# 13. Final statistics
# --------------------------------

print("\n========== SESSION SUMMARY ==========")
print(f"Total user messages: {message_count}")
print("April AI session ended.")
