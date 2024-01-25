def word_filter_counter(text, filter_words):
    from collections import Counter

    # Split the text into words
    words = text.split()

    # Initialize the result as a Counter
    result = Counter()

    # Iterate over each word and count occurrences
    for word in words:
        result[word.lower()] += 1

    # Filter the result based on the provided filter words
    filtered_result = {filter_word: result.get(filter_word.lower(), 0) for filter_word in filter_words}

    return filtered_result

# Test cases
print(word_filter_counter("Hello world, hello!", ["hello"]))
# Expected output: {'hello': 2}

print(word_filter_counter("The quick brown fox.", ["the"]))
# Expected output: {'the': 1}

print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))
# Expected output: {'is': 2, 'this': 2, 'just': 1}

print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]))
# Expected output: {'we': 1, 'the': 1, 'or': 1}