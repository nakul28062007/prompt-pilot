from tkinter import *

triggers = {
    "research": [
        "research", "source", "citation", "paper", "literature", "latest", "news", "fact",
        "reference", "journal", "scholar", "survey", "verify", "evidence", "current",
        "trend", "report", "investigate", "findings", "credible", "reliable", "studies",
        "history", "background", "whitepaper", "thesis", "dissertation", "review",
        "official", "update", "happening", "recent",
    ],
    "coding": [
        "code", "coding", "python", "java", "javascript", "bug", "bugs", "debug", "program",
        "function", "error", "script", "algorithm", "html", "css", "sql", "nextjs", "reactjs",
        "backend", "frontend", "database", "compile", "syntax", "developer", "tkinter",
        "loop", "exception", "crash", "software", "website", "android", "leetcode", "dsa",
        "refactor", "deploy", "terminal", "regex", "json", "variable", "class", "oop",
        "flask", "django", "nodejs", "typescript", "github", "repository", "optimize",
        "implement", "develop", "build", "app", "api", "library", "framework", "cpp",
    ],
    "writing": [
        "write", "essay", "email", "blog", "letter", "story", "rewrite", "proofread", "draft",
        "grammar", "paragraph", "article", "caption", "poem", "resume", "speech", "linkedin",
        "tone", "content", "paraphrase", "edit", "copywriting", "newsletter", "script",
        "post", "message", "reply", "apply", "application", "cover", "statement", "bio",
        "slogan", "tagline", "description", "formal", "polite", "improve", "wording",
    ],
    "study": [
        "learn", "explain", "understand", "exam", "exams", "concept", "revise", "teach",
        "homework", "lecture", "syllabus", "tutor", "notes", "quiz", "chapter", "assignment",
        "subject", "theory", "study", "prepare", "preparation", "revision", "course",
        "beginner", "basics", "tutorial", "simple", "meaning", "difference", "why",
        "how", "textbook", "viva", "semester", "university", "college", "school",
        "flashcards", "practice", "doubt", "doubts",
    ],
    "data": [
        "data", "analyze", "analysis", "analytics", "excel", "csv", "chart", "spreadsheet",
        "statistic", "graph", "graphs", "plot", "plots", "dashboard", "pandas", "visualize",
        "pivot", "dataset", "forecast", "metrics", "sheet", "sheets", "numpy", "regression",
        "correlation", "average", "mean", "median", "database", "query", "numbers",
        "figures", "kpi", "insights", "clean", "cleaning", "tableau", "powerbi",
    ],
    "summarize": [
        "summarize", "summary", "summarise", "shorten", "pdf", "document", "lengthy", "tldr",
        "condense", "brief", "digest", "overview", "recap", "abstract", "highlights",
        "gist", "short", "long", "shorter", "minutes", "transcript", "report", "key",
        "extract", "outline", "points", "compress", "trim", "essence", "capsule",
    ],
    "math": [
        "math", "maths", "mathematics", "calculate", "calculation", "equation", "solve",
        "algebra", "calculus", "integral", "derivative", "probability", "geometry",
        "trigonometry", "theorem", "formula", "matrix", "arithmetic", "percentage",
        "simplify", "proof", "prove", "number", "numerical", "statistics", "logarithm",
        "factorial", "permutation", "combination", "limit", "vector", "puzzle", "aptitude",
        "ratio", "sum", "average", "speed", "profit", "interest",
    ],
    "translation": [
        "translate", "translation", "translating", "hindi", "tamil", "french", "spanish",
        "german", "japanese", "korean", "chinese", "arabic", "multilingual", "localize",
        "localization", "language", "languages", "telugu", "malayalam", "kannada",
        "russian", "italian", "portuguese", "bilingual", "interpret", "interpreter",
        "subtitle", "subtitles", "dialect",
    ],
    "brainstorm": [
        "brainstorm", "idea", "ideas", "creative", "startup", "pitch", "innovate",
        "innovation", "strategy", "suggest", "suggestions", "name", "names", "naming",
        "brand", "campaign", "marketing", "plan", "planning", "project", "hackathon",
        "business", "options", "alternatives", "inspire", "inspiration", "theme",
        "themes", "concepts", "think", "possibilities", "gift", "gifts", "topic",
    ],
    "design": [
        "image", "images", "logo", "poster", "picture", "draw", "illustration", "sketch",
        "wallpaper", "thumbnail", "banner", "graphic", "graphics", "photo", "photos",
        "visual", "design", "designs", "mockup", "wireframe", "icon", "icons", "painting",
        "artwork", "cartoon", "avatar", "portrait", "render", "ui", "ux", "layout",
        "palette", "flyer", "brochure", "infographic", "generate",
    ],
}

order = {
    "research":    ["Perplexity", "Gemini", "ChatGPT", "Copilot"],
    "coding":      ["Claude", "DeepSeek", "ChatGPT", "Gemini", "Copilot"],
    "writing":     ["Claude", "ChatGPT", "Gemini", "Copilot"],
    "study":       ["ChatGPT", "DeepSeek", "Gemini", "Claude"],
    "data":        ["ChatGPT", "Gemini", "Copilot", "Claude"],
    "summarize":   ["Gemini", "Claude", "ChatGPT"],
    "math":        ["DeepSeek", "ChatGPT", "Gemini", "Claude"],
    "translation": ["Gemini", "ChatGPT", "Claude", "DeepSeek"],
    "brainstorm":  ["ChatGPT", "Claude", "Gemini", "Copilot"],
    "design":      ["ChatGPT", "Gemini", "Copilot"],
    "general":     ["ChatGPT", "Gemini", "Claude", "Copilot", "DeepSeek", "Perplexity"],
}

keywords = {
    "research":    ["cite sources", "with links", "latest as of [date]", "compare viewpoints",
                    "state limitations", "fact-check claims", "group by source",
                    "separate facts from opinions"],
    "coding":      ["step-by-step", "edge cases", "time complexity", "explain each line",
                    "minimal example", "add comments", "handle errors", "optimize it"],
    "writing":     ["tone", "target audience", "word limit", "avoid jargon", "rewrite",
                    "active voice", "3 variations", "key message"],
    "study":       ["ELI5", "analogy", "quiz me", "key takeaways", "common mistakes",
                    "real-world example", "step-by-step", "practice questions"],
    "data":        ["table format", "state assumptions", "outliers", "show calculation",
                    "trend", "suggest a chart", "missing values", "summary statistics"],
    "summarize":   ["TL;DR", "key points", "in N words", "action items", "preserve numbers",
                    "bullet format", "main argument", "do not add new info"],
    "math":        ["show steps", "final answer", "verify the result", "formula used",
                    "alternative method", "include units", "worked example", "common pitfalls"],
    "translation": ["preserve tone", "formal vs casual", "keep idioms", "transliteration",
                    "regional dialect", "side-by-side", "explain nuances", "keep formatting"],
    "brainstorm":  ["10 ideas", "unconventional", "pros and cons", "rank by feasibility",
                    "constraints", "target audience", "mix of safe and bold", "next steps"],
    "design":      ["style", "color palette", "aspect ratio", "mood", "lighting",
                    "composition", "background", "level of detail"],
    "general":     ["clear goal", "give context", "desired format", "constraints",
                    "add examples", "step-by-step", "ask clarifying questions", "tone"],
}

good_for = {
    "Perplexity": {
        "research":  "Searches the web live and shows sources with links.",
        "general":   "Best when you need current facts with sources.",
    },
    "Gemini": {
        "research":    "Broad searching and long documents, linked with Google.",
        "coding":      "Handles large code and many languages.",
        "writing":     "Quick drafts and rewrites.",
        "study":       "Explains topics with examples.",
        "data":        "Works well with Google Sheets and large data.",
        "summarize":   "Handles very long documents and PDFs.",
        "math":        "Solid at general problems and explains the working.",
        "translation": "Strong across many languages, including Indian ones.",
        "brainstorm":  "Gives wide-ranging ideas quickly.",
        "design":      "Generates and edits images inside Google tools.",
        "general":     "Good all-rounder, linked with Google apps.",
    },
    "ChatGPT": {
        "research":    "Good for explaining and organizing research findings.",
        "coding":      "Versatile for writing, debugging and explaining code.",
        "writing":     "Flexible drafting across many styles.",
        "study":       "Explains concepts step by step and can quiz you.",
        "data":        "Can analyze files and produce tables and charts.",
        "summarize":   "Fast summaries in the length and format you ask for.",
        "math":        "Clear worked solutions and can run calculations.",
        "translation": "Natural translations that follow the tone you ask for.",
        "brainstorm":  "Produces many varied ideas and refines them with you.",
        "design":      "Creates images from text prompts in many styles.",
        "general":     "Flexible all-rounder for almost any task.",
    },
    "Copilot": {
        "research":   "Web-connected answers with links for quick lookups.",
        "coding":     "Suggestions inside coding tools like VS Code and GitHub.",
        "writing":    "Helps write emails and documents inside Microsoft apps.",
        "data":       "Works inside Excel for formulas and analysis.",
        "brainstorm": "Quick ideas that fit into Microsoft apps like Word and PowerPoint.",
        "design":     "Makes images and slide visuals with Microsoft tools.",
        "general":    "Handy for tasks inside Windows and Microsoft apps.",
    },
    "Claude": {
        "coding":      "Writes and explains clean code, good at long code and debugging.",
        "writing":     "Natural, careful writing tone.",
        "study":       "Patient, clear explanations of difficult ideas.",
        "data":        "Careful reasoning about data and clear explanations of results.",
        "summarize":   "Accurate summaries of long text that keep key details.",
        "math":        "Careful step-by-step reasoning that explains each step.",
        "translation": "Keeps meaning and nuance in careful translations.",
        "brainstorm":  "Thoughtful, original ideas with reasons behind them.",
        "general":     "Careful, clear answers on long or detailed tasks.",
    },
    "DeepSeek": {
        "coding":      "Strong step-by-step reasoning for writing, debugging, and algorithms.",
        "study":       "Patient logical explanations for math, science, and difficult concepts.",
        "math":        "Very strong at math and logical reasoning problems.",
        "translation": "Good with Chinese and English translation.",
        "general":     "Strong reasoning for logic-heavy questions.",
    },
}

models = {
    "Claude": {
        "default":     ["Opus", "Sonnet", "Haiku"],
        "summarize":   ["Sonnet", "Haiku", "Opus"],
        "translation": ["Sonnet", "Haiku", "Opus"],
        "general":     ["Sonnet", "Haiku", "Opus"],
    },
    "Gemini": {
        "default":     ["Pro", "Flash", "Flash-Lite"],
        "summarize":   ["Flash", "Pro", "Flash-Lite"],
        "translation": ["Flash", "Flash-Lite", "Pro"],
        "general":     ["Flash", "Pro", "Flash-Lite"],
    },
    "ChatGPT": {
        "default":     ["Pro", "Thinking", "Instant"],
        "writing":     ["Thinking", "Instant", "Pro"],
        "brainstorm":  ["Thinking", "Instant", "Pro"],
        "summarize":   ["Instant", "Thinking", "Pro"],
        "translation": ["Instant", "Thinking", "Pro"],
        "general":     ["Instant", "Thinking", "Pro"],
    },
    "DeepSeek": {
        "default":     ["V4-Pro", "V4-Flash"],
        "translation": ["V4-Flash", "V4-Pro"],
        "general":     ["V4-Flash", "V4-Pro"],
    },
    "Perplexity": {
        "default":     ["Sonar Deep Research", "Sonar Reasoning Pro", "Sonar Pro", "Sonar"],
        "general":     ["Sonar Pro", "Sonar", "Sonar Reasoning Pro"],
    },
    "Copilot": {
        "default":     ["Think Deeper", "Quick Response"],
        "writing":     ["Quick Response", "Think Deeper"],
        "brainstorm":  ["Quick Response", "Think Deeper"],
        "general":     ["Quick Response", "Think Deeper"],
    },
}

tags = {
    "Opus": "most capable", "Sonnet": "balanced", "Haiku": "fastest",
    "Pro": "most capable", "Flash": "balanced", "Flash-Lite": "fastest",
    "Thinking": "deep reasoning", "Instant": "fastest",
    "V4-Pro": "most capable", "V4-Flash": "fastest",
    "Sonar Deep Research": "most thorough", "Sonar Reasoning Pro": "multi-step reasoning",
    "Sonar Pro": "more depth", "Sonar": "fastest",
    "Think Deeper": "deep reasoning", "Quick Response": "fastest",
}

matched_category = ""

def is_match(word, trigger):
    if word == trigger:
        return True
    if len(trigger) >= 5 and word.startswith(trigger):
        return True
    return False

def models_text(llm, category):
    if category in models[llm]:
        model_list = models[llm][category]
    else:
        model_list = models[llm]["default"]
    parts = []
    for model in model_list:
        parts.append(model + " (" + tags[model] + ")")
    return " > ".join(parts)

ACCENT = "#2563eb"
placeholder_text = "e.g. Explain recursion with examples for my exam"
placeholder_on = True
logo_images = {}
row_widgets = {}

examples = {
    "Research": "Find the latest news and credible sources on electric vehicles in India",
    "Coding": "Help me debug a python function that crashes with an error",
    "Study": "Explain operating system concepts for my exam in simple words",
    "Writing": "Write a formal email to my professor asking for an extension",
    "Data": "Analyze a csv file and make a chart of monthly sales",
}

def make_button(parent, text, command, bg_color="#2563eb", fg_color="#ffffff", size=14):
    button = Label(parent, text=text, font=("Avenir Next", size, "bold"), bg=bg_color, fg=fg_color, padx=24, pady=8, cursor="hand2")
    button.bind("<Button-1>", lambda event: command())
    return button

def get_logo(llm, small):
    key = llm + str(small)
    if key in logo_images:
        return logo_images[key]
    try:
        image = PhotoImage(file="logos/" + llm.lower() + ".png")
        if small:
            image = image.subsample(2, 2)
    except TclError:
        size = 64
        if small:
            size = 32
        image = PhotoImage(width=size, height=size)
    logo_images[key] = image
    return image

def show_placeholder():
    global placeholder_on
    task_text.delete("1.0", END)
    task_text.insert("1.0", placeholder_text)
    task_text.config(fg="#9ca3af")
    placeholder_on = True

def on_focus_in(event):
    global placeholder_on
    if placeholder_on:
        task_text.delete("1.0", END)
        task_text.config(fg="#111827")
        placeholder_on = False

def on_focus_out(event):
    if task_text.get("1.0", END).strip() == "":
        show_placeholder()

def fill_example(text):
    global placeholder_on
    task_text.delete("1.0", END)
    task_text.insert("1.0", text)
    task_text.config(fg="#111827")
    placeholder_on = False
    error_label.config(text="")

def on_enter_key(event):
    find_llms()
    return "break"

def show_input_screen():
    results_screen.pack_forget()
    input_screen.pack(fill=BOTH, expand=True)

def show_results_screen():
    input_screen.pack_forget()
    results_screen.pack(fill=BOTH, expand=True)

def build_rows():
    for child in rows_frame.winfo_children():
        child.destroy()
    row_widgets.clear()

    rank = 1
    for llm in order[matched_category]:
        row = Frame(rows_frame, bg="#ffffff", cursor="hand2")
        row.pack(fill=X, pady=3, padx=10)

        rank_label = Label(row, text=str(rank), font=("Avenir Next", 14, "bold"), fg="#6b7280", bg="#ffffff", width=2)
        rank_label.pack(side=LEFT, padx=(8, 4), pady=8)

        logo_small = Label(row, image=get_logo(llm, True), bg="#ffffff")
        logo_small.pack(side=LEFT, padx=4)

        name_small = Label(row, text=llm, font=("Avenir Next", 14), fg="#1f2937", bg="#ffffff")
        name_small.pack(side=LEFT, padx=8)

        row_widgets[llm] = [row, rank_label, logo_small, name_small]
        for widget in row_widgets[llm]:
            widget.bind("<Button-1>", lambda event, chosen=llm: select_llm(chosen))
        rank = rank + 1

def select_llm(selected_llm):
    for llm in row_widgets:
        row_color = "#ffffff"
        if llm == selected_llm:
            row_color = "#dbeafe"
        for widget in row_widgets[llm]:
            widget.config(bg=row_color)

    logo_label.config(image=get_logo(selected_llm, False))
    name_label.config(text=selected_llm)
    good_for_label.config(text="Good for: " + good_for[selected_llm][matched_category])
    models_label.config(text="Best models: " + models_text(selected_llm, matched_category))

    bullet_text = ""
    for keyword in keywords[matched_category]:
        bullet_text = bullet_text + "\u2022  " + keyword + "\n"
    bullet_text = bullet_text.strip()

    keywords_heading.config(text="Prompt keywords to use")
    keywords_label.config(text=bullet_text)

def find_llms():
    global matched_category

    if placeholder_on:
        task_text_value = ""
    else:
        task_text_value = task_text.get("1.0", END)

    lowercase_text = task_text_value.lower()
    if lowercase_text.strip() == "":
        error_label.config(text="Please describe your task first")
        return
    error_label.config(text="")

    raw_words = lowercase_text.split()
    clean_words = []
    for word in raw_words:
        cleaned_word = word.strip(".,?!;:()\"'")
        clean_words.append(cleaned_word)

    best_category = ""
    highest_count = 0

    for category in triggers:
        count = 0
        trigger_words = triggers[category]
        for word in clean_words:
            for trigger in trigger_words:
                if is_match(word, trigger):
                    count = count + 1
                    break

        if count > highest_count:
            highest_count = count
            best_category = category

    if highest_count == 0:
        matched_category = "general"
        category_badge.config(text="General picks")
        note_label.config(text="No exact match found")
    else:
        matched_category = best_category
        category_badge.config(text="Category: " + matched_category.capitalize())
        note_label.config(text="")

    build_rows()
    select_llm(order[matched_category][0])
    show_results_screen()

window = Tk()
window.title("Prompt Pilot")
window.geometry("1040x640")
window.resizable(False, False)

background_image = PhotoImage(file="background.png")

# ---------- Screen 1: input ----------
input_screen = Frame(window)
input_screen.pack(fill=BOTH, expand=True)

input_bg = Label(input_screen, image=background_image)
input_bg.place(x=0, y=0, relwidth=1, relheight=1)

input_card = Frame(input_screen, bg="#ffffff", highlightbackground="#e5e7eb", highlightthickness=1)
input_card.place(relx=0.5, rely=0.5, anchor="center")

title_label = Label(input_card, text="Prompt Pilot", font=("Avenir Next", 32, "bold"), fg="#111827", bg="#ffffff")
title_label.pack(padx=60, pady=(30, 0))

subtitle_label = Label(input_card, text="Find the best LLM and prompt keywords for your task", font=("Avenir Next", 13), fg="#6b7280", bg="#ffffff")
subtitle_label.pack(pady=(0, 20))

instruction_label = Label(input_card, text="Describe your task in 2-3 lines:", font=("Avenir Next", 13, "bold"), fg="#374151", bg="#ffffff")
instruction_label.pack(anchor="w", padx=60)

task_text = Text(input_card, width=46, height=4, wrap=WORD, font=("Avenir Next", 14), bg="#ffffff", fg="#9ca3af", relief="solid", bd=1, padx=10, pady=8)
task_text.pack(padx=60, pady=(6, 4))
task_text.bind("<FocusIn>", on_focus_in)
task_text.bind("<FocusOut>", on_focus_out)
task_text.bind("<Return>", on_enter_key)

error_label = Label(input_card, text="", font=("Avenir Next", 12, "bold"), fg="#dc2626", bg="#ffffff")
error_label.pack()

chips_heading = Label(input_card, text="Or try an example:", font=("Avenir Next", 12), fg="#6b7280", bg="#ffffff")
chips_heading.pack(pady=(4, 4))

chips_frame = Frame(input_card, bg="#ffffff")
chips_frame.pack()

for chip_name in examples:
    chip = Label(chips_frame, text=chip_name, font=("Avenir Next", 12, "bold"), bg="#eff6ff", fg=ACCENT, padx=12, pady=4, cursor="hand2")
    chip.pack(side=LEFT, padx=4)
    chip.bind("<Button-1>", lambda event, chosen=chip_name: fill_example(examples[chosen]))

find_button = make_button(input_card, "Find LLMs", find_llms)
find_button.pack(pady=(20, 30))

show_placeholder()

# ---------- Screen 2: results ----------
results_screen = Frame(window)

results_bg = Label(results_screen, image=background_image)
results_bg.place(x=0, y=0, relwidth=1, relheight=1)

top_bar = Frame(results_screen, bg="#ffffff", highlightbackground="#e5e7eb", highlightthickness=1)
top_bar.pack(fill=X, padx=30, pady=(20, 10))

back_button = make_button(top_bar, "\u2190  New task", show_input_screen, "#f3f4f6", "#111827", 12)
back_button.pack(side=LEFT, padx=10, pady=10)

category_badge = Label(top_bar, text="", font=("Avenir Next", 13, "bold"), bg=ACCENT, fg="#ffffff", padx=16, pady=6)
category_badge.pack(side=RIGHT, padx=10)

note_label = Label(top_bar, text="", font=("Avenir Next", 12, "bold"), fg="#d97706", bg="#ffffff")
note_label.pack(side=RIGHT, padx=10)

left_frame = Frame(results_screen, bg="#ffffff", width=340, height=500, highlightbackground="#e5e7eb", highlightthickness=1)
left_frame.pack(side=LEFT, anchor="n", padx=(30, 10), pady=(0, 20))
left_frame.pack_propagate(False)

right_frame = Frame(results_screen, bg="#ffffff", width=620, height=500, highlightbackground="#e5e7eb", highlightthickness=1)
right_frame.pack(side=LEFT, anchor="n", padx=(10, 30), pady=(0, 20))
right_frame.pack_propagate(False)

list_heading = Label(left_frame, text="Recommended LLMs", font=("Avenir Next", 15, "bold"), fg="#111827", bg="#ffffff")
list_heading.pack(pady=(16, 6))

rows_frame = Frame(left_frame, bg="#ffffff")
rows_frame.pack(fill=X)

logo_label = Label(right_frame, bg="#ffffff")
logo_label.pack(pady=(16, 2))

name_label = Label(right_frame, text="", font=("Avenir Next", 20, "bold"), fg="#111827", bg="#ffffff")
name_label.pack(pady=2)

good_for_label = Label(right_frame, text="", wraplength=560, justify="center", font=("Avenir Next", 12), fg="#374151", bg="#ffffff")
good_for_label.pack(pady=2)

models_label = Label(right_frame, text="", wraplength=560, justify="center", font=("Avenir Next", 12, "bold"), fg="#059669", bg="#ffffff")
models_label.pack(pady=2)

keywords_heading = Label(right_frame, text="", font=("Avenir Next", 15, "bold"), fg=ACCENT, bg="#ffffff")
keywords_heading.pack(pady=(10, 4))

keywords_label = Label(right_frame, text="", justify="left", anchor="w", font=("Avenir Next", 14, "bold"), fg="#111827", bg="#f9fafb", relief="solid", bd=1, padx=30, pady=8)
keywords_label.pack(pady=2)

window.mainloop()