# Initialize an empty list to store the feedback entries.
feedback_list = []

# Print a message to the user, instructing them on how to enter feedback
# and how to signal the end of input.
print("Enter customer feedback. Type 'END' to finish:")

# Start an infinite loop. This loop will continue until the user enters 'END'.
while True:
    # Prompt the user to enter feedback using the "> " symbol.
    # The input provided by the user is stored in the 'feedback' variable.
    feedback = input("> ")
    # Check if the user has entered 'END' (case-insensitive) to finish input.
    if(feedback.strip().upper() == "END"):
        # If the user entered 'END', break out of the 'while' loop.
        break
    # If the input is not 'END', remove any leading or trailing whitespace from the feedback
    # and append it to the 'feedback_list'.
    feedback_list.append(feedback.strip())

# Check if the 'feedback_list' is empty. This happens if the user types 'END' immediately.
if not feedback_list:
    # If the list is empty, print a message indicating that no feedback was provided.
    print("No feedback provided.")
else:
    # If there is feedback in the list, prompt the user to enter keywords for analysis.
    # The keywords should be separated by commas.
    keywords_input = input("Enter keywords to analyze, separated by commas: ")
    # Remove leading/trailing whitespace from the input, convert it to lowercase,
    # and split the string into a list of keywords using the comma as a delimiter.
    keywords = keywords_input.strip().lower().split(',')
    # Create a new list of keywords, ensuring that each keyword in the list
    # has no leading or trailing whitespace and is not an empty string.
    keywords = [keyword.strip() for keyword in keywords if keyword.strip()]

    # Initialize an empty dictionary to store the counts of each keyword.
    # The keys of the dictionary will be the keywords, and the initial value for each will be 0.
    keyword_counts = {keyword: 0 for keyword in keywords}
    # Initialize an empty list to store phrases from the feedback that start with "i feel" or "i think".
    extracted_phrases = []

    # Iterate through each feedback entry in the 'feedback_list'.
    for feedback in feedback_list:
        # Convert the current feedback entry to lowercase for case-insensitive keyword searching.
        feedback_lower = feedback.lower()

        # Iterate through each keyword in the 'keywords' list.
        for keyword in keywords:
            # Count the number of times the current keyword appears in the lowercase feedback.
            # Add this count to the current count of the keyword in the 'keyword_counts' dictionary.
            keyword_counts[keyword] += feedback_lower.count(keyword)

        # Check if the phrase "i feel" is present in the lowercase feedback.
        if "i feel" in feedback_lower:
            # If found, find the starting index of "i feel" in the lowercase feedback.
            start_idx = feedback_lower.find("i feel")
            # Append the portion of the original feedback (preserving original casing) starting from the found index
            # to the 'extracted_phrases' list.
            extracted_phrases.append(feedback[start_idx:])
        # Check if the phrase "i think" is present in the lowercase feedback.
        elif "i think" in feedback_lower: # Corrected line: should check in lowercase feedback
            # If found, find the starting index of "i think" in the lowercase feedback.
            start_idx = feedback_lower.find("i think")
            # Append the portion of the original feedback (preserving original casing) starting from the found index
            # to the 'extracted_phrases' list.
            extracted_phrases.append(feedback[start_idx:])

# Print a heading for the feedback summary.
print("\nFeedback Summary:")
# Print a separator line.
print("-----------------")
# Print the total number of feedback entries collected.
print(f"Total feedback entries: {len(feedback_list)}")

# Print a heading for the keyword counts.
print("\nkeyword Counts:")
# Iterate through the 'keyword_counts' dictionary.
for keyword, count in keyword_counts.items():
    # Print each keyword and its corresponding count, formatted as "-keyword: count".
    print(f"-{keyword}: {count}")

# Print a heading for the extracted phrases.
print("\nExtracted Phrases:")
# Check if the 'extracted_phrases' list contains any phrases.
if extracted_phrases:
    # If there are extracted phrases, iterate through the list.
    for phrase in extracted_phrases:
        # Print each extracted phrase, formatted with a hyphen.
        print(f"-{phrase}")
else:
    # If no phrases starting with "i feel" or "i think" were found, print a corresponding message.
    print("No phrases starting with 'I feel' or 'I think' found.")