import itertools
import random
import os
import string
from typing import List, Generator, Set
from datetime import datetime

# -------------------- CONFIGURATION -------------------- #
LEET_MAP = {
    'a': ['@', '4'],
    'b': ['8'],
    'e': ['3'],
    'i': ['1', '!'],
    'l': ['1'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['7'],
    'g': ['9']
}

SYMBOLS = ['!', '@', '#', '$', '%', '&', '*', '-', '_']
NUMBERS = [str(i) for i in range(10)] + [str(i).zfill(2) for i in range(100)]

TARGET_COUNT = 100_000_000
BATCH_SIZE = 5000

# ------------------ TRANSFORMATION ENGINE ------------------ #
class KeywordTransformer:
    @staticmethod
    def leet_variants(word: str) -> Set[str]:
        variants = set()

        def _helper(w, i):
            if i == len(w):
                variants.add(w)
                return
            char = w[i].lower()
            if char in LEET_MAP:
                for rep in LEET_MAP[char]:
                    _helper(w[:i] + rep + w[i+1:], i+1)
            _helper(w, i+1)

        _helper(word, 0)
        return variants

    @staticmethod
    def case_variants(word: str) -> Set[str]:
        return {
            word.lower(),
            word.upper(),
            word.capitalize(),
            ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word)])
        }

    @staticmethod
    def reverse(word: str) -> str:
        return word[::-1]

    @staticmethod
    def transform(words: List[str]) -> Set[str]:
        transformed = set()
        for word in words:
            transformed.update(KeywordTransformer.case_variants(word))
            leets = KeywordTransformer.leet_variants(word)
            transformed.update(leets)
            for lw in leets:
                transformed.add(KeywordTransformer.reverse(lw))
            transformed.add(KeywordTransformer.reverse(word))
        return transformed

# ------------------ PATTERN COMBINATOR ------------------ #
class PasswordPatternEngine:
    @staticmethod
    def generate_combinations(words: List[str], min_len: int, max_len: int) -> Generator[str, None, None]:
        for r in range(1, 4):  # 1-word, 2-word, 3-word combinations
            for combo in itertools.permutations(words, r):
                base = ''.join(combo)
                if min_len <= len(base) <= max_len:
                    yield base
                # Append/prepend symbols or numbers
                for sym in SYMBOLS:
                    variants = [
                        sym + base,
                        base + sym,
                        base[:len(base)//2] + sym + base[len(base)//2:]
                    ]
                    for var in variants:
                        if min_len <= len(var) <= max_len:
                            yield var

                for num in NUMBERS:
                    variants = [
                        num + base,
                        base + num,
                        base[:len(base)//2] + num + base[len(base)//2:]
                    ]
                    for var in variants:
                        if min_len <= len(var) <= max_len:
                            yield var

                # Symbol + Number patterns
                for sym in SYMBOLS:
                    for num in NUMBERS:
                        pattern1 = f"{sym}{base}{num}"
                        pattern2 = f"{num}{sym}{base}"
                        pattern3 = f"{base}{sym}{num}"
                        for var in [pattern1, pattern2, pattern3]:
                            if min_len <= len(var) <= max_len:
                                yield var

# ------------------ OUTPUT WRITER ------------------ #
class PasswordWriter:
    def __init__(self, filepath: str):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

    def write(self, generator: Generator[str, None, None], limit: int = TARGET_COUNT):
        count = 0
        batch = []

        with open(self.filepath, 'w', encoding='utf-8') as f:
            for pw in generator:
                batch.append(pw)
                count += 1
                if len(batch) >= BATCH_SIZE:
                    f.write('\n'.join(batch) + '\n')
                    batch.clear()
                if count >= limit:
                    break
            if batch:
                f.write('\n'.join(batch) + '\n')

        print(f"\n✅ {count} passwords saved to: {self.filepath}")

# ------------------ MAIN APPLICATION ------------------ #
class PasswordGeneratorApp:
    def run(self):
        print("🔐 Dz PLG ")
        keywords = input("Enter base keywords (e.g., names, dates): ").split()
        min_len = int(input("Minimum password length: "))
        max_len = int(input("Maximum password length: "))
        output_file = f"output/password_list_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        print("\n🔄 Transforming keywords...")
        transformed_words = list(KeywordTransformer.transform(keywords))
        print(f"✨ Generated {len(transformed_words)} unique keyword variants.")

        print("🚀 Generating and writing passwords...")
        generator = PasswordPatternEngine.generate_combinations(transformed_words, min_len, max_len)
        writer = PasswordWriter(output_file)
        writer.write(generator)
        print("Aya Bsahtk !! ")

# ------------------ ENTRY POINT ------------------ #
if __name__ == "__main__":
    PasswordGeneratorApp().run()
