# Comprehensyllabi

<img src="https://github.com/dpeletz/Comprehensyllabi/blob/assets/logo.png?raw=true" width="200" />

## Introduction
*comprehensyllabi* is a Python program that enables students to have a better understanding of their workload by extracting the important information from their classes’ syllabi. 

## Inspiration
We felt that as students, sometimes the syllabi for our classes can be lengthy and wordy. It can take a while to read through these all syllabi at the beginning of the semester and it can also be frustrating to continually have to sift through them looking for the important information throughout the semester. We wanted to entirely eliminate the need to review syllabi repeatedly and create a platform that enables students to have a better overview of what the course will look like. 
With *comprehensyllabi*, a student will no longer need to sift through long syllabi to look for the important information such as grading breakdowns, important due dates, office hours, and contact information. The program examines the PDF syllabus and extracts all the important information for the student and exports it as a CSV file. 

## What It Does
*comprehensyllabi* is a Python program that takes allows a user to import their syllabus and receive a CSV file with a comprehensive overview of the course. This condensed guide with only the most important information will then serve as a resource for the student to reference throughout the semester. No longer will a student have to spend a long time looking for the most important information for each of his or her classes many times throughout the semester. After running comprehensyllabi once at the semester’s start, the user will then have a quick reference guide that they can look at in seconds. 

## How We Built It
We started out by sketching out what we wanted our graphic user interface to look like and determining the functionality for our minimum viable product (MVP). We determined that we simply wanted a button for importing and extracting the important information and then a button for quitting the program. We wanted to keep the user interface as simple as possible. 
Next, we outlined the functions that we would need and the inputs and outputs of the program. We felt that the program would work best with a PDF as an input and a CSV as an output. Often, we’ve found that syllabi tend to come in PDF form. 
We then assigned tasks and began the coding in Python and worked on figuring out which libraries to implement and how to get them to function together. Lastly, we tested our program on various syllabi. 

## Challenges
Some of the challenges we faced while making our project included difficulties linking the actual program to our GUI, problems with the various packages our program relied on, and making the entire project user-friendly. We split the program into two sections, with one being a front-end GUI and the other being the back-end text parsing. Because two different editors were used for these separate tasks, merging them proved more complex than anticipated; to overcome this, we had to fix the modules that each section relied on.
Furthermore, making the interface user friendly was a key part of our project idea. The entire purpose of this project is to simplify the users’ lives, so the entire program needed to be streamlined and appealing. While we didn’t have time to fully develop an incredibly aesthetically pleasing GUI, we feel that our result is straightforward and easy to use.
Accomplishments That We're Proud Of
We are very proud of our idea and the way in which we chose to implement it. The program as a whole incorporates a wide variety of software development elements, ranging from the front-end user interaction to the back-end machine learning. Combining these two facets of computer science was not easy, but it certainly deepened our understanding and forced us to venture outside of our comfort zones. In the end, we are created a program that accomplished our initial goals and can drastically simplify students’ lives

## What We Learned
As we had some new hackers on our team, we learned that it's possible to develop an impactful piece of software in a short period of time. We also learned how to utilize various Python libraries such as NLTK, PyPDF2, Tkinter, Pandas, and easyGUI. 

## What's Next for comprehensyllabi
We hope to improve comprehensyllabi moving forward and improve the functionality by extracting more important information from the syllabi. We also hope to implement on the UI and UX, as we’ll have more than just this 12-hour period to work on it in the future.

## Built With
Python, NLTK, PyPDF2, Tkinter, Pandas, and easyGUI. 
