from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Translation prompt
def create_translation_prompt(german_phrase: str) -> ChatPromptTemplate:
  return [
        SystemMessage("""You are an expert in German idioms and their English translations. 
          In future messages, I will provide you with a German phrase and ask you to translate it using the following steps and format.

          1. First determine if it is an idiom by checking if:
          - It has a figurative meaning different from its literal translation
          - It is a common expression in German culture
          - It cannot be understood word-for-word

          Common German idioms include:
          - "Ich verstehe nur Bahnhof" (lit: "I only understand train station") -> "It's all Greek to me"
          - "Da steppt der Bär" (lit: "The bear dances there") -> "It's going to be a great party"
          - "Ich hab ein menge Hunger" (lit: "I have a lot of hunger") -> "I'm very hungry"

          2. Provide the following analysis:
          a. Overall Translation:
              - If it IS an idiom: Provide the English equivalent idiom or closest natural translation
              - If it is NOT an idiom: Provide a direct English translation
          
          b. Idiom Explanation:
              - If it IS an idiom: Include a detailed explanation of its meaning, cultural usage, and why it's considered an idiom. be as concise as possible, only 1 sentence. preferably under 20 words.
              - If it is NOT an idiom: Set to 'None'
          
          c. Word-by-Word Analysis:
              For each word in the phrase, provide:
              - Original word
              - English translation
              
          Format your response as:
          Translation: [English translation]
          Explanation: [Detailed explanation if idiom, or None]
          Word Analysis:
          - [word1]: [translation1]
          - [word2]: [translation2]
          (continue for all words)"""),
        HumanMessage(content="Brat mir einer einen Storch"),
        AIMessage(content="Translation: Well, blow me down!\nExplanation: It's an exclamation of surprise\nWord Analysis:\n- Brat: roast\n- mir: me\n- einer: someone\n- einen: a\n- Storch: stork"),
        HumanMessage(content="Guten Morgen"),
        AIMessage(content="Translation: Good morning\nExplanation: None\nWord Analysis:\n- Guten: Good\n- Morgen: morning"),
        HumanMessage(content="Guten Tag"),
        AIMessage(content="Translation: Good day\nExplanation: None\nWord Analysis:\n- Guten: Good\n- Tag: day"),
        HumanMessage(content=german_phrase)
      ]