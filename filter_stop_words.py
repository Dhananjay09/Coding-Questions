def stop_words(text, k):
    # Step 1: Tokenize the input text into words
    words = text.split()

    # Step 2: Count the occurrences of each word while maintaining order
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Step 3: Filter out words that occur at least k times
    stop_words_list = []
    for word in words:
        if word_count[word] >= k and word not in stop_words_list:
            stop_words_list.append(word)

    # Step 4: Return the list of stop words in order of their first occurrence
    return stop_words_list


# Example usage
text = "a mouse is smaller than a dog but a dog is stronger"
k = 2
result = stop_words(text, k)
print(result)  # Output: ['a', 'is', 'dog']
