# TLDRify

## The "TLDR"
TLDRify is an application that accepts a link from the user and provides a tldr (or summary) of the content present on the given page. 

## Tech Stack
This project was made with React, Next.js, TailwindCSS, Flask, Python, and OpenAI API (REST).

## System Flow
Valid links inputted by the user are sent via POST HTTP Requests to the back-end, where the link is then parsed for HTML content. Parsing is done so through web scraping via the Beautiful Soup library, where the text is scraped from the web page, tokenized with NLTK, and stored into a query along with additional context given to the OpenAI API to provide a tldr of the given information. This query is then stored in a request sent to the API, where the response is then sent back to the front-end to be displayed to the user.

## License
This project is not licensed and therefore the source code is only avaiable for viewing. Please do not use large portions of the source code without my permisssion. 