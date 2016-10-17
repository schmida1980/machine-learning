"""Count words."""


def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    words = str.split(s)
    counted_words = []

    # Count the number of occurences of each word in s

    while len(words) > 0:
        # take the first word from the list
        compare_word = words.pop(0)
        count = 1
        remaining_words = []

        # compare the first word with every other word in the list
        for word in words:
            if compare_word == word:
                # both words match => increase the count
                count += 1
            else:
                # the words don't match => keep the none matching word for future iterations
                remaining_words.append(word)

        # replace the word list with all non-matching words
        words = remaining_words

        # Sort the occurences in descending order (alphabetically in case of ties)

        insert_position = 0

        # iterate over the result tuples of words which have been counted so far
        for i in range(len(counted_words)):

            # check if the new word has the same count as the current result tuples
            if counted_words[i][1] == count:

                # both words have the same count, now determine the alphabetical order (using only the remaining tuples)
                for j in range(i, len(counted_words)):

                    # check if the tuple is "larger" alphabetically or if we have reached a tuple with a smaller count
                    if counted_words[j][0] > compare_word or counted_words[j][1] != count:
                        insert_position = j
                        break
                    j += 1
                    insert_position = j
                break
            elif counted_words[i][1] < count:
                # the new word has a larger count than this one, so insert it in front of it
                insert_position = i
                break

            i += 1
            insert_position = i

        # insert the newly counted word at the correct position
        counted_words.insert(insert_position, [compare_word, count])

        # Return the top n words as a list of tuples (<word>, <count>)

    top_n = counted_words[:n]

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()
