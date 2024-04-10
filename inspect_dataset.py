#!/usr/bin/env python
import argparse
from datasets import load_dataset
# Assuming the tokenizer module and relevant functions are available as described
from tokenizer import TextTokenizer, tokenize_text
from tqdm import tqdm  # For progress bar

def describe_dataset(dataset_name):
    try:
        # Initialize the text tokenizer
        text_tokenizer = TextTokenizer()

        # Load the dataset
        dataset = load_dataset(dataset_name)

        # Initialize total row and token counters
        total_rows = 0
        total_words = 0
        total_tokens = 0

        # Print a basic description of the dataset
        print(f"Description of the dataset {dataset_name}:")
        print(f"Dataset structure: {dataset}")
        print("\nColumn names and their data types:")
        for split in dataset.keys():
            print(f"\n{split} split:")
            for column, dtype in dataset[split].features.items():
                print(f"{column}: {dtype}")

        # Iterate through each split to count rows and tokenize text
        for split in dataset.keys():
            print(f"\nProcessing the {split} split:")
            rows = len(dataset[split])
            total_rows += rows

            # Processing first two examples separately to print text and tokenized text
            for i in range(min(2, rows)):
                sample = dataset[split][i]
                if 'text' in sample:
                    text = sample['text']
                    tokenized_text = tokenize_text(text_tokenizer, text)
                    print(f"\nExample {i+1} original text: {text}")
                    print(f"Tokenized text: {tokenized_text}")

            # Progress bar for the rest of the dataset
            for i in tqdm(range(rows), desc=f"Tokenizing {split} split"):
                sample = dataset[split][i]
                if 'text' in sample and sample['text'] is not None:  # Check if 'text' exists and is not None
                    text = sample['text']
                    word_count = len(text.split())
                    total_words += word_count

                    tokenized_text = tokenize_text(text_tokenizer, text)
                    token_count = len(tokenized_text)
                    total_tokens += token_count
                else:
                    print(f"Skipping row {i} in {split} split due to missing 'text' field.")

            print(f"\nNumber of rows in the {split} split: {rows:,}")

        
        print(f"\nTotal number of rows in the dataset: {total_rows:,}")  # Using thousand separator
        print(f"Total word count in the dataset: {total_words:,}")  # Using thousand separator
        print(f"Total token count in the dataset: {total_tokens:,}")  # Using thousand separator
        print(f"Average words per row: {total_words / total_rows:.2f}")  # Rounded to 2 decimal places
        print(f"Average tokens per row: {total_tokens / total_rows:.2f}")  # Rounded to 2 decimal places


    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Describe a HuggingFace dataset, tokenize a text field, provide aggregate word and token counts, and display progress.")
    parser.add_argument("--dataset_name", type=str, help="Name of the dataset to describe", required=True)

    args = parser.parse_args()
    describe_dataset(args.dataset_name)

if __name__ == "__main__":
    main()

