## Love Calculator
# UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

Click here

## 💪 This is a Difficult Challenge 💪
# Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
```
"Your score is **x**, you go together like coke and mentos."
```

For Love Scores between 40 and 50, the message should be:
```
"Your score is **y**, you are alright together."
```
Otherwise, the message will just be their score. e.g.:
```
"Your score is **z**."
```
e.g.
```
name1 = "Angela Yu"

name2 = "Jack Bauer"
```
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times
```
Total = 5
```
L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times
```
Total = 3
```
```
Love Score = 53
Print: "Your score is 53."
```
Example Input 1
```
name1 = "Kanye West"
name2 = "Kim Kardashian"
```
Example Output 1
```
Your score is 42, you are alright together.
```
Example Input 2
```
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
```
Example Output 2
```
Your score is 73.
```
e.g. When you hit run, this is what should happen:

Unsupported image

The testing code will check for print output that is formatted like one of the lines below:
```
"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."
```
### Score Comparison
Not sure you're getting the correct score for the exercise? Use this table to check your code's score against mine.

<table>
    <thead>
        <td>Name 1</td>
        <td>Name 2</td>
        <td>Score</td>
    </thead>
    <tbody>
        <tr>
            <td>Catherine Zeta-Jones</td>
            <td>Michael Douglas</td>
            <td>99</td>
        </tr>
        <tr>
            <td>Brad Pitt</td>
            <td>Jennifer Aniston</td>
            <td>73</td>
        </tr>
        <tr>
            <td>Prince William</td>
            <td>Kate Middleton</td>
            <td>67</td>
        </tr>
        <tr>
            <td>Angela Yu</td>
            <td>Jack Bauer</td>
            <td>53</td>
        </tr>
        <tr>
            <td>Kanye West</td>
            <td>Kim Kardashian</td>
            <td>42</td>
        </tr>
        <tr>
            <td>Beyonce</td>
            <td>Jay-Z</td>
            <td>23</td>
        </tr>
        <tr>
            <td>John Lennon</td>
            <td>Yoko Ono</td>
            <td>18</td>
        </tr>
    </tbody>
</table>

## Hint
- The lower() function changes all the letters in a string to lower case.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

- The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string