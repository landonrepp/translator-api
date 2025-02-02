# Translator API

A Python-based translation service API. It returns a direct translation of a given sentence or phrase, translations of each individual word in isolation, and an explanation of any idioms used.

The API is only designed to translate German text to English now, but can be easily extended.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Set up environment variables by copying `.env.example` to `.env` and filling in the values
2. Run the application:
   ```bash
   python app.py
   ```

## Testing

Run tests using:
```bash
python -m pytest


## Sample payload

### Input

[POST] http://127.0.0.1:5001/translate
{
    "german_phrase": "Guten Tag"
}

## Output
{
    "idiom_explanation": null,
    "translation": "Good day",
    "word_translations": [
        {
            "translation": "Good",
            "word": "Guten"
        },
        {
            "translation": "day",
            "word": "Tag"
        }
    ]
}