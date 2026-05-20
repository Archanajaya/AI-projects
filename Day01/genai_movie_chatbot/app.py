print("🎬 AI Movie Recommendation Chatbot")

knowledge = {
    "action": ["Leo", "Vikram", "KGF"],
    "comedy": ["Doctor", "Jailer"],
    "romance": ["96", "Sita Ramam"],
    "horror": ["Pizza", "Maya"]
}

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    found = False

    for genre in knowledge:

        if genre in user:

            print(f"Bot: Recommended {genre} movies:")

            for movie in knowledge[genre]:
                print("-", movie)

            found = True
            break

    if not found:
        print("Bot: Sorry, I only know action, comedy, romance, and horror movies.")
