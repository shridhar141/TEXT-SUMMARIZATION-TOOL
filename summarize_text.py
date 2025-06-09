from transformers import pipeline

# Initialize the summarization pipeline once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summarize_text(text, min_length=30, max_length=None):
    """
    Summarizes the input text using a pre-trained transformer model.

    Parameters:
    - text (str): The input article or document.
    - min_length (int): Minimum length of the summary.
    - max_length (int or None): Maximum length of the summary. If None, set dynamically.

    Returns:
    - summary (str): A concise summary of the input.
    """
    input_length = len(text.split())

    # Dynamically set max_length: half the input length, but between 30 and 60 tokens
    if max_length is None:
        max_length = min(60, max(30, input_length // 2))

    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("=== TEXT SUMMARIZATION TOOL ===")
    input_text = input("\nPaste the article or document you want to summarize:\n\n").strip()

    if len(input_text.split()) < 50:
        print("\n⚠️ Please enter a longer article for meaningful summarization.")
    else:
        print("\n🔍 Summarizing...\n")
        try:
            summary = summarize_text(input_text)
            print("\n✅ Summary:\n", summary)
        except Exception as e:
            print("❌ Error during summarization:", str(e))
