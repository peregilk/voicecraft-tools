# VoiceCraft Tools
Some tools for VoiceCraft. The first tool inspects the dataset.

```bash
 python inspect_dataset.py --dataset_name pere/nst-voicecraft
```



This should give you some examples of tokenization:

```bash
Original text: Mytene om tusser og troll levde i beste velgående til langt inn i forrige århundre <PERIOD>
Tokenized text: ['m', 'yː', 't', 'ɛ', 'n', 'a', '_', 'uː', 'm', '_', 't', 'ʉ', 's', 's', 'ə', 'r', '_', 'uː', 'ɡ', '_', 't', 'r', 'ɔ', 'l', '_', 'l', 'ɛ', 'v', 'd', 'a', '_', 'iː', '_', 'b', 'ə', 's', 't', 'eː', '_', 'v', 'ɛ', 'l', 'ɡ', 'oː', 'a', 'n', 'n', 'a', '_', 't', 'iː', 'l', '_', 'l', 'ɑ', 'ŋ', 't', '_', 'ɪ', 'n', '_', 'iː', '_', 'f', 'ɔ', 'r', 'r', 'iː', 'ɡ', 'a', '_', 'ɔ', 'r', 'h', 'ʉ', 'n', 'n', 'r', 'a', '_', 'p', 'eː', 'r', 'iː', 'uː', 'd']
```

It should also give you a status like this:

```bash
Total number of rows in the dataset: 227240
Total word count in the dataset: 2191506
Total token count in the dataset: 12400734
Average words per row: 9.644015138179897
Average tokens per row: 54.57108783664848
```
