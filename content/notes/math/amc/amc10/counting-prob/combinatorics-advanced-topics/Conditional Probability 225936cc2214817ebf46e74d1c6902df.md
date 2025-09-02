# Conditional Probability

Conditional probability is a key concept that appears frequently in competitions like the AMC and AIME. It deals with finding the probability of an event occurring, given that a certain condition is already true.

### Example 4.7.1:

**Problem:** Given that the number we roll on a die is even, what is the probability that the number rolled is a 2?

**Solution:** The problem is asking for the probability of rolling a 2, given that the number is even. This can be expressed as:

\[
P(\text{Number is 2} \mid \text{Even number}) = \frac{P(\text{Number is 2 and even})}{P(\text{Even number})}
\]

There are three possible even numbers on a die: 2, 4, and 6. Since these are equally likely, the probability of rolling a 2, given that the number is even, is:

\[
P(\text{Number is 2} \mid \text{Even number}) = \frac{1}{3}
\]

### Theorem 4.7.2: **Bayes' Theorem**

Bayes' Theorem is a fundamental formula in conditional probability. It states that the probability of event \( A \) occurring given that event \( B \) has already occurred is:

\[
P(A \mid B) = \frac{P(A \cap B)}{P(B)}
\]

This formula means that the conditional probability of \( A \), given \( B \), is the probability of both \( A \) and \( B \) occurring, divided by the probability of \( B \) occurring.

- If \( A \) and \( B \) are **independent events**, then \( P(A \mid B) = P(A) \), because whether \( B \) occurs or not does not affect the probability of \( A \) occurring.

### Intuition:

- Conditional probability helps adjust the likelihood of an event based on the information that another event has occurred.
- In the case of independent events, the occurrence of one event does not influence the probability of the other, which is why \( P(A \mid B) = P(A) \).

This concept is critical in probability theory and shows up in various types of problems, from simple dice rolls to more complex scenarios like those involving Bayes' Theorem.