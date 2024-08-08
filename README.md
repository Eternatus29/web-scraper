# WEB SCRAPER

Kindly follow these instructions to get the project up and running on your system.

## Prerequisites

Before you start, make sure you have Python 3.10.12 installed on your system. Additionally, you might need `python3-pip` and `python3.10-venv` if you're on Linux, but these are optional.

## Setup Instructions

1. **Install Dependencies**

   First, go to the project root directory. Install all the required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

   All the necessary libraries specified in the `requirements.txt` file.

2. **Download SpaCy Model**

   I have used SpaCy for Named Entity Recognition. Download the SpaCy model with the following command:

   ```bash
   python3 -m spacy download en_core_web_sm
   ```

   Note: `en_core_web_lg` model instead of `en_core_web_sm` for more accurate results. 

3. **Start the Application**

   To start the application, run:

   ```bash
   python3 app.py
   ```

   The application will ask you for the URL of a web page from which the content will be scraped. Make sure that the webpage is publicly accessible so that a successful HTTP GET request returns a status code of 200.

## Usage

Once the application is running, you can enter the URL of the web page you want to scrape. The application will process the content and perform Named Entity Recognition on it.