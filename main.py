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

def clear_details():
    logo_label.config(image="")
    name_label.config(text="")
    good_for_label.config(text="")
    models_label.config(text="")
    keywords_heading.config(text="")
    keywords_label.config(text="", relief="flat", bg="#f3f4f6", padx=0, pady=0)

def find_llms():
    global matched_category

    task_text = task_entry.get()
    lowercase_text = task_text.lower()
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

    llm_listbox.delete(0, END)
    clear_details()

    if highest_count == 0:
        matched_category = "general"
        message_label.config(text="No exact match, showing general picks", fg="#d97706")
    else:
        matched_category = best_category
        message_label.config(text="Category: " + matched_category, fg="#2563eb")

    for llm in order[matched_category]:
        llm_listbox.insert(END, llm)

def show_details():
    selected_indices = llm_listbox.curselection()
    if len(selected_indices) == 0:
        clear_details()
        name_label.config(text="Please select an LLM first", fg="#dc2626")
        return

    selected_index = selected_indices[0]
    selected_llm = llm_listbox.get(selected_index)

    logo_path = "logos/" + selected_llm.lower() + ".png"
    logo_image = PhotoImage(file=logo_path)
    logo_label.config(image=logo_image)
    logo_label.image = logo_image

    name_label.config(text=selected_llm, fg="#111827")
    good_for_label.config(text="Good for: " + good_for[selected_llm][matched_category])
    models_label.config(text="Best models: " + models_text(selected_llm, matched_category))

    bullet_text = ""
    for keyword in keywords[matched_category]:
        bullet_text = bullet_text + "\u2022  " + keyword + "\n"
    bullet_text = bullet_text.strip()

    keywords_heading.config(text="Prompt keywords to use")
    keywords_label.config(text=bullet_text, relief="solid", bg="#ffffff", padx=30, pady=10)

window = Tk()
window.title("Prompt Pilot")
window.geometry("1040x640")
window.configure(bg="#f3f4f6")

title_label = Label(window, text="Prompt Pilot", font=("Avenir Next", 24, "bold"), fg="#111827", bg="#f3f4f6")
title_label.pack(pady=(10, 4))

left_frame = Frame(window, bg="#f3f4f6", width=400, height=520)
left_frame.pack(side=LEFT, anchor="n", padx=(30, 10), pady=10)
left_frame.pack_propagate(False)

right_frame = Frame(window, bg="#f3f4f6", width=560, height=520)
right_frame.pack(side=LEFT, anchor="n", padx=(10, 30), pady=10)
right_frame.pack_propagate(False)

instruction_label = Label(left_frame, text="Describe your task:", font=("Avenir Next", 13), fg="#4b5563", bg="#f3f4f6")
instruction_label.pack(pady=2)

task_entry = Entry(left_frame, width=28, font=("Avenir Next", 14), bg="#ffffff", fg="#111827", relief="solid", bd=1)
task_entry.pack(pady=4)

find_button = Button(left_frame, text="Find LLMs", font=("Avenir Next", 13, "bold"), fg="#111827", cursor="hand2")
find_button.config(command=find_llms)
find_button.pack(pady=4)

message_label = Label(left_frame, text="", font=("Avenir Next", 13, "bold"), fg="#2563eb", bg="#f3f4f6")
message_label.pack(pady=2)

llm_listbox = Listbox(left_frame, height=6, width=24, font=("Avenir Next", 13), bg="#ffffff", fg="#1f2937", selectbackground="#2563eb", selectforeground="#ffffff", relief="solid", bd=1)
llm_listbox.pack(pady=2)

details_button = Button(left_frame, text="Show details", font=("Avenir Next", 13, "bold"), fg="#111827", cursor="hand2")
details_button.config(command=show_details)
details_button.pack(pady=4)

logo_label = Label(right_frame, bg="#f3f4f6")
logo_label.pack(pady=2)

name_label = Label(right_frame, text="", font=("Avenir Next", 18, "bold"), fg="#111827", bg="#f3f4f6")
name_label.pack(pady=2)

good_for_label = Label(right_frame, text="", wraplength=520, justify="center", font=("Avenir Next", 12), fg="#374151", bg="#f3f4f6")
good_for_label.pack(pady=2)

models_label.pack(pady=2)

keywords_heading = Label(right_frame, text="", font=("Avenir Next", 15, "bold"), fg="#2563eb", bg="#f3f4f6")
keywords_heading.pack(pady=(8, 2))

keywords_label = Label(right_frame, text="", justify="left", anchor="w", font=("Avenir Next", 16, "bold"), fg="#111827", bg="#f3f4f6", bd=2, padx=0, pady=0)
keywords_label.pack(pady=2)

window.mainloop()