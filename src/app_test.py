import unittest
from app import translate_phrase

class TestTranslation(unittest.TestCase):
    def test_guten_tag_translation(self):
        result = translate_phrase("guten tag")
        self.assertIsNotNone(result.translation)
        self.assertIsNone(result.idiom_explanation)
        # Test word translations
        self.assertIsNotNone(result.word_translations)
        self.assertEqual(len(result.word_translations), 2)  # "guten" and "tag"
        for word_trans in result.word_translations:
            self.assertIsInstance(word_trans.word, str)
            self.assertIsInstance(word_trans.translation, str)

    def test_schlafen_wie_ein_murmeltier_translation(self):
        result = translate_phrase("schlafen wie ein Murmeltier")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_um_den_heißen_brei_herumreden(self):
        result = translate_phrase("um den heißen Brei herumreden")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_da_kannst_du_gift_drauf_nehmen(self):
        result = translate_phrase("da kannst du Gift drauf nehmen")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_sich_zum_affen_machen(self):
        result = translate_phrase("sich zum Affen machen")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_zwei_fliegen_mit_einer_klappe_schlagen(self):
        result = translate_phrase("zwei Fliegen mit einer Klappe schlagen")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_eine_extrawurst_verlangen(self):
        result = translate_phrase("eine Extrawurst verlangen")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_tomaten_auf_den_augen_haben(self):
        result = translate_phrase("Tomaten auf den Augen haben")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_den_nagel_auf_den_kopf_treffen(self):
        result = translate_phrase("den Nagel auf den Kopf treffen")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_ich_verstehe_nur_bahnhof(self):
        result = translate_phrase("ich verstehe nur Bahnhof")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)
        # Test word translations for idiom
        self.assertIsNotNone(result.word_translations)
        self.assertEqual(len(result.word_translations), 4)  # "ich", "verstehe", "nur", "Bahnhof"
        # Verify specific word translations
        words = [wt.word for wt in result.word_translations]
        self.assertIn("ich", words)
        self.assertIn("verstehe", words)
        self.assertIn("nur", words)
        self.assertIn("Bahnhof", words)
        # Check that each word translation has required fields
        for word_trans in result.word_translations:
            self.assertIsInstance(word_trans.word, str)
            self.assertIsInstance(word_trans.translation, str)

    def test_jemandem_die_daumen_drücken(self):
        result = translate_phrase("jemandem die Daumen drücken")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_lügen_haben_kurze_beine(self):
        result = translate_phrase("Lügen haben kurze Beine")
        self.assertIsNotNone(result.translation)
        self.assertIsNotNone(result.idiom_explanation)

    def test_word_translations_structure(self):
        """Test to verify the structure of word translations for any phrase"""
        result = translate_phrase("Ich hab ein menge Hunger")
        self.assertIsNotNone(result.word_translations)
        self.assertGreater(len(result.word_translations), 0)
        
        for word_trans in result.word_translations:
            # Check all required fields are present
            self.assertTrue(hasattr(word_trans, 'word'))
            self.assertTrue(hasattr(word_trans, 'translation'))
            
            # Check all fields have content
            self.assertGreater(len(word_trans.word), 0)
            self.assertGreater(len(word_trans.translation), 0)

if __name__ == "__main__":
    unittest.main()
