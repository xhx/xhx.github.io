# Rearranging Letters with Repetitions

The problem you're describing is a classic combinatorics question about counting the number of ways to rearrange letters of a word when some of the letters are repeated.

### Formula for Rearranging Letters with Repetitions:

Given a word with \( n \) letters, where:

- \( x_a \) is the number of times letter \( a \) appears,
- \( x_b \) is the number of times letter \( b \) appears,
- \( x_c \) is the number of times letter \( c \) appears, and so on,
- up to \( x_z \), representing all other repeated letters.

These counts satisfy the equation:

$$

x_a + x_b + x_c + \dots + x_z = n

$$

The total number of distinct ways to rearrange the letters is given by the formula:

$$

\text{Number of distinct arrangements} = \frac{n!}{x_a! \cdot x_b! \cdot x_c! \cdot \dots \cdot x_z!}

$$

### Explanation of the Formula:

- **\( n! \)** represents the total number of ways to arrange \( n \) letters if all the letters were distinct.
- **Dividing by \( x_a!, x_b!, \dots \)** accounts for the overcounting caused by repeated letters. For instance, if a letter appears \( x_a \) times, permuting just those \( x_a \) letters doesn't create new distinct arrangements.

### Example:

Consider the word **BANANA**:

- The total number of letters is \( n = 6 \).
- The letter "A" appears \( x_A = 3 \) times.
- The letter "N" appears \( x_N = 2 \) times.
- The letter "B" appears \( x_B = 1 \) time.

Using the formula:

\[
\text{Number of distinct arrangements} = \frac{6!}{3! \cdot 2! \cdot 1!}
\]

Calculate each factorial:

\[
6! = 720, \quad 3! = 6, \quad 2! = 2, \quad 1! = 1
\]

So, the number of distinct arrangements is:

\[
\frac{720}{6 \cdot 2 \cdot 1} = \frac{720}{12} = 60
\]

Thus, there are **60 distinct ways** to rearrange the letters of the word "BANANA."

### General Case:

For any word where certain letters are repeated, you follow the same process:

1. Calculate \( n! \), where \( n \) is the total number of letters.
2. Divide by the factorial of the number of repetitions of each letter.