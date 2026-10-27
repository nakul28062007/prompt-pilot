import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Definitions
    COLOR_BG_DARK     = RGBColor(15, 23, 42)     # #0f172a (Deep Slate/Navy)
    COLOR_CARD_DARK   = RGBColor(30, 41, 59)     # #1e293b
    COLOR_BG_LIGHT    = RGBColor(248, 250, 252)  # #f8fafc (Off-white/Gray 50)
    COLOR_CARD_LIGHT  = RGBColor(255, 255, 255)  # #ffffff
    COLOR_BORDER_LIGHT= RGBColor(226, 232, 240)  # #e2e8f0
    COLOR_PRIMARY     = RGBColor(37, 99, 235)    # #2563eb (Royal Blue)
    COLOR_PRIMARY_DARK= RGBColor(29, 78, 216)    # #1d4ed8
    COLOR_SECONDARY   = RGBColor(5, 150, 105)    # #059669 (Emerald)
    COLOR_TEXT_DARK   = RGBColor(15, 23, 42)     # #0f172a
    COLOR_TEXT_MUTED  = RGBColor(100, 116, 139)  # #64748b
    COLOR_TEXT_WHITE  = RGBColor(255, 255, 255)  # #ffffff
    COLOR_ACCENT_BLUE = RGBColor(219, 234, 254)  # #dbeafe (Light Blue fill)
    COLOR_ACCENT_EMERALD = RGBColor(209, 250, 229) # #d1fae5

    FONT_FAMILY = "Arial"

    # Helper: Set slide background color
    def set_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    # Helper: Add header banner
    def add_header(slide, title_text, category_text="PROMPT PILOT"):
        # Category / Tracker tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category_text.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(11)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_PRIMARY

        # Slide Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT_DARK

        # Thin divider line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = COLOR_BORDER_LIGHT
        line.line.fill.background()

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Dark Luxury Theme)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_background(s1, COLOR_BG_DARK)

    # Accent decorative glow/shape
    accent_bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(0.2), Inches(3.2))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = COLOR_PRIMARY
    accent_bar.line.fill.background()

    # Title & Subtitle box
    tbox = s1.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11.0), Inches(2.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p_badge = tf1.paragraphs[0]
    p_badge.text = "PYTHON TKINTER DESKTOP APPLICATION"
    p_badge.font.name = FONT_FAMILY
    p_badge.font.size = Pt(12)
    p_badge.font.bold = True
    p_badge.font.color.rgb = RGBColor(96, 165, 250) # Light blue

    p_main = tf1.add_paragraph()
    p_main.text = "Prompt Pilot"
    p_main.font.name = FONT_FAMILY
    p_main.font.size = Pt(46)
    p_main.font.bold = True
    p_main.font.color.rgb = COLOR_TEXT_WHITE
    p_main.space_after = Pt(10)

    p_sub = tf1.add_paragraph()
    p_sub.text = "Intelligent Multi-LLM Intent Recommendation & Prompt Engineering System"
    p_sub.font.name = FONT_FAMILY
    p_sub.font.size = Pt(18)
    p_sub.font.color.rgb = RGBColor(203, 213, 225) # Slate 300

    # Project metadata card
    meta_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(3.8), Inches(10.9), Inches(2.8))
    meta_card.fill.solid()
    meta_card.fill.fore_color.rgb = COLOR_CARD_DARK
    meta_card.line.color.rgb = RGBColor(51, 65, 85)
    meta_card.line.width = Pt(1)

    # Team Members Header inside card
    mb_head = s1.shapes.add_textbox(Inches(1.5), Inches(4.0), Inches(10.3), Inches(0.4))
    tf_mb = mb_head.text_frame
    p_mh = tf_mb.paragraphs[0]
    p_mh.text = "PROJECT TEAM MEMBERS"
    p_mh.font.name = FONT_FAMILY
    p_mh.font.size = Pt(11)
    p_mh.font.bold = True
    p_mh.font.color.rgb = RGBColor(148, 163, 184)

    # 3 Member Cards
    members = [
        ("Nakulvasudev T", "RA2511031010028", "Lead Software Architect & GUI Engineering"),
        ("SriMithru", "RA2511031010040", "Data Engineering & Domain Knowledge Curation"),
        ("Mukesh", "RA2511031010038", "Model Intelligence Research, QA & Documentation")
    ]

    col_w = Inches(3.2)
    gap = Inches(0.35)
    start_x = Inches(1.5)

    for i, (name, reg, role) in enumerate(members):
        mx = start_x + i * (col_w + gap)
        mcard = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, mx, Inches(4.5), col_w, Inches(1.8))
        mcard.fill.solid()
        mcard.fill.fore_color.rgb = RGBColor(15, 23, 42)
        mcard.line.color.rgb = RGBColor(59, 130, 246)
        mcard.line.width = Pt(1)

        mbox = s1.shapes.add_textbox(mx + Inches(0.15), Inches(4.6), col_w - Inches(0.3), Inches(1.6))
        mtf = mbox.text_frame
        mtf.word_wrap = True

        p1 = mtf.paragraphs[0]
        p1.text = name
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_TEXT_WHITE

        p2 = mtf.add_paragraph()
        p2.text = f"Reg No: {reg}"
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(12)
        p2.font.color.rgb = RGBColor(96, 165, 250)
        p2.space_after = Pt(4)

        p3 = mtf.add_paragraph()
        p3.text = role
        p3.font.name = FONT_FAMILY
        p3.font.size = Pt(11)
        p3.font.color.rgb = RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 2: INTRODUCTION TO THE PROJECT
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_background(s2, COLOR_BG_LIGHT)
    add_header(s2, "Introduction & Project Motivation", "PROJECT BACKGROUND")

    # Left Column: Problem & Context (Card)
    card_prob = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.2))
    card_prob.fill.solid()
    card_prob.fill.fore_color.rgb = COLOR_CARD_LIGHT
    card_prob.line.color.rgb = COLOR_BORDER_LIGHT
    card_prob.line.width = Pt(1)

    pb_box = s2.shapes.add_textbox(Inches(1.1), Inches(1.9), Inches(5.0), Inches(4.8))
    ptf = pb_box.text_frame
    ptf.word_wrap = True

    p = ptf.paragraphs[0]
    p.text = "The Modern AI Challenge"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(12)

    bullet_points_left = [
        ("The Multi-LLM Landscape", "Users now navigate ChatGPT, Claude, Gemini, DeepSeek, Perplexity, and Copilot—each with divergent architectures and specialized strengths."),
        ("The 'Model Fatigue' Dilemma", "Selecting the wrong model leads to subpar outputs (e.g., using a general chatbot for live web research or deep algorithmic debugging)."),
        ("The Prompt Engineering Barrier", "Most users write vague queries without domain-specific constraints (e.g., missing 'time complexity' for code or 'cite sources' for research)."),
        ("Lack of Model Tier Awareness", "Providers offer complex tier structures (Opus vs Sonnet, Pro vs Flash, Thinking vs Instant) without clear speed vs capability clarity.")
    ]

    for title, desc in bullet_points_left:
        p_t = ptf.add_paragraph()
        p_t.text = f"•  {title}:"
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_DARK

        p_d = ptf.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(8)

    # Right Column: The Solution (Card)
    card_sol = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.7), Inches(5.7), Inches(5.2))
    card_sol.fill.solid()
    card_sol.fill.fore_color.rgb = COLOR_CARD_LIGHT
    card_sol.line.color.rgb = COLOR_BORDER_LIGHT
    card_sol.line.width = Pt(1)

    sb_box = s2.shapes.add_textbox(Inches(7.1), Inches(1.9), Inches(5.1), Inches(4.8))
    stf = sb_box.text_frame
    stf.word_wrap = True

    p = stf.paragraphs[0]
    p.text = "The Prompt Pilot Solution"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.space_after = Pt(12)

    features = [
        ("Automated Intent Recognition", "Parses natural language task descriptions using a heuristic NLP engine matching 300+ trigger keywords across 10 specialized domains."),
        ("Deterministic Priority Ranking", "Ranks top LLMs in strict priority order for the detected task domain, complete with contextual rationale ('Good for...')."),
        ("Granular Model Tier Breakdown", "Exposes concrete sub-model hierarchies (e.g. Claude Opus > Sonnet > Haiku) tagged by capability: fastest, balanced, or deep reasoning."),
        ("Curated Prompt Keywords", "Generates instant copy-ready prompt engineering keywords to enforce structural constraints, formatting, and edge-case handling."),
        ("Zero Overhead Desktop App", "Built in pure Python with Tkinter—launches instantly with zero accounts, no subscription keys, and 100% offline recommendation logic.")
    ]

    for title, desc in features:
        p_t = stf.add_paragraph()
        p_t.text = f"✔  {title}:"
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT_DARK

        p_d = stf.add_paragraph()
        p_d.text = f"   {desc}"
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = COLOR_TEXT_MUTED
        p_d.space_after = Pt(6)

    # ==========================================
    # SLIDE 3: PROPOSED VS EXISTING
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_background(s3, COLOR_BG_LIGHT)
    add_header(s3, "Comparative Analysis: Proposed vs. Existing System", "SYSTEM COMPARISON")

    # Table of Comparison
    rows = 5
    cols = 3
    tbl_shape = s3.shapes.add_table(rows, cols, Inches(0.8), Inches(1.7), Inches(11.733), Inches(5.1))
    tbl = tbl_shape.table

    # Column widths
    tbl.columns[0].width = Inches(2.5)
    tbl.columns[1].width = Inches(4.5)
    tbl.columns[2].width = Inches(4.733)

    # Headers
    headers = ["Evaluation Metric", "Traditional / Existing Workflow", "Proposed System: Prompt Pilot"]
    for c_idx, h_text in enumerate(headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY if c_idx == 2 else (COLOR_CARD_DARK if c_idx == 0 else RGBColor(71, 85, 105))
        tf = cell.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.12)
        tf.margin_bottom = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = h_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT

    comparison_data = [
        (
            "Task & Model Discovery",
            "Manual guesswork. Users cycle through multiple browser tabs (ChatGPT, Claude, Gemini) trial-and-erroring queries without knowing model specialties.",
            "Instant Automated Recommendation. User enters 1 sentence; Prompt Pilot identifies task category and returns prioritized LLMs in 0 milliseconds."
        ),
        (
            "Model Tier Transparency",
            "Opaque and confusing naming schemes (e.g. Sonnet, Haiku, Flash, Thinking, Sonar) with no guidance on latency vs intelligence trade-offs.",
            "Granular Model Hierarchy. Lists exact models ranked by tier with explicit capability tags: fastest, balanced, deep reasoning, or most capable."
        ),
        (
            "Prompt Formulation Quality",
            "Unstructured prompts resulting in hallucinations, missing details, verbose fluff, and lack of technical constraints.",
            "Contextual Keyword Suggestions. Supplies curated domain-specific keywords (e.g. 'edge cases', 'cite sources with links', 'ELI5', 'table format')."
        ),
        (
            "Operational Overhead",
            "High context-switching penalty. Requires multiple active logins, heavy web pages, API rate-limits, and subscription fragmentation.",
            "Lightweight Local Desktop Tool. Zero logins, zero API tokens, runs on pure Python standard library, instant response with clean visual feedback."
        )
    ]

    for r_idx, (metric, existing, proposed) in enumerate(comparison_data, start=1):
        # Metric cell
        c0 = tbl.cell(r_idx, 0)
        c0.fill.solid()
        c0.fill.fore_color.rgb = RGBColor(241, 245, 249)
        tf0 = c0.text_frame
        tf0.word_wrap = True
        tf0.margin_top = Inches(0.1)
        p0 = tf0.paragraphs[0]
        p0.text = metric
        p0.font.name = FONT_FAMILY
        p0.font.size = Pt(13)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_TEXT_DARK

        # Existing cell
        c1 = tbl.cell(r_idx, 1)
        c1.fill.solid()
        c1.fill.fore_color.rgb = COLOR_CARD_LIGHT
        tf1 = c1.text_frame
        tf1.word_wrap = True
        tf1.margin_top = Inches(0.1)
        p1 = tf1.paragraphs[0]
        p1.text = existing
        p1.font.name = FONT_FAMILY
        p1.font.size = Pt(12)
        p1.font.color.rgb = RGBColor(71, 85, 105)

        # Proposed cell
        c2 = tbl.cell(r_idx, 2)
        c2.fill.solid()
        c2.fill.fore_color.rgb = COLOR_ACCENT_BLUE
        tf2 = c2.text_frame
        tf2.word_wrap = True
        tf2.margin_top = Inches(0.1)
        p2 = tf2.paragraphs[0]
        p2.text = proposed
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(12)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_PRIMARY_DARK

    # ==========================================
    # SLIDE 4: TEAM CONTRIBUTION (80% MARKS SLIDE)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_background(s4, COLOR_BG_LIGHT)
    add_header(s4, "Individual Technical Contributions & Architecture", "TEAM ASSIGNMENTS & RESPONSIBILITIES")

    # Important note banner at the top
    note_banner = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.4))
    note_banner.fill.solid()
    note_banner.fill.fore_color.rgb = RGBColor(254, 242, 242)
    note_banner.line.color.rgb = RGBColor(252, 165, 165)
    note_banner.line.width = Pt(1)
    tf_nb = note_banner.text_frame
    p_nb = tf_nb.paragraphs[0]
    p_nb.text = "★ Evaluation Criterion: Rigorous technical work breakdown. Individual modules, algorithmic development, and verified deliverables."
    p_nb.font.name = FONT_FAMILY
    p_nb.font.size = Pt(11)
    p_nb.font.bold = True
    p_nb.font.color.rgb = RGBColor(185, 28, 28)

    # 3 Distinct Columns for 3 Members
    col_w = Inches(3.7)
    gap = Inches(0.316)
    c_y = Inches(2.05)
    c_h = Inches(5.0)

    contrib_data = [
        (
            "Nakulvasudev T",
            "RA2511031010028",
            "Lead Software Architect & GUI Engineering",
            COLOR_PRIMARY,
            [
                ("Desktop GUI Architecture", "Architected and implemented the Tkinter desktop GUI, structuring the two-column master-detail layout, layout geometry, responsive packing, and PhotoImage logo caching."),
                ("NLP Tokenizer & String Cleaning", "Engineered the text sanitization pipeline (`lower()`, punctuation stripping `.,?!;:()'\"`, and tokenization) to extract clean search tokens from user inputs."),
                ("Matching & Greedy Scoring Logic", "Implemented `find_llms()` and `is_match()` algorithms: evaluates trigger occurrences across 10 categories, handles greedy tie-breaking, and triggers fallback picks."),
                ("Dynamic Tier & Detail Resolver", "Constructed `show_details()` and `models_text()` to dynamically bind model hierarchies, format bullet lists, and manage selection states with error handling.")
            ]
        ),
        (
            "SriMithru",
            "RA2511031010040",
            "Data Engineering & Knowledge Base Curation",
            COLOR_SECONDARY,
            [
                ("Domain Vocabulary Dataset", "Researched and curated 300+ categorized trigger words spanning Coding, Research, Writing, Study, Data, Math, Translation, Brainstorming, Design, and General."),
                ("Empirical Model Benchmarking", "Conducted comparative performance benchmarks across LLMs to establish deterministic priority ranking orders (`order` dictionary) for each domain."),
                ("Contextual Rationale Synthesis", "Formulated detailed domain capability explanations (`good_for` dictionary) articulating why specific models outperform competitors for each task."),
                ("Prompt Engineering Keywords", "Researched and compiled specialized prompt constraint keywords (`keywords` dictionary) optimized for output quality, precision, and edge-case prevention.")
            ]
        ),
        (
            "Mukesh",
            "RA2511031010038",
            "Model Intelligence Research & Quality Assurance",
            RGBColor(124, 58, 237), # Violet
            [
                ("LLM Tier Hierarchy Mapping", "Investigated contemporary model families across providers to build the granular sub-model catalog (`models` dictionary) covering Opus/Sonnet, Pro/Flash, and Sonar."),
                ("Performance Tagging System", "Designed and mapped the capability tagging ontology (`tags` dictionary) categorizing model tiers into 'fastest', 'balanced', 'deep reasoning', and 'most capable'."),
                ("Test Suite & Edge-Case QA", "Authored comprehensive test suites: verified zero-match general fallbacks, empty inputs, non-selection validation, punctuation stripping, and prefix matches."),
                ("Technical Documentation Deliverables", "Created architectural data-flow diagrams, system specifications, and coordinated evaluation deliverables for academic defense.")
            ]
        )
    ]

    for i, (name, reg, role, accent_col, points) in enumerate(contrib_data):
        cx = Inches(0.8) + i * (col_w + gap)
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, c_y, col_w, c_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_LIGHT
        card.line.color.rgb = accent_col
        card.line.width = Pt(1.5)

        tb = s4.shapes.add_textbox(cx + Inches(0.15), c_y + Inches(0.12), col_w - Inches(0.3), c_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True

        p_name = tf.paragraphs[0]
        p_name.text = name
        p_name.font.name = FONT_FAMILY
        p_name.font.size = Pt(16)
        p_name.font.bold = True
        p_name.font.color.rgb = COLOR_TEXT_DARK

        p_reg = tf.add_paragraph()
        p_reg.text = f"Reg No: {reg}"
        p_reg.font.name = FONT_FAMILY
        p_reg.font.size = Pt(12)
        p_reg.font.bold = True
        p_reg.font.color.rgb = accent_col

        p_role = tf.add_paragraph()
        p_role.text = role
        p_role.font.name = FONT_FAMILY
        p_role.font.size = Pt(11)
        p_role.font.color.rgb = COLOR_TEXT_MUTED
        p_role.space_after = Pt(10)

        for p_title, p_desc in points:
            pt = tf.add_paragraph()
            pt.text = f"▶  {p_title}"
            pt.font.name = FONT_FAMILY
            pt.font.size = Pt(11)
            pt.font.bold = True
            pt.font.color.rgb = COLOR_TEXT_DARK

            pd = tf.add_paragraph()
            pd.text = p_desc
            pd.font.name = FONT_FAMILY
            pd.font.size = Pt(10)
            pd.font.color.rgb = RGBColor(71, 85, 105)
            pd.space_after = Pt(6)

    # ==========================================
    # SLIDE 5: SCREENSHOT 1 — CODING WORKFLOW
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_background(s5, COLOR_BG_LIGHT)
    add_header(s5, "Software Demonstration: Coding & Algorithm Optimization", "APPLICATION WALKTHROUGH — USE CASE 1")

    # Add Screenshot image on the left
    img_path1 = "screenshot_coding_claude.png"
    if os.path.exists(img_path1):
        s5.shapes.add_picture(img_path1, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.15))

    # Right side: Analytical Explanations Card
    c_side1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(1.7), Inches(4.033), Inches(5.15))
    c_side1.fill.solid()
    c_side1.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c_side1.line.color.rgb = COLOR_BORDER_LIGHT
    c_side1.line.width = Pt(1)

    s1_box = s5.shapes.add_textbox(Inches(8.7), Inches(1.9), Inches(3.633), Inches(4.7))
    stf1 = s1_box.text_frame
    stf1.word_wrap = True

    p = stf1.paragraphs[0]
    p.text = "Workflow Breakdown"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(10)

    steps1 = [
        ("Input Prompt", "\"I need help to debug my python code and optimize an algorithm\""),
        ("Intent Classification", "The tokenizer strips punctuation and matches trigger words 'debug', 'python', 'code', 'algorithm'. Categorized as 'coding'."),
        ("Ranked LLM Recommendation", "Claude is identified as the #1 coding model, followed by DeepSeek, ChatGPT, Gemini, and Copilot in deterministic priority order."),
        ("Model Tier Guidance", "Prescribes Claude 3.5/3.7 tier hierarchy: Opus (most capable), Sonnet (balanced), Haiku (fastest)."),
        ("Actionable Prompt Keywords", "Recommends essential coding prompt constraints: 'step-by-step', 'edge cases', 'time complexity', 'explain each line'.")
    ]

    for title, desc in steps1:
        pt = stf1.add_paragraph()
        pt.text = f"•  {title}:"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK

        pd = stf1.add_paragraph()
        pd.text = f"   {desc}"
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(6)

    # ==========================================
    # SLIDE 6: SCREENSHOT 2 — RESEARCH WORKFLOW
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_background(s6, COLOR_BG_LIGHT)
    add_header(s6, "Software Demonstration: Academic & Web Research", "APPLICATION WALKTHROUGH — USE CASE 2")

    # Add Screenshot image on the left
    img_path2 = "screenshot_research_perplexity.png"
    if os.path.exists(img_path2):
        s6.shapes.add_picture(img_path2, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.15))

    # Right side: Analytical Explanations Card
    c_side2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(1.7), Inches(4.033), Inches(5.15))
    c_side2.fill.solid()
    c_side2.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c_side2.line.color.rgb = COLOR_BORDER_LIGHT
    c_side2.line.width = Pt(1)

    s2_box = s6.shapes.add_textbox(Inches(8.7), Inches(1.9), Inches(3.633), Inches(4.7))
    stf2 = s2_box.text_frame
    stf2.word_wrap = True

    p = stf2.paragraphs[0]
    p.text = "Research Intelligence"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.space_after = Pt(10)

    steps2 = [
        ("Input Prompt", "\"Find the latest news, sources, and literature on renewable energy\""),
        ("Intent Classification", "Matches trigger words 'latest', 'news', 'sources', 'literature'. Classified cleanly into 'research' category."),
        ("Ranked LLM Recommendation", "Perplexity is recommended as #1 pick due to real-time search indexing and source attribution, followed by Gemini and ChatGPT."),
        ("Sub-Model Specialization", "Details Perplexity Sonar options: Sonar Deep Research (thorough synthesis) down to Sonar (rapid lookup)."),
        ("Prompt Engineering Anchors", "Guides the user to attach key phrases: 'cite sources', 'with links', 'latest as of [date]', 'separate facts from opinions'.")
    ]

    for title, desc in steps2:
        pt = stf2.add_paragraph()
        pt.text = f"•  {title}:"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK

        pd = stf2.add_paragraph()
        pd.text = f"   {desc}"
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(6)

    # ==========================================
    # SLIDE 7: SCREENSHOT 3 — STUDY & EDUCATION
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_background(s7, COLOR_BG_LIGHT)
    add_header(s7, "Software Demonstration: Conceptual Study & Exam Revision", "APPLICATION WALKTHROUGH — USE CASE 3")

    # Add Screenshot image on the left
    img_path3 = "screenshot_study_chatgpt.png"
    if os.path.exists(img_path3):
        s7.shapes.add_picture(img_path3, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.15))

    # Right side: Analytical Explanations Card
    c_side3 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(1.7), Inches(4.033), Inches(5.15))
    c_side3.fill.solid()
    c_side3.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c_side3.line.color.rgb = COLOR_BORDER_LIGHT
    c_side3.line.width = Pt(1)

    s3_box = s7.shapes.add_textbox(Inches(8.7), Inches(1.9), Inches(3.633), Inches(4.7))
    stf3 = s3_box.text_frame
    stf3.word_wrap = True

    p = stf3.paragraphs[0]
    p.text = "Educational Workflow"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = RGBColor(124, 58, 237)
    p.space_after = Pt(10)

    steps3 = [
        ("Input Prompt", "\"Explain quantum computing concepts simply for exam revision\""),
        ("Intent Classification", "Matches 'explain', 'concept', 'exam', 'revision' — successfully routes to the 'study' learning domain."),
        ("Ranked LLM Recommendation", "ChatGPT is prioritized as #1 for pedagogical step-by-step breakdowns, followed by DeepSeek, Gemini, and Claude."),
        ("Tier Adaptation", "Shows ChatGPT reasoning paths: Pro (most capable), Thinking (deep mathematical reasoning), Instant (quick answers)."),
        ("Pedagogical Keywords", "Injects proven study prompt anchors: 'ELI5' (Explain Like I'm 5), 'analogy', 'quiz me', 'common mistakes', 'practice questions'.")
    ]

    for title, desc in steps3:
        pt = stf3.add_paragraph()
        pt.text = f"•  {title}:"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK

        pd = stf3.add_paragraph()
        pd.text = f"   {desc}"
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(11)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(6)

    # ==========================================
    # SLIDE 8: SYSTEM ARCHITECTURE & CONCLUSION
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_background(s8, COLOR_BG_LIGHT)
    add_header(s8, "System Architecture, Testing & Conclusion", "TECHNICAL SUMMARY & ROADMAP")

    # 3 Summary Cards
    col_w8 = Inches(3.7)
    gap8 = Inches(0.316)
    y8 = Inches(1.7)
    h8 = Inches(5.15)

    # Card 1: Architectural Pipeline
    c1 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y8, col_w8, h8)
    c1.fill.solid()
    c1.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c1.line.color.rgb = COLOR_BORDER_LIGHT
    c1.line.width = Pt(1)

    t1 = s8.shapes.add_textbox(Inches(0.95), y8 + Inches(0.15), col_w8 - Inches(0.3), h8 - Inches(0.3))
    tf1 = t1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "1. Technical Pipeline"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.space_after = Pt(8)

    pipe_steps = [
        ("Input Stage", "TaskEntry widget captures user input via Tkinter `.get()` method."),
        ("Sanitization", "Punctuation stripping (`.,?!;:()\"'`), lowercasing, and word tokenization."),
        ("Heuristic Scoring", "Iterates through 10-domain trigger sets; counts frequency matches per domain."),
        ("Priority Resolution", "Determines top category; fetches model priority list from `order` dictionary."),
        ("Dynamic GUI Rendering", "Loads PNG logo, formats tier hierarchy via `models_text()`, and renders bulleted prompt keywords.")
    ]
    for s_title, s_desc in pipe_steps:
        pt = tf1.add_paragraph()
        pt.text = f"▶ {s_title}"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK
        pd = tf1.add_paragraph()
        pd.text = s_desc
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(10)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(4)

    # Card 2: QA & Verification
    c2 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + col_w8 + gap8, y8, col_w8, h8)
    c2.fill.solid()
    c2.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c2.line.color.rgb = COLOR_BORDER_LIGHT
    c2.line.width = Pt(1)

    t2 = s8.shapes.add_textbox(Inches(0.95) + col_w8 + gap8, y8 + Inches(0.15), col_w8 - Inches(0.3), h8 - Inches(0.3))
    tf2 = t2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "2. Verification & Testing"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.space_after = Pt(8)

    test_points = [
        ("Standard Inputs", "Tested 10+ standard prompts (coding, research, translation, data, math) verifying exact category outputs."),
        ("Edge Case Fallback", "Tested unrecognized prompts ('hello'); successfully triggers fallback to 'general' model ranking."),
        ("Selection Validation", "Clicking 'Show details' without an item selected alerts user in red without crashing."),
        ("Prefix Matching", "Implemented `is_match()` to match words of 5+ letters (e.g. 'summarizing' matches 'summarize')."),
        ("Cross-Platform Layout", "Verified zero-crop responsive window sizing across macOS screen bounds.")
    ]
    for s_title, s_desc in test_points:
        pt = tf2.add_paragraph()
        pt.text = f"✔ {s_title}"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK
        pd = tf2.add_paragraph()
        pd.text = s_desc
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(10)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(4)

    # Card 3: Future Scope & Conclusion
    c3 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8) + (col_w8 + gap8) * 2, y8, col_w8, h8)
    c3.fill.solid()
    c3.fill.fore_color.rgb = COLOR_CARD_LIGHT
    c3.line.color.rgb = COLOR_BORDER_LIGHT
    c3.line.width = Pt(1)

    t3 = s8.shapes.add_textbox(Inches(0.95) + (col_w8 + gap8) * 2, y8 + Inches(0.15), col_w8 - Inches(0.3), h8 - Inches(0.3))
    tf3 = t3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "3. Conclusion & Roadmap"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(124, 58, 237)
    p.space_after = Pt(8)

    future_points = [
        ("Educational Outcome", "Successfully developed an end-to-end Python desktop application showcasing algorithmic text analysis and Tkinter GUI design."),
        ("1-Click Prompt Copy", "Roadmap: Add a 'Copy Formatted Prompt' button to instantly copy the prompt with keywords to system clipboard."),
        ("Local LLM Support", "Roadmap: Integration with local open-weights engines (Ollama, Llama 3) for private offline inference."),
        ("Theme Customization", "Roadmap: System dark-mode switch and custom user trigger keyword addition."),
        ("Project Status", "Fully functioning, documented, and ready for academic presentation & viva.")
    ]
    for s_title, s_desc in future_points:
        pt = tf3.add_paragraph()
        pt.text = f"★ {s_title}"
        pt.font.name = FONT_FAMILY
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_TEXT_DARK
        pd = tf3.add_paragraph()
        pd.text = s_desc
        pd.font.name = FONT_FAMILY
        pd.font.size = Pt(10)
        pd.font.color.rgb = COLOR_TEXT_MUTED
        pd.space_after = Pt(4)

    output_filename = "Prompt_Pilot_Presentation.pptx"
    prs.save(output_filename)
    print(f"Presentation saved successfully as '{output_filename}' ({len(prs.slides)} slides)!")

if __name__ == "__main__":
    build_presentation()
