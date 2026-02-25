"""
This program will take in a file of text and count the number of times each word
appears in the file using a hash table.
"""

import string
import os
import re
from HashTable import HashTable

def count_words_in_file(filename):
    word_count_table = HashTable(10)
    words_processed = 0
    # Compile regex pattern once instead of per word
    punctuation_pattern = re.compile(r'[^\w\s]')

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                words_processed += 1
                word = word.lower()
                word = punctuation_pattern.sub('', word)  # Remove punctuation
                # Use insert_or_update to combine search+insert into one operation
                word_count_table.insert_or_update(word)

    return word_count_table

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, 'war_and_peace.txt')
    word_counts = count_words_in_file(filename)

    # Print the word counts
    for bucket in word_counts.table:
        if not bucket.isEmpty():
            print(f"{bucket.key}: {bucket.value}")
    print(f"Total collisions: {word_counts.collisionCount}")
    with open(os.path.join(script_dir, 'hash_table_stats.txt'), 'w') as stats_file:
        stats_file.write(f"Total collisions: {word_counts.collisionCount}\n")
        stats_file.write(f"Final table size: {word_counts.size}\n")
        stats_file.write(f"Number of buckets used: {word_counts.bucketCount}\n")
        for bucket in word_counts.table:
            if not bucket.isEmpty():
                stats_file.write(f"{bucket.key}: {bucket.value}\n")