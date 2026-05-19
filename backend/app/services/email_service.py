


def print_mock_email(to_email: str, subject: str, body: str) -> None:
    print("\n", "=" * 60)
    print("MOCK EMAIL")
    print("=" * 60)
    print("To: ", to_email)
    print("Subject: ", subject)
    print("\nBody: ", body)
    print("=" * 60)


def send_shortlist_email(
        applicant_name: str,
        applicant_email: str,
        job_title: str, 
        score: int, 
        reason: str,
):
    subject = f"Application Update: {job_title}"
    body = f"""
Hello {applicant_name},

Thank you for applying for the {job_title} position.

We are happy to inform you that your application has been shortlisted for recruiter interview.

AI Evaluation Score: {score}/100

Reason:
{reason}

Our recruitment team may contact you for the next steps.

Best regards,
HR Recruitment Team

"""
    print_mock_email(to_email=applicant_email, subject=subject, body=body.strip())


def send_rejection_email(
    applicant_name: str, 
    applicant_email: str,
    job_title: str,
    reason: str,
):
    subject = f"Application Update: {job_title}"
    body = f"""
Hello {applicant_name},

Thank you for applying for the {job_title} position.

After reviewing your application, we are unable to shortlist you for this role at this time.

Reason:
{reason}

We appreciate your interest and encourage you to apply again for future opportunities that match your skills and experience.

Best regards,
HR Recruitment Team
"""
    print_mock_email(to_email=applicant_email, subject=subject, body=body.strip())
