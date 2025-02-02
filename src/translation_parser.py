from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field

class WordTranslation(BaseModel):
    word: str
    translation: str

class TranslationOutput(BaseModel):
    translation: str
    idiom_explanation: str | None = Field(default=None)
    word_translations: list[WordTranslation] = Field(default_factory=list)

    def __eq__(self, other):
        if not isinstance(other, TranslationOutput):
            return False
        return (
            self.translation == other.translation and
            self.idiom_explanation == other.idiom_explanation and
            self.word_translations == other.word_translations
        )

def extract_translation(text: str) -> Optional[str]:
    """Extract the translation from the text."""
    for line in text.split('\n'):
        if line.strip().startswith('Translation:'):
            return line.strip().replace('Translation:', '').strip()
    return None

def extract_explanation(text: str) -> Optional[str]:
    """Extract the explanation from the text."""
    lines = text.split('\n')
    explanation_lines = []
    in_explanation = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('Explanation:'):
            in_explanation = True
            explanation = line.replace('Explanation:', '').strip()
            # Check if explanation is None or starts with None
            if explanation.lower() == 'none' or explanation.lower().startswith('none.'):
                return None
            explanation_lines.append(explanation)
        elif in_explanation and line and not line.startswith('Word Analysis:'):
            explanation_lines.append(line)
        elif line.startswith('Word Analysis:'):
            break
            
    return ' '.join(explanation_lines) if explanation_lines else None

def extract_word_translations(text: str) -> List[Dict[str, str]]:
    """Extract word translations from the text."""
    word_translations = []
    in_word_analysis = False
    
    for line in text.split('\n'):
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Check if we're in the word analysis section
        if line.startswith('Word Analysis:'):
            in_word_analysis = True
            continue
            
        # Check if we've reached a new section
        if line.startswith('Translation:') or line.startswith('Explanation:'):
            in_word_analysis = False
            continue
            
        # Process word translations
        if in_word_analysis and line.startswith('-'):
            # Remove the leading dash and split on colon
            word_pair = line.lstrip('- ').split(':')
            if len(word_pair) == 2:
                word, translation = word_pair
                word_translations.append({
                    "word": word.strip(),
                    "translation": translation.strip()
                })
    
    return word_translations

def parse_translation_result(text: str) -> TranslationOutput:
    """Parse the complete translation result into a structured format."""
    translation = extract_translation(text)
    explanation = extract_explanation(text)
    word_translations = [
        WordTranslation(word=wt["word"], translation=wt["translation"])
        for wt in extract_word_translations(text)
    ]
    
    return TranslationOutput(
        translation=translation,
        idiom_explanation=explanation,
        word_translations=word_translations
    )
