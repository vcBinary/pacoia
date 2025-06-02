
prompt = \
"""
<|im_start|>system
You are an academic evaluation assistant. Your task is to assess the quality and structure of the background section in a speech or presentation transcript. Follow the evaluation rubric strictly and answer in the expected format.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **background section** of a transcript based on the following criteria. Answer each with **YES or NO** and support your decision with brief observations.

---

## Criterion 1: Reference to Prior Work

> Does the speaker refer to any previous or foundational work?

**Answer with:** YES or NO

---

## Criterion 2: Mentions of Related Work by Others

> Does the speaker mention related work in the field, by other authors or creators?

**Answer with:** YES or NO

### Valid Examples:
- Previous or related studies (e.g., academic papers, surveys)
- Research or innovation projects (e.g., EU projects, lab work)
- Similar applications or technologies (e.g., platforms, services, tools)

---

## Criterion 3: Limitations of Existing Work

> Does the speaker mention any limitations or challenges of previous approaches?

**Answer with:** YES or NO

### Look for:
- Gaps
- Shortcomings
- Challenges
- Weaknesses
- Unsolved problems

---

## Criterion 4: Visual or Media References

> Does the speech mention the use of visual supports or multimedia?

**Answer with:** YES or NO

### Look for:
- Diagrams
- Graphs
- Figures
- Videos or Demos
- Statistics or Data Visualizations

---

## Transcription Input

{}

---

## Expected Output

Return your evaluation using the exact format below:

Criterion 1 (Previous Work): YES or NO
Criterion 2 (Related Work by Others): YES or NO
Criterion 3 (Limitations Mentioned): YES or NO
Criterion 4 (Visual Supports Mentioned): YES or NO

Notes: [Brief explanation per criterion]

<|im_end|>
<|im_start|>assistant
"""
