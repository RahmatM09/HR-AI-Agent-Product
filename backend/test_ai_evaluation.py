from app.services.ai_evaluation import evaluate_resume

job_description = """
We are looking for a Graphic Designer to be good in photoshop and illustrator.
The candidate will work with Photoshop, branding.
"""

job_requirements = """
Photoshop, Illustrator, Branding, After Effect, Canva.
"""

resume_text = """
John Doe is a Python backend developer with 3 years of experience.
He has built REST APIs using FastAPI and Flask.
He has worked with SQLAlchemy, PostgreSQL, and authentication systems.
He also has basic Docker experience.
"""

weak_resume_text = """
Jane Smith has 2 years of experience as a graphic designer.
She has worked with Photoshop, Illustrator, branding, and social media content.
She has basic knowledge of HTML and CSS but no backend API development experience.
"""

def print_evaluation_result(result: dict):
    print("\n" + "=" * 60)
    print("AI Response: ")
    print("=" * 60)

    print("Score:", result["score"])
    print("Status:", result["status"])
    print("Reason:", result["reason"])

    print("\nStrengths:")
    for strength in result["strengths"]:
        print("-", strength)

    print("\nWeaknesses:")
    for weakness in result["weaknesses"]:
        print("-", weakness)

    print("\nRecommendation:")
    print(result["recommendation"])


try:

    result = evaluate_resume(job_description=job_description, job_requirements=job_requirements, resume_text=resume_text)

    print_evaluation_result(result)

except Exception as error:
    print("AI evaluation failed.")
    print("Reason: ", error)