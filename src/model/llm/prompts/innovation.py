
prompt = \
"""
<|im_start|>system
You are an academic evaluation assistant. Your task is to assess the **Innovation** section of a speech or presentation transcript. Follow the given criteria and answer with YES or NO for each. Provide brief justifications where applicable.
<|im_end|>
<|im_start|>user
# Evaluation Task

Grade the **Innovation section** of the transcript according to the following criterion:

---

## Criterion 1: Innovation and Key Features

> Does the speech mention the **key features** that make the application innovative?

### Look for:
- Mentions of novelty and originality of the service or product.
- Specific innovative aspects that differentiate it from existing solutions.

**Answer with:** YES or NO

---

## Transcription Input

{}

---

## Expected Output Format

Criterion 1 (Innovation and Key Features): YES or NO

Notes: [Brief explanation or example related to the innovation mentioned in the speech]

<|im_end|>
<|im_start|>assistant
"""
