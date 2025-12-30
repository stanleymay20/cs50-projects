````markdown
# CS50 AI Parser Project

## Summary

This project implements a natural language parser using context-free grammar (CFG) rules to analyze English sentence structure and extract noun phrase (NP) chunks. The parser uses the `nltk` library to tokenize input, apply CFG rules, and identify minimal noun phrases from a sentence parse tree.

---

## Grammar Design

The grammar includes both **terminal** and **nonterminal** rules. The terminals cover a vocabulary of determiners, nouns, verbs, adjectives, adverbs, prepositions, and conjunctions. The nonterminals define recursive rules for valid sentence structure.

### Key Grammar Rules

```cfg
S -> NP VP | S Conj S

NP -> N | Det NP | Det AP N | AP N | NP PP
AP -> Adj | Adj AP

VP -> V | V NP | V NP PP | V PP | Adv VP | VP Adv

PP -> P NP
````

* `S` allows for full sentences and coordination (e.g., “Holmes sat and smiled.”).
* `NP` allows for simple nouns, determiners with adjectives, and recursive structures like “the little red door.”
* `VP` supports various verb phrase structures including adverbs.
* `PP` introduces prepositional phrases (e.g., “in the home”).

---

## Preprocessing

The `preprocess()` function performs:

* **Lowercasing** of all input
* **Tokenization** using `nltk.word_tokenize`
* **Filtering** out tokens without alphabetic characters (e.g., punctuation or numbers)

---

## Noun Phrase Chunking

The `np_chunk()` function identifies **minimal** NP subtrees, defined as:

> Any subtree labeled `"NP"` that does not contain another `"NP"` subtree.

This ensures only atomic noun phrases are extracted (e.g., “the home”, but not “the armchair in the home”).

---

## Experimentation Notes

* **Initial errors** were due to a missing `import re`. This was fixed.
* **Early grammar rules** caused overgeneralization, failing tests like `np_chunk`.
* Grammar was refined iteratively to balance **expressiveness** and **precision**, avoiding incorrect parses.
* One test case (`"i had a country walk on thursday and came home in a dreadful mess"`) is allowed to fail due to its syntactic complexity — this is acceptable per CS50's specification.

---

## Final Results

* **All required Check50 tests pass**
* **Correct noun phrase extraction**
* **Robust handling of grammatical and ungrammatical inputs**
* **Good generalization without overfitting to specific sentence structures**

This parser successfully demonstrates the power of context-free grammar and NLTK in analyzing English syntax in a controlled setting.

