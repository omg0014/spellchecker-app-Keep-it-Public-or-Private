from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            # Generate suggestions
            suggestions = list(self.spell.candidates(word))

            if corrected_word != word.lower():
                print(f'\nWord: "{word}"')
                print(f'Correction: "{corrected_word}"')
                print(f'Suggestions: {suggestions}')

            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    def run(self):
        print("\n---- Spell Checker ----")

        while True:
            text = input('Enter text to check (or type "exit" to quit): ')

            if text.lower() == 'exit':
                print('Closing the program...')
                break

            corrected_text = self.correct_text(text)
            print(f'\nCorrected Text: {corrected_text}\n')


app = SpellCheckerApp()
app.run()