def edit_distance(string1: str, string2: str) -> int:
    """Calculate the edit distance between two strings based on levenshtein distance.

    Parameters
    ----------
    string1 : str
        First string.
    string2 : str
        Second string.

    Returns
    -------
    An Integer representing the edit distance.
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("string1 and string2 must be strings.")

    m = len(string1)
    n = len(string2)
    d = [[0] * (n + 1) for _ in range(m + 1)]  # create matrix for dynamic programming approach

    for i in range(1, m + 1):  # set first row of d to indices of m (string1) testcomment
        d[i][0] = i

    for j in range(1, n + 1):  # set first column of d to indices of n (string2)
        d[0][j] = j

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if string1[i - 1] == string2[j - 1]:  # set the cost c to 0 for the same letter, 1 for different letters
                c = 0
            else:
                c = 1
            # fill the matrix according to algorithm:
            d[i][j] = min(
                d[i - 1][j] + 1,  # deletion?
                d[i][j - 1] + 1,  # insertion?
                d[i - 1][j - 1] + c,
            )  # substitution
    return d[m][n]  # return lower right corner
