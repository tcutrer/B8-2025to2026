"""
This program will take in a file of text and count the number of times each word
appears in the file using a hash table.
"""

import string
import os
import re
from HashTable import HashTable

def count_words_in_file(filename, table_size=10):
    word_count_table = HashTable(table_size)
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
    return (word_count_table, words_processed)

def write_word_counts_to_file(hash_table, heading="Word Counts", words_processed=None, filename="word_counts.txt"):
    with open(filename, 'a') as stats_file:
        stats_file.write(f"--- {heading} ---\n")
        stats_file.write(f"Total collisions: {hash_table.COLLISIONS}\n")
        stats_file.write(f"Average bucket checks per insert/update: {hash_table.BUCKET_CHECK_COUNT / words_processed:.2f}\n")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    write_file = os.path.join(script_dir, 'hash_table_stats.txt')
    # Clear the stats file before writing new results
    with open(write_file, 'w') as f:
        f.write("Hash Table Performance Stats\n\n")
    filename = os.path.join(script_dir, 'war_and_peace.txt')

    # Run tests with different initial table sizes to see impact on collisions and performance
    word_counts, words_processed = count_words_in_file(filename)
    double_size_table, double_words_processed = count_words_in_file(filename, table_size=word_counts.size * 2)
    triple_size_table, triple_words_processed = count_words_in_file(filename, table_size=word_counts.size * 3)
    three_halfs_size_table, three_halfs_words_processed = count_words_in_file(filename, table_size=int(word_counts.size * 1.5))
    five_fourths_size_table, five_fourths_words_processed = count_words_in_file(filename, table_size=int(word_counts.size * 1.25))

    # write results to file
    write_word_counts_to_file(word_counts, heading="Original Table (Size 10)", words_processed=words_processed, filename=write_file)
    write_word_counts_to_file(double_size_table, heading="Double Size Table", words_processed=double_words_processed, filename=write_file)
    write_word_counts_to_file(triple_size_table, heading="Triple Size Table", words_processed=triple_words_processed, filename=write_file)
    write_word_counts_to_file(three_halfs_size_table, heading="1.5x Size Table", words_processed=three_halfs_words_processed, filename=write_file)
    write_word_counts_to_file(five_fourths_size_table, heading="1.25x Size Table", words_processed=five_fourths_words_processed, filename=write_file)

    print("Word counting complete. Performance stats written to hash_table_stats.txt")
