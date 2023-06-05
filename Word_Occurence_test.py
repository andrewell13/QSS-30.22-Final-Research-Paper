# Andrew Ellis
# QSS 30.22 - SP23
# Used in research for Final Paper on Fizz posts

import re

def count_word_occurrences(file1, file2, output_file):
    # Read the contents of file1
    with open(file1, 'r') as f1:
        text1 = f1.read()

    # Read the words from file2
    with open(file2, 'r') as f2:
        words = [line.strip() for line in f2 if line.strip()]

    # Count the occurrences of each word in file1
    counts = {}
    total_count = 0
    for word in words:
        pattern = r"\b" + re.escape(word) + r"\b"  # Add word boundary anchors
        count = len(re.findall(pattern, text1, re.IGNORECASE)) # Find all occurrences of given word
        counts[word] = count
        total_count += count # Increment total count

    # Write the counts to the output file
    with open(output_file, 'w') as f_out:
        for word, count in counts.items():
            # Write the testing word and its count to the output file
            f_out.write(f"{word}: {count}\n")

        # Write the total count to the output file
        f_out.write(f"Total Count: {total_count}\n")

        # Calculate the probabilities of a given testing word occurring more than once, twice, and three times
        more_than_once = sum(1 for count in counts.values() if count > 1) / len(words)
        more_than_twice = sum(1 for count in counts.values() if count > 2) / len(words)
        more_than_three = sum(1 for count in counts.values() if count > 3) / len(words)

        # Write the probabilities to the output file
        f_out.write(f"Probability of getting the same word more than once: {more_than_once:.2f}\n")
        f_out.write(f"Probability of getting the same word more than twice: {more_than_twice:.2f}\n")
        f_out.write(f"Probability of getting the same word more than three times: {more_than_three:.2f}\n")

# Usage example
file1 = 'Jacko.txt'
file2 = 'Sample.txt'
output_file = 'Jacko_occurrences.txt'

count_word_occurrences(file1, file2, output_file)
