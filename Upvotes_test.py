# Andrew Ellis
# QSS 30.22 - SP23
# Used in research for Final Paper on Fizz posts

import re
import numpy as np

def count_word_occurrences(posts_file, likes_file, file2, output_file):
    # Read the posts from the text file
    with open(posts_file, 'r') as f_posts:
        posts = f_posts.read().split('\n')

    # Read the likes from the text file
    with open(likes_file, 'r') as f_likes:
        likes = f_likes.read().splitlines()

    # Read the words from file2
    with open(file2, 'r') as f2:
        words = [line.strip() for line in f2 if line.strip()]

    # Count the occurrences of each word in each post
    counts = [] # Initialize counts of occurences
    total_ratio = 0  # Initialize total ratio sum
    total_likes = 0 # Initialize total upvote count
    key_word_counts = []  # List to store key word counts
    key_word_ratio = [] # List to store testing word ratios
    like_counts = []  # List to store like counts

    for post, post_likes in zip(posts, likes):
        post_counts = {}
        total_count = 0
        for word in words:
            pattern = r"\b" + re.escape(word) + r"\b"  # Add word boundary anchors
            count = len(re.findall(pattern, post, re.IGNORECASE)) # counts all occurrences of given testing word
            if count > 0:  # Only include words with a count greater than 0
                post_counts[word] = count
                total_count += count  # Increase the total count
        counts.append((post, post_likes, post_counts, total_count))
        if total_count > 0:  # Calculate and accumulate ratio if total_count is greater than 0
            ratio = int(post_likes) * (total_count / len(post.split())) # Calculate ratio of likes per testing word
            total_ratio += ratio  # Add to total ratio
            # Add the ratio of testing words to total words to key_word_ratio if total count > 0
            key_word_ratio.append(total_count / len(post.split()))
        else:
            # If there were no testing words append 0 to key_word_ratio
            key_word_ratio.append(0)
        # Increment total likes
        total_likes += int(post_likes)
        key_word_counts.append(total_count)
        like_counts.append(int(post_likes))

    # Write the counts to the output file
    with open(output_file, 'w') as f_out:
        for post, post_likes, post_counts, total_count in counts:
            f_out.write(f"Post: {post}\n")
            f_out.write(f"Likes: {post_likes}\n")
            for word, count in post_counts.items():
                f_out.write(f"{word}: {count}\n")
            f_out.write(f"Key Word Count: {total_count}\n")
            if total_count > 0:
                ratio = int(post_likes) * (total_count / len(post.split()))
                f_out.write(f"Like to Key Word Ratio: {ratio}\n\n")
            else:
                f_out.write(f"\n")

        average_ratio = total_ratio / len(counts) if len(counts) > 0 else 0  # Calculate average ratio
        adjusted_ratio = float(average_ratio) / total_likes if total_likes > 0 else 0 # Calculate adjusted normalized ratio
        correlation = np.corrcoef(key_word_counts, like_counts)[0, 1]  # Calculate correlation coefficient
        ratio_correlation = np.corrcoef(key_word_ratio, like_counts)[0, 1] # Calculate correlation for ratios and likes

        # Write the results to an output file
        f_out.write(f"\nAverage Likes per Key Word Count Ratio: {average_ratio:.2f}\n")
        f_out.write(f"\nAdjusted Ratio: {adjusted_ratio:.5f}\n")
        f_out.write(f"\nCorrelation between Key Word Count and Likes: {correlation:.2f}\n")
        f_out.write(f"\nCorrelation between Key Word Count Ratio to Total Words and Likes: {ratio_correlation:.2f}\n")

# Usage example
posts_file = 'New_fizz.txt'
likes_file = 'New_upvotes.txt'
file2 = 'Sample.txt'
output_file = 'New_upvotes_output.txt'

# posts_file = 'Fizzing_fizz.txt'
# likes_file = 'Fizzing_upvotes.txt'
# file2 = 'Sample.txt'
# output_file = 'Fizzing_upvotes_output.txt'

# posts_file = 'Top_fizz.txt'
# likes_file = 'Top_upvotes.txt'
# file2 = 'Sample.txt'
# output_file = 'Top_upvotes_output.txt'

count_word_occurrences(posts_file, likes_file, file2, output_file)