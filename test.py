from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

def get_user_details():
    print("Enter the following details to create your resume:")
    details = {
        "name": input("Full Name: "),
        "email": input("Email: "),
        "phone": input("Phone: "),
        "address": input("Address: "),
        "job_role": input("Job Role You're Applying For: "),
        "summary": input("Summary (a brief introduction about yourself): "),
        "education": input("Education (e.g., Degree, University, Year): "),
        "skills": input("Skills (comma-separated): "),
        "experience": input("Experience (e.g., Job Title, Company, Duration): "),
        "projects": input("Projects (e.g., Project Name, Description): "),
        "hobbies": input("Hobbies and Interests: "),
        "photo_path": input("Path to your photo (e.g., photo.jpg): "),
    }
    return details

def create_resume(details, output_file="resume.pdf"):
    pdf = canvas.Canvas(output_file, pagesize=letter)
    pdf.setTitle("Resume")
    
    width, height = letter
    x_margin = 50
    y_margin = height - 50
    line_height = 20

    # Colors
    header_color = colors.HexColor("#4CAF50")
    subheader_color = colors.HexColor("#2C3E50")
    text_color = colors.black
    divider_color = colors.HexColor("#D3D3D3")
    background_color = colors.HexColor("#F4F4F9")

    # Background
    pdf.setFillColor(background_color)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    # Photo Section
    if details["photo_path"]:
        try:
            photo = ImageReader(details["photo_path"])
            pdf.drawImage(photo, x_margin, y_margin - 120, width=100, height=100, preserveAspectRatio=True, mask="auto")
        except Exception as e:
            print(f"Could not load photo: {e}")

    # Header
    pdf.setFillColor(header_color)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(x_margin + 120, y_margin - 50, details["name"])
    
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin + 120, y_margin - 70, f"Email: {details['email']} | Phone: {details['phone']}")
    pdf.drawString(x_margin + 120, y_margin - 90, f"Address: {details['address']}")

    # Job Role
    pdf.setFont("Helvetica-Bold", 18)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin - 150, f"Applying For: {details['job_role']}")

    # Divider
    pdf.setFillColor(divider_color)
    pdf.rect(x_margin, y_margin - 160, width - 2 * x_margin, 1, stroke=0, fill=1)

    # Summary Section
    y_margin -= 180
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Summary")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin, y_margin - line_height, details["summary"])

    # Education Section
    y_margin -= 60
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Education")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin, y_margin - line_height, details["education"])

    # Skills Section
    y_margin -= 60
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Skills")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    skills_list = details["skills"].split(",")
    for i, skill in enumerate(skills_list):
        pdf.drawString(x_margin + 20, y_margin - (i + 1) * line_height, f"- {skill.strip()}")
    y_margin -= (len(skills_list) + 1) * line_height

    # Experience Section
    y_margin -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Experience")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin, y_margin - line_height, details["experience"])

    # Projects Section
    y_margin -= 60
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Projects")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin, y_margin - line_height, details["projects"])

    # Hobbies Section
    y_margin -= 60
    pdf.setFont("Helvetica-Bold", 14)
    pdf.setFillColor(subheader_color)
    pdf.drawString(x_margin, y_margin, "Hobbies")
    pdf.setFont("Helvetica", 12)
    pdf.setFillColor(text_color)
    pdf.drawString(x_margin, y_margin - line_height, details["hobbies"])

    # Save PDF
    pdf.save()
    print(f"Resume created successfully as {output_file}!")

if __name__ == "__main__":
    user_details = get_user_details()
    create_resume(user_details)
