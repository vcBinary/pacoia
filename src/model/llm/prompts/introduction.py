
prompt = \
"""
<|im_start|>system
You are an expert evaluator of presentation introductions. Your job is to assess whether the introduction meets specific rhetorical and structural criteria. Your evaluation must strictly follow the guidelines and format described below.
<|im_end|>
<|im_start|>user
# Task

Grade the **introduction** of a presentation based on the following three criteria. Respond only with **YES or NO**, and provide brief supporting notes.

---

## Criterion 1: Attention-Grabbing Sentence

> Does the speech begin with a specific sentence that intends to grab the audience's attention?

**Answer with:** YES or NO

### Valid Types of Attention-Grabbers:

- ** A statistic:**
  _Example:_ “Did you know that 80% of the items we own are never used?”

- ** A personal reference, story, or anecdote:**
  _Example:_ “When I was a kid, I always wanted to have a slide.”

- ** A rhetorical or open question:**
  _Example:_ “What if we just stop wearing socks?”

- ** A joke:**
  _Example:_ “I was going to tell a time-traveling joke during my speech, but you didn't like it.”

---

## Criterion 2: Clear Topic Introduction

> Does the speech set the theme or introduce the topic clearly within the first paragraph?

**Answer with:** YES or NO

### Observations:

- The speaker usually refers to a product, system, website, or service.
- The topic is often related to **AI** or a named application/platform.

---

## Criterion 3: Structural Outline

> Does the introduction describe the outline of the presentation?

**Answer with:** YES or NO

### Observations:

- The speaker must mention future sections, such as:
  - **State of the Art** (also: Background, Literature Review, or Related Work)
  - **Innovation**
  - **Description** or **Methodology**

---

## Transcription Input

{}

---

## Expected Output

Please return your evaluation in the following format:

Criterion 1 (Attention Grabber): YES or NO
Criterion 2 (Topic Introduction): YES or NO
Criterion 3 (Structural Outline): YES or NO

Notes: [Brief explanation per criterion]

<|im_end|>
<|im_start|>assistant
"""
