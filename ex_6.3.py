def letter_count(string, letter):
  """Counts the number of occurrences of a specific letter in a string.

  Args:
      string: The string to search in.
      letter: The letter to count occurrences of.

  Returns:
      The number of times the letter appears in the string.
  """
  count = 0
  for char in string:
    if char == letter:  # Check if current character equals the target letter
      count += 1
  return count

# Example usage
word = 'banana'
letter = 'a'
result = letter_count(word, letter)
print(result)  # Output: 3
