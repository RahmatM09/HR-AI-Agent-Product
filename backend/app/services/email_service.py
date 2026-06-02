import smtplib
from email.message import EmailMessage

from app.core.config import settings

def send_email(to_email: str, subject: str, body: str) -> bool:

    if not settings.EMAIL_HOST or not settings.EMAIL_USERNAME or not settings.EMAIL_PASSWORD:
        print("Email settings are missing, Email was not sent.")
        return False
    
    message = EmailMessage()
    message["From"] = settings.EMAIL_FROM or settings.EMAIL_USERNAME
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            if settings.EMAIL_USE_TLS:
                server.starttls()

            server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
            server.send_message(message)

        return True
    except Exception as error:
        print("Email sending failed: {error}")
        return False




def send_shortlist_email(
        applicant_name: str,
        applicant_email: str,
        job_title: str, 
        score: int, 
        reason: str,
) -> bool:
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

""".strip()
    
    return send_email(
        to_email=applicant_email,
        subject=subject,
        body=body
    )


def send_rejection_email(
    applicant_name: str, 
    applicant_email: str,
    job_title: str,
    reason: str,
) -> bool:
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
""".strip()
    
    return send_email(
        to_email=applicant_email,
        subject=subject,
        body=body
    )
