from flask import Flask, request, jsonify
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import json
import time
import os
import logging
from dotenv import load_dotenv
from prompting import create_translation_prompt
from sanitize_json import sanitize_json
from translation_parser import TranslationOutput, parse_translation_result # Import the sanitize_json function

load_dotenv()

app = Flask(__name__)

# Initialize LLM with local emulator
llm = ChatOpenAI(
    temperature=os.getenv("OPENAI_TEMP"),
    base_url=os.getenv("OPENAI_API_BASE_URL"),
    model=os.getenv("OPENAI_MODEL"),
    api_key=os.getenv("OPENAI_API_KEY")  # Required for ML Studio emulator
)

# Configure logging
logging.basicConfig(level=logging.INFO)

def translate_phrase(german_phrase: str) -> TranslationOutput:
    logging.debug(f"Request: {german_phrase}")
    start_time = time.time()
    
    # First get translation result
        
    translation_result = llm.invoke(create_translation_prompt(german_phrase))
    
    print(translation_result.content)
    
    return parse_translation_result(translation_result.content)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    
    if not data or 'german_phrase' not in data:
        return jsonify({"error": "Missing german_phrase parameter"}), 400
     
    result = translate_phrase(data['german_phrase'])
    return jsonify(result.model_dump())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
