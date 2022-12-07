# Instructions

## Expectations

In this project you are expected to do Day 1 of Advent of Code for the years 2015, 2016, 2017, 2018, 2019, 2020, 2021, and 2022. Every puzzle has two parts, an initial puzzle to solve, and a follow-up that is provided after you get the correct answer to the first: **it is expected that you complete both parts!**

For each year, you should have a python file called `solve.py` that displays a well-formatted printed output for both parts of the puzzle when you are finished. Here is my example output from the 2022 puzzle as reference:

```
The elf carrying the most calories was carrying 69,626 calories.
The top three elves carrying the most calories were carrying a total of 206,780 calories.
```

_Note the commas to format the numbers nicely in the output!_

This is our first project where I am going to start nit-picking our code and answers! We are going to be getting more serious about getting to know our tools and problem-solving with them!

---

## Accessing Different Years of Advent of Code

To access different years of Advent of Code, you should go to the [Advent of Code website](https://adventofcode.com/), and go to the `Events` section at the top. This page shows a list of all of the years of the challenge (and therefore all of the years you need to complete Day 1 of)! Choose your year from the list and choose Day 1 to read the instructions and work!

---

## Basic Setup

For each individual year's puzzle, you will go into that year's folder in this repository (for example for the 2015 puzzle, you go into the folder `2015`).

In that folder, you will have the following available:

- `input-transform.py` - This file will convert your puzzle input into the `input.json` file for you to read into your program and work with.
- `input.json` - This file starts out empty but will fill after you paste your puzzle input into `input.txt` and run `input-transform.py`
- `input.txt` - This file starts out empty and has you paste in your puzzle input.
- `mrg-answer.txt` - This file contains Mr. G's final answers to his own puzzle input, allowing you to check if your program works on the input provided in `mrg-input.json`.
- `mrg-input.json` - This file contains Mr. G's puzzle input, which you could run in your code and check your answers against `mrg-answer.txt` to see if you solved it correctly.

Your process for each year should look like the following:

1. Open the respective year's folder to work in
2. Read through the puzzle for that year on the [Advent of Code website](https://adventofcode.com/).
3. Click `get your puzzle input` at the bottom of the page to access your unique input. (If this is not there, make sure you have logged into the website)
4. Copy all of the text from your puzzle input using `CTRL + A` to highlight everything and `CTRL + C` to copy it all.
5. Paste the text from your puzzle input into the `input.txt` file using `CTRL + V`.
6. Open and run the `input-transform.py` file. Check `input.json` after running this and you should see all of your puzzle input converted into a list.
7. Create the file `solve.py` and work on coding your solution. Make sure your file is in the year's folder! Hint: Your first step is going to be reading in your input from `input.json`!
8. When needed, read in `mrg-input.json` instead and check your answer(s) against `mrg-answer.txt`

---

## Working with `json` Files in Folders

When working with things in folders, we need to tell Python where to look in the repository for a file. For example, when working on your `solve.py` in the 2022 folder, you will want to read from the `input.json` file in that same folder. To do this, it will not be as simple as:

```python
open("input.json", "r")
```

We have to specify the folder that this `json` file is in:

```python
open("2022/input.json", "r")
```

To do this for any year, just replace the `2022` with the year folder you are working in at the time!

---

## Assistance Offered

This project is meant to push you to find new uses for your current programming skills. As such, I don't want to provide the complete answers to you as that may limit your growth. That being said, there are a couple of things I am offering to do to help you out:

- I am always willing to discuss the project with you in class, and will do my best to rotate around and help everyone that needs it!
- I stay after school on Mondays, Wednesdays, and Thursdays in the computer lab (B102), so this is a great opportunity to get some one-on-one help from me!
- I have made a set of [videos]() of me reading through each year's puzzle and sketching out an algorithm in English on an approach to solve the problem. These are not the only ways to solve the problems, your limits are your creativity!
- I have provided my puzzle input in each folder in a file named `mrg-input.json`. If you change your code to read in my `mrg-input.json` file instead of yours, you can check your output against my correct answer to help determine if your code is working correctly!
