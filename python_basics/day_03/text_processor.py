def process_text(text : str):
    text = text.strip().lower()
    word_num = len(text.split())

    return (text, word_num)

print(process_text("  Hello World! Python is GREAT.  "))