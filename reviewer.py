from transformers import pipeline

# Load model once
reviewer = pipeline("text2text-generation", model="google/flan-t5-base")

def review_code(user_code):

    if not user_code.strip():
        return "⚠️ Please paste some code."

    prompt = f"""
You are a senior software engineer.

Review the following code and provide:
1. Bugs / Issues
2. Improvements
3. Best Practices

Code:
{user_code}

Answer in bullet points.
"""

    try:
        result = reviewer(
            prompt,
            max_new_tokens=200,
            do_sample=False
        )

        output = result[0]["generated_text"]
        cleaned = output.replace(prompt, "").strip()

        return cleaned if cleaned else "⚠️ No response generated."

    except Exception as e:
        return f"❌ Error: {str(e)}"