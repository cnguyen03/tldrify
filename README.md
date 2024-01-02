# TLDRify

## The "TLDR"
TLDRify is an application that accepts a link from the user and provides a tldr (or summary) of the content present on the given page. 

## Tech Stack
This project was made with React, Next.js, TailwindCSS, Flask, Python, and Hugging-Face AI Pipeline for Summaries.

## System Flow
Valid links inputted by the user are sent via POST HTTP Requests to the back-end, where the link is then parsed for HTML content. Parsing is done so through web scraping via the Beautiful Soup library, where the text is scraped from the web page, tokenized with NLTK, and used to generate a summary with an AI-powered transformer model pre-trained to provide a tldr of the given information. This summary is then stored in a response that is sent back to the front-end to be displayed to the user.

## License
This project is not licensed and therefore the source code is only avaiable for viewing. Please do not use large portions of the source code without my permisssion. 
