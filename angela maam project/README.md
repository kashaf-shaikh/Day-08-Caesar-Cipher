# Day 08 - Caesar Cipher

This is my Day 8 project from Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp.

In this project, I created a Caesar Cipher program using Python. It can encrypt and decrypt messages by shifting each letter forward or backward in the alphabet.

## About the Project

The program gives the user two options:

- **Encode:** Changes the original message into an encrypted message.
- **Decode:** Changes the encrypted message back into its original form.

The user needs to enter three things:

1. Whether they want to encode or decode.
2. The message they want to process.
3. The shift number.

The program then shifts each letter according to the given number.

Spaces and other characters that are not in the alphabet are kept unchanged.

## Example

**Encoding:**

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello

Enter Shift Amount:
3

Here is the encoded result: khoor
```

**Decoding:**

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
decode

Type your message:
khoor

Enter Shift Amount:
3

Here is the decoded result: hello
```

## How It Works

For example, if the shift number is 3:

| Original Letter | Encoded Letter |
|---|---|
| a | d |
| b | e |
| c | f |
| d | g |
| e | h |

The program uses the position of each letter in the alphabet and shifts it by the given number.

## What I Learned

While making this project, I learned:

- Creating functions with parameters.
- Passing arguments to functions.
- Using `return` and `print()` inside functions.
- Working with strings and lists.
- Using `for` loops.
- Using `while` loops.
- Finding the position of an item using `index()`.
- Checking whether a character exists in a list using `in`.
- Using the modulo operator `%`.
- Importing variables from another Python file.
- Using conditions to encode and decode messages.
- Using Boolean variables to control a loop.

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How to Run

1. Clone or download this repository.
2. Open the project folder in PyCharm or another Python editor.
3. Make sure both Python files are in the same folder.
4. Open `main.py`.
5. Run the program.
6. Choose encode or decode and enter your message and shift number.

You can also run it using the terminal:

```bash
python main.py
```

## Project Structure

```text
Day-08-Caesar-Cipher/
│
├── main.py
├── art.py
└── README.md
```

## About My Learning

This is my eighth project in the 100 Days of Python course. I enjoyed making this project because I got to practise functions, loops, strings and the modulo operator together.

I will keep adding my daily projects to GitHub as I continue learning Python.