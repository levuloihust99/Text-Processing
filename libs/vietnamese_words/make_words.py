import json
import argparse
from pathlib import Path

from trie import Trie
from pair_rules import Rule


def main():
    sounds_path = Path(__file__).parent / "assets/sounds.json"
    rules_path  = Path(__file__).parent / "assets/pair_rules.json"
    words_path = Path(__file__).parent / "assets/words.txt"

    with sounds_path.open(mode="r") as reader:
        data = json.load(reader)
    trie = Trie()
    trie.root = data
    
    with rules_path.open(mode="r") as reader:
        rules = json.load(reader)
    words = []
    for consonant, rule_data in rules.items():
        rule = Rule.parse(rule_data, trie)
        sounds = rule.execute()
        for sound in sounds:
            words.append(consonant + sound)
    with words_path.open(mode="w") as writer:
        for word in words:
            writer.write(word + "\n")


if __name__ == "__main__":
    main()
