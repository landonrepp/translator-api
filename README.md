# Translator API

A Python-based translation service API. It returns a direct translation of a given sentence or phrase, translations of each individual word in isolation, and an explanation of any idioms used.

The API is only designed to translate German text to English now, but can be easily extended.

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   
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

## Running the Application with Docker

1. Build the Docker image:
   ```bash
   docker build -t translator-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 translator-api
   ```

3. Access the application at `http://127.0.0.1:8000`.

## Running the Application (without Docker)

1. Set up environment variables by copying `.env.example` to `.env` and filling in the values
2. Run the application:
   ```bash
    export FLASK_DEBUG=1 && export FLASK_APP=src/app.py && flask run --port 5001
   ```

## Testing

Run tests using:
```bash
python -m pytest
```


## Sample payload

### Input

```json
[POST] http://127.0.0.1:5001/translate
{
    "german_phrase": "Guten Tag"
}
```

## Output
```json
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
```