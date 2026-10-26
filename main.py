from tkinter import *

triggers = {
    "research":  ["research", "sources", "citations", "paper", "literature", "latest", "news", "facts"],
    "coding":    ["code", "python", "java", "bug", "debug", "program", "function", "error", "script", "algorithm"],
    "writing":   ["write", "essay", "email", "blog", "letter", "story", "rewrite", "proofread", "draft"],
    "study":     ["learn", "explain", "understand", "exam", "concept", "revise", "teach", "homework"],
    "data":      ["data", "analyze", "analysis", "excel", "csv", "chart", "spreadsheet", "statistics"],
    "summarize": ["summarize", "summary", "shorten", "pdf", "document", "lengthy"],
}

order = {
    "research":  ["Perplexity", "Gemini", "ChatGPT", "Copilot"],
    "coding":    ["Claude", "DeepSeek", "ChatGPT", "Gemini", "Copilot"],
    "writing":   ["Claude", "ChatGPT", "Gemini", "Copilot"],
    "study":     ["ChatGPT", "DeepSeek", "Gemini", "Claude"],
    "data":      ["ChatGPT", "Gemini", "Copilot", "Claude"],
    "summarize": ["Gemini", "Claude", "ChatGPT"],
}

keywords = {
    "research":  ["cite sources", "with links", "latest as of [date]", "compare viewpoints", "limitations"],
    "coding":    ["step-by-step", "edge cases", "time complexity", "explain each line", "minimal example"],
    "writing":   ["tone", "target audience", "word limit", "avoid jargon", "rewrite"],
    "study":     ["ELI5", "analogy", "quiz me", "key takeaways", "common mistakes"],
    "data":      ["table format", "state assumptions", "outliers", "show calculation", "trend"],
    "summarize": ["TL;DR", "key points", "in N words", "action items", "preserve numbers"],
}

good_for = {
    "Perplexity": {
        "research": "Searches the web live and shows sources with links.",
    },
    "Gemini": {
        "research":  "Broad searching and long documents, linked with Google.",
        "coding":    "Handles large code and many languages.",
        "writing":   "Quick drafts and rewrites.",
        "study":     "Explains topics with examples.",
        "data":      "Works well with Google Sheets and large data.",
        "summarize": "Handles very long documents and PDFs.",
    },
    "ChatGPT": {
        "research":  "Good for explaining and organizing research findings.",
        "coding":    "Versatile for writing, debugging and explaining code.",
        "writing":   "Flexible drafting across many styles.",
        "study":     "Explains concepts step by step and can quiz you.",
        "data":      "Can analyze files and produce tables and charts.",
        "summarize": "Fast summaries in the length and format you ask for.",
    },
    "Copilot": {
        "research": "Web-connected answers with links for quick lookups.",
        "coding":   "Suggestions inside coding tools like VS Code and GitHub.",
        "writing":  "Helps write emails and documents inside Microsoft apps.",
        "data":     "Works inside Excel for formulas and analysis.",
    },
    "Claude": {
        "coding":    "Writes and explains clean code, good at long code and debugging.",
        "writing":   "Natural, careful writing tone.",
        "study":     "Patient, clear explanations of difficult ideas.",
        "data":      "Careful reasoning about data and clear explanations of results.",
        "summarize": "Accurate summaries of long text that keep key details.",
    },
    "DeepSeek": {
        "coding": "Strong step-by-step reasoning for writing, debugging, and algorithms.",
        "study":  "Patient logical explanations for math, science, and difficult concepts.",
    },
}

matched_category = ""

def find_llms():
    global matched_category

    task_text = task_entry.get()
    lowercase_text = task_text.lower()
    raw_words = lowercase_text.split()
    clean_words = []
    for word in raw_words:
        cleaned_word = word.strip(".,?!;")
        clean_words.append(cleaned_word)

    best_category = ""
    highest_count = 0

    for category in triggers:
        count = 0
        trigger_words = triggers[category]
        for word in clean_words:
            if word in trigger_words:
                count = count + 1

        if count > highest_count:
            highest_count = count
            best_category = category

    if highest_count == 0:
        matched_category = ""
        message_label.config(text="Please describe your task with more detail", fg="#dc2626")
        llm_listbox.delete(0, END)
        logo_label.config(image="")
        name_label.config(text="")
        good_for_label.config(text="")
        keywords_label.config(text="")
    else:
        matched_category = best_category
        message_label.config(text="Category: " + matched_category, fg="#2563eb")
        llm_listbox.delete(0, END)
        for llm in order[matched_category]:
            llm_listbox.insert(END, llm)
        logo_label.config(image="")
        name_label.config(text="")
        good_for_label.config(text="")
        keywords_label.config(text="")

def show_details():
    selected_indices = llm_listbox.curselection()
    if len(selected_indices) == 0:
        name_label.config(text="Please select an LLM first", fg="#dc2626")
        logo_label.config(image="")
        good_for_label.config(text="")
        keywords_label.config(text="")
        return

    selected_index = selected_indices[0]
    selected_llm = llm_listbox.get(selected_index)

    logo_path = "logos/" + selected_llm.lower() + ".png"
    logo_image = PhotoImage(file=logo_path)
    logo_label.config(image=logo_image)
    logo_label.image = logo_image

    name_label.config(text=selected_llm, fg="#111827")
    good_for_label.config(text="Good for: " + good_for[selected_llm][matched_category])
    keywords_label.config(text="Keywords: " + ", ".join(keywords[matched_category]))

window = Tk()
window.title("Prompt Pilot")
window.geometry("420x640")
window.configure(bg="#f3f4f6")

title_label = Label(window, text="Prompt Pilot", font=("Helvetica", 18, "bold"), fg="#111827", bg="#f3f4f6")
title_label.pack(pady=(14, 4))

instruction_label = Label(window, text="Describe your task:", font=("Helvetica", 10), fg="#4b5563", bg="#f3f4f6")
instruction_label.pack(pady=4)

task_entry = Entry(window, width=34, font=("Helvetica", 11), bg="#ffffff", fg="#111827", relief="solid", bd=1)
task_entry.pack(pady=6)

find_button = Button(window, text="Find LLMs", font=("Helvetica", 10, "bold"), bg="#2563eb", fg="#ffffff", highlightbackground="#2563eb", cursor="hand2")
find_button.config(command=find_llms)
find_button.pack(pady=6)

message_label = Label(window, text="", font=("Helvetica", 11, "bold"), fg="#2563eb", bg="#f3f4f6")
message_label.pack(pady=4)

llm_listbox = Listbox(window, height=5, width=26, font=("Helvetica", 11), bg="#ffffff", fg="#1f2937", selectbackground="#2563eb", selectforeground="#ffffff", relief="solid", bd=1)
llm_listbox.pack(pady=4)

details_button = Button(window, text="Show details", font=("Helvetica", 10, "bold"), bg="#059669", fg="#ffffff", highlightbackground="#059669", cursor="hand2")
details_button.config(command=show_details)
details_button.pack(pady=6)

logo_label = Label(window, bg="#f3f4f6")
logo_label.pack(pady=4)

name_label = Label(window, text="", font=("Helvetica", 13, "bold"), fg="#111827", bg="#f3f4f6")
name_label.pack(pady=2)

good_for_label = Label(window, text="", wraplength=360, justify="center", font=("Helvetica", 10), fg="#374151", bg="#f3f4f6")
good_for_label.pack(pady=2)

keywords_label = Label(window, text="", wraplength=360, justify="center", font=("Helvetica", 9, "italic"), fg="#6b7280", bg="#f3f4f6")
keywords_label.pack(pady=2)

window.mainloop()
