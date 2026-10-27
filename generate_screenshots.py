import os
from PIL import Image, ImageDraw, ImageFont

def render_ui(task_text, category, llm_list, selected_index, llm_name, good_for_text, models_text, keywords_list, filename):
    # Window dimensions (2x scale for crisp retina look, resized to 1040x640)
    w, h = 1040, 640
    img = Image.new("RGB", (w, h), "#f3f4f6")
    draw = ImageDraw.Draw(img)

    # Fonts
    font_win_title = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 13)
    font_app_title = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 24)
    font_label = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 13)
    font_entry = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 14)
    font_btn = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 13)
    font_cat = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 13)
    font_listbox = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 13)
    font_llm_title = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 18)
    font_good_for = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 12)
    font_models = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 12)
    font_kw_heading = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 15)
    font_kw_bullet = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 14)

    # 1. macOS Titlebar
    draw.rectangle([0, 0, w, 32], fill="#e5e7eb")
    draw.line([0, 32, w, 32], fill="#d1d5db", width=1)
    
    # Traffic lights
    draw.ellipse([14, 10, 26, 22], fill="#ff5f56", outline="#e0443e")
    draw.ellipse([34, 10, 46, 22], fill="#ffbd2e", outline="#dea123")
    draw.ellipse([54, 10, 66, 22], fill="#27c93f", outline="#1aab29")
    
    # Window Title text
    win_title = "Prompt Pilot"
    bbox = draw.textbbox((0, 0), win_title, font=font_win_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 8), win_title, fill="#4b5563", font=font_win_title)

    # 2. Main Title
    app_title = "Prompt Pilot"
    bbox = draw.textbbox((0, 0), app_title, font=font_app_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 44), app_title, fill="#111827", font=font_app_title)

    # 3. Two-Column Layout Coordinates
    left_x, left_w = 40, 380
    right_x, right_w = 460, 540
    y_start = 88

    # --- LEFT COLUMN ---
    # "Describe your task:"
    draw.text((left_x + 10, y_start), "Describe your task:", fill="#4b5563", font=font_label)

    # Task Entry box
    entry_y = y_start + 24
    entry_h = 36
    draw.rectangle([left_x + 10, entry_y, left_x + left_w - 10, entry_y + entry_h], fill="#ffffff", outline="#111827", width=1)
    # text inside entry
    draw.text((left_x + 18, entry_y + 8), task_text, fill="#111827", font=font_entry)

    # Find LLMs button
    btn_y = entry_y + entry_h + 10
    btn_w, btn_h = 130, 34
    btn_x = left_x + (left_w - btn_w) / 2
    draw.rectangle([btn_x, btn_y, btn_x + btn_w, btn_y + btn_h], fill="#e5e7eb", outline="#9ca3af", width=1)
    bbox = draw.textbbox((0, 0), "Find LLMs", font=font_btn)
    draw.text((btn_x + (btn_w - (bbox[2] - bbox[0])) / 2, btn_y + 7), "Find LLMs", fill="#111827", font=font_btn)

    # Category Label
    cat_y = btn_y + btn_h + 10
    cat_text = f"Category: {category}"
    bbox = draw.textbbox((0, 0), cat_text, font=font_cat)
    draw.text((left_x + (left_w - (bbox[2] - bbox[0])) / 2, cat_y), cat_text, fill="#2563eb", font=font_cat)

    # Listbox
    lb_y = cat_y + 28
    lb_h = 150
    lb_w = left_w - 40
    lb_x = left_x + 20
    draw.rectangle([lb_x, lb_y, lb_x + lb_w, lb_y + lb_h], fill="#ffffff", outline="#1f2937", width=1)

    item_h = 24
    for idx, item in enumerate(llm_list):
        iy = lb_y + 6 + idx * item_h
        if idx == selected_index:
            # Highlight selected row
            draw.rectangle([lb_x + 2, iy - 2, lb_x + lb_w - 2, iy + item_h - 2], fill="#2563eb")
            draw.text((lb_x + 12, iy), item, fill="#ffffff", font=font_listbox)
        else:
            draw.text((lb_x + 12, iy), item, fill="#1f2937", font=font_listbox)

    # Show details button
    dtl_y = lb_y + lb_h + 12
    dtl_w, dtl_h = 140, 34
    dtl_x = left_x + (left_w - dtl_w) / 2
    draw.rectangle([dtl_x, dtl_y, dtl_x + dtl_w, dtl_y + dtl_h], fill="#e5e7eb", outline="#9ca3af", width=1)
    bbox = draw.textbbox((0, 0), "Show details", font=font_btn)
    draw.text((dtl_x + (dtl_w - (bbox[2] - bbox[0])) / 2, dtl_y + 7), "Show details", fill="#111827", font=font_btn)

    # --- RIGHT COLUMN ---
    right_center = right_x + right_w / 2

    # Logo
    logo_path = f"logos/{llm_name.lower()}.png"
    ry = y_start - 6
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path).convert("RGBA")
        logo_img = logo_img.resize((64, 64), Image.Resampling.LANCZOS)
        img.paste(logo_img, (int(right_center - 32), int(ry)), logo_img)
        ry += 70
    else:
        ry += 10

    # LLM Name
    bbox = draw.textbbox((0, 0), llm_name, font=font_llm_title)
    draw.text((right_center - (bbox[2] - bbox[0]) / 2, ry), llm_name, fill="#111827", font=font_llm_title)
    ry += 32

    # Good for label
    gf_prefix = "Good for: "
    full_gf = gf_prefix + good_for_text
    # simple wrap
    words = full_gf.split()
    lines = []
    curr = []
    for w_word in words:
        curr.append(w_word)
        line_str = " ".join(curr)
        bbox = draw.textbbox((0, 0), line_str, font=font_good_for)
        if bbox[2] - bbox[0] > right_w - 40:
            curr.pop()
            lines.append(" ".join(curr))
            curr = [w_word]
    if curr:
        lines.append(" ".join(curr))

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font_good_for)
        draw.text((right_center - (bbox[2] - bbox[0]) / 2, ry), line, fill="#374151", font=font_good_for)
        ry += 18
    ry += 6

    # Best models label
    mod_prefix = "Best models: "
    full_mod = mod_prefix + models_text
    words = full_mod.split()
    lines = []
    curr = []
    for w_word in words:
        curr.append(w_word)
        line_str = " ".join(curr)
        bbox = draw.textbbox((0, 0), line_str, font=font_models)
        if bbox[2] - bbox[0] > right_w - 40:
            curr.pop()
            lines.append(" ".join(curr))
            curr = [w_word]
    if curr:
        lines.append(" ".join(curr))

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font_models)
        draw.text((right_center - (bbox[2] - bbox[0]) / 2, ry), line, fill="#059669", font=font_models)
        ry += 18
    ry += 8

    # Keywords Heading
    kw_head = "Prompt keywords to use"
    bbox = draw.textbbox((0, 0), kw_head, font=font_kw_heading)
    draw.text((right_center - (bbox[2] - bbox[0]) / 2, ry), kw_head, fill="#2563eb", font=font_kw_heading)
    ry += 26

    # Keywords Box
    card_w = 400
    card_x = right_center - card_w / 2
    card_pad_y = 10
    card_h = len(keywords_list) * 22 + card_pad_y * 2

    # White box with clean border
    draw.rectangle([card_x, ry, card_x + card_w, ry + card_h], fill="#ffffff", outline="#111827", width=1)
    
    ky = ry + card_pad_y
    for kw in keywords_list:
        bullet_item = f"•  {kw}"
        draw.text((card_x + 24, ky), bullet_item, fill="#111827", font=font_kw_bullet)
        ky += 22

    img.save(filename)
    print(f"Saved: {filename}")

# Generate 3 screenshots
# Screenshot 1: Coding Task -> Claude
render_ui(
    task_text="I need help to debug my python code and optimize an algorithm",
    category="coding",
    llm_list=["Claude", "DeepSeek", "ChatGPT", "Gemini", "Copilot"],
    selected_index=0,
    llm_name="Claude",
    good_for_text="Writes and explains clean code, good at long code and debugging.",
    models_text="Opus (most capable) > Sonnet (balanced) > Haiku (fastest)",
    keywords_list=[
        "step-by-step",
        "edge cases",
        "time complexity",
        "explain each line",
        "minimal example",
        "add comments",
        "handle errors",
        "optimize it"
    ],
    filename="screenshot_coding_claude.png"
)

# Screenshot 2: Research Task -> Perplexity
render_ui(
    task_text="Find the latest news, sources, and literature on renewable energy",
    category="research",
    llm_list=["Perplexity", "Gemini", "ChatGPT", "Copilot"],
    selected_index=0,
    llm_name="Perplexity",
    good_for_text="Searches the web live and shows sources with links.",
    models_text="Sonar Deep Research (most thorough) > Sonar Reasoning Pro (multi-step reasoning) > Sonar Pro (more depth) > Sonar (fastest)",
    keywords_list=[
        "cite sources",
        "with links",
        "latest as of [date]",
        "compare viewpoints",
        "state limitations",
        "fact-check claims",
        "group by source",
        "separate facts from opinions"
    ],
    filename="screenshot_research_perplexity.png"
)

# Screenshot 3: Study Task -> ChatGPT
render_ui(
    task_text="Explain quantum computing concepts simply for exam revision",
    category="study",
    llm_list=["ChatGPT", "DeepSeek", "Gemini", "Claude"],
    selected_index=0,
    llm_name="ChatGPT",
    good_for_text="Explains concepts step by step and can quiz you.",
    models_text="Pro (most capable) > Thinking (deep reasoning) > Instant (fastest)",
    keywords_list=[
        "ELI5",
        "analogy",
        "quiz me",
        "key takeaways",
        "common mistakes",
        "real-world example",
        "step-by-step",
        "practice questions"
    ],
    filename="screenshot_study_chatgpt.png"
)
