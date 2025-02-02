import unittest
from translation_parser import (
    extract_translation,
    extract_explanation,
    extract_word_translations,
    parse_translation_result,
    TranslationOutput,
    WordTranslation
)

class TestTranslationParser(unittest.TestCase):
    
    def test_extract_translation(self):
        # Test with example from comments
        text = ''' Translation: To demand an extra sausage
                 Explanation: None. This phrase does not contain a figurative meaning and is directly translatable.
                 Word Analysis:
                 - eine: a/an
                 - Extrawurst: extra sausage (literally "extra sausage")
                 - verlangen: to demand'''
        self.assertEqual(extract_translation(text), "To demand an extra sausage")
        
        # Test with no translation
        self.assertIsNone(extract_translation("No translation here"))
        
    def test_extract_explanation(self):
        # Test with example from comments
        text = ''' Translation: It's all Greek to me.
             Explanation: This is a common German idiom meaning someone doesn't understand something at all. The literal translation "I only understand train station" does not reflect its intended meaning, which stems from the fact that many people find it difficult to understand the layout and complexity of train stations.
             Word Analysis:
             - ich: I
             - versteh: understand
             - nur: only
             - Bahnhof: train station (literal word-by-word translation)'''
        expected = "This is a common German idiom meaning someone doesn't understand something at all. The literal translation \"I only understand train station\" does not reflect its intended meaning, which stems from the fact that many people find it difficult to understand the layout and complexity of train stations."
        self.assertEqual(extract_explanation(text), expected)
        
        # Test with no explanation
        self.assertIsNone(extract_explanation("No explanation here"))
        
        # Test with "None" explanation
        text = '''# Translation: To have pigs.
            # Explanation: None
            # Word Analysis:
            # - Schwein: Pig
            # - haben: to have'''
        self.assertIsNone(extract_explanation(text))
        
    def test_extract_word_translations(self):
        # Test with example from comments
        text = ''' Translation: That's the crux of the matter.
             Explanation: It refers to bringing up the essential point or truth when discussing a situation, often unexpectedly. This idiom is commonly used in German discussions to highlight the main issue.
             Word Analysis:
             - Da: There/Here
             - liegt: lies
             - der Hund begraben: buried dog (idiomatically meaning "the nub" or "the punchline")'''
        expected = [
            {"word": "Da", "translation": "There/Here"},
            {"word": "liegt", "translation": "lies"},
            {"word": "der Hund begraben", "translation": "buried dog (idiomatically meaning \"the nub\" or \"the punchline\")"}
        ]
        self.assertEqual(extract_word_translations(text), expected)
        
        # Test with no word analysis
        self.assertEqual(extract_word_translations("No word analysis here"), [])
        
    def test_parse_translation_result(self):
        # Test complete parsing
        text = ''' Translation: To demand an extra sausage
             Explanation: None. This phrase does not contain a figurative meaning and is directly translatable.
             Word Analysis:
             - eine: a/an
             - Extrawurst: extra sausage (literally "extra sausage")
             - verlangen: to demand'''
        
        expected = TranslationOutput(
            translation="To demand an extra sausage",
            idiom_explanation=None,
            word_translations=[
                WordTranslation(word="eine", translation="a/an"),
                WordTranslation(word="Extrawurst", translation='extra sausage (literally "extra sausage")'),
                WordTranslation(word="verlangen", translation="to demand")
            ]
        )
        result = parse_translation_result(text)
        self.assertDictEqual(result.model_dump(), expected.model_dump())

if __name__ == '__main__':
    unittest.main()