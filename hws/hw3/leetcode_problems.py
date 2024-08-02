

def merge_alternately(word1, word2):
    """
    Merge two strings alternately.

    Merges two input strings by alternating characters 
    from each string until one of the strings is exhausted,
    then appends the remaining characters of the other string to the result.

    :type word1: str
    :type word2: str
    :rtype: str
    """
    # Convert to lists to use append
    word1_list = list(word1)
    word2_list = list(word2)
    merged_word_list = []

    # Alternate through word 1 and 2, removing each letter after appending to the merged word
    # Utilizie fact that empty string returns false
    while word1_list or word2_list:
        if word1_list:
            merged_word_list.append(word1_list.pop(0))
        if word2_list:
            merged_word_list.append(word2_list.pop(0))

    # Now convert back to a string
    merged_word = ''.join(merged_word_list)

    return merged_word


def gcd_of_strings(str1, str2):
    """ Find the greatest common divisor (GCD) of two strings.

    Given two strings `str1` and `str2`, this function finds the
    greatest common divisor (GCD) of the two strings. The GCD of 
    two strings is the longest string that divides both `str1` and `str2`.

    :type str1: str
    :type str2: str
    :rtype: str
    """
    # If concat they should be the same in either direction
    if (str1 + str2) != (str2 + str1):
        return ""

    # If they are just the same then you have the gcd
    if (str1 == str2):
        return str1

    # Otherwise find the longer string and pass it recursively
    if len(str1) > len(str2):
        return gcd_of_strings(str1[len(str2):], str2)
    else:
        return gcd_of_strings(str1, str2[len(str1):])


def students_with_books(books, extra):
    """ Determine which students will have the highest number of books
    in the class after receiving extra books.

    :type books: List[int]
    :type extra: int
    :rtype: List[bool]
    """
    #max errors on empty list so run this
    if not books:
        return []
    # Get current most books
    max_books = max(books)
    # Go through list and check if
    book_bool = [False] * len(books)
    for i in range(len(books)):
        if books[i] + extra >= max_books:
            book_bool[i] = True
        else:
            book_bool[i] = False
    return book_bool


def two_sum(nums, target):
    """Find the indices of two numbers in the given list 
    that add up to the target value.

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # utilize dictionary with indexes for single loop
    values = {}
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in values:
            return [values[remainder], i]
        values[nums[i]] = i
    return None


def move_zeroes(nums):
    """Move all zeroes to the end of the given list while maintaining
    the relative order of non-zero elements.

    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    #find every zero, and swap with the next value then iterate
    zero_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[zero_pos]
            nums[zero_pos] = temp
            zero_pos += 1
