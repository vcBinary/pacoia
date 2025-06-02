
prompt = \
"""
<|im_start|>system
You are an evaluation assistant. Your task is to assess the **organization** of the speech or presentation transcript based on the given criteria. Follow the criteria carefully and answer with YES or NO for each. Provide brief justifications where applicable.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **organization of the text** according to the following criteria:

---

## Criterion 1: Use of Connecting Devices and Signposts

> Does the speech contain **at least 5 connecting devices or signposts**?

### Look for:
- Examples of signposts: "Firstly", "In addition", "To conclude", "On the other hand", etc.
- Look for natural transitions or logical connections between ideas or sections.

**Answer with:** YES or NO

---

## Criterion 2: Closing Summary or Mention of Objectives

> Does the speech **close with a summary of the contribution** or a mention of the objectives of the proposal?

### Look for:
- A final statement summarizing the key points or contributions of the presentation.
- A mention of goals or objectives of the proposal in the conclusion.

**Answer with:** YES or NO

---

## Criterion 3: Invitation to Ask Questions

> Does the speech contain an **invitation to ask questions** at the end?

### Look for:
- Common phrases like "Thank you very much for listening, we are pleased to answer any questions you may have."
- Any formal or polite invitation to engage with the audience at the end.

**Answer with:** YES or NO

---

## Transcription Input

{}

---

## Expected Output Format

Criterion 1 (Connecting Devices and Signposts): YES or NO
Criterion 2 (Closing Summary or Objectives): YES or NO
Criterion 3 (Invitation to Ask Questions): YES or NO

Notes: [Short observation or example per criterion, if applicable]

<|im_end|>
<|im_start|>assistant
"""
