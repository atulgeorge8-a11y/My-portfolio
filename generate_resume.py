import sys
import subprocess
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
except ImportError:
    install("reportlab")
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors

# Generate PDF
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Atul_Thomas_George_Resume.pdf")
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

# Simple layout
c.setFont("Helvetica-Bold", 24)
c.drawString(50, height - 50, "Atul Thomas George")

c.setFont("Helvetica", 12)
c.drawString(50, height - 70, "Electronics and Computer Science (ECS) Engineer")
c.drawString(50, height - 85, "GitHub: github.com/atulgeorge8-a11y")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 120, "SUMMARY")
c.setFont("Helvetica", 10)
c.drawString(50, height - 135, "Passionate ECS Engineer blending software engineering and electronics to build innovative products.")
c.drawString(50, height - 150, "Experienced in modern web applications, microcontrollers, and IoT solutions.")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 180, "SKILLS")
c.setFont("Helvetica", 10)
c.drawString(50, height - 195, "- Frontend: HTML, CSS, JavaScript")
c.drawString(50, height - 210, "- Backend & Core: Java, Python, C, C++")
c.drawString(50, height - 225, "- Hardware & Tools: Microcontrollers, Sensors, IoT, Git, GitHub")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 255, "PROJECTS")
c.setFont("Helvetica-Bold", 11)
c.drawString(50, height - 275, "Student Grievance Redressal System")
c.setFont("Helvetica", 10)
c.drawString(50, height - 290, "A secure, scalable web portal designed to streamline the grievance reporting process for students.")
c.drawString(50, height - 305, "Features a secure login system and an AI-powered chatbot for immediate assistance.")
c.drawString(50, height - 320, "Technologies: HTML, CSS, JavaScript, AI Integration")

c.setFont("Helvetica-Bold", 11)
c.drawString(50, height - 345, "Smart Dustbin")
c.setFont("Helvetica", 10)
c.drawString(50, height - 360, "An innovative electronics project utilizing microcontrollers and sensors for automated waste management.")
c.drawString(50, height - 375, "Automatically opens upon detecting proximity to encourage touch-less hygienic disposal.")
c.drawString(50, height - 390, "Technologies: C, Electronics, Microcontrollers, Sensors")

c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 420, "EDUCATION")
c.setFont("Helvetica", 10)
c.drawString(50, height - 435, "B.Tech in Electronics and Computer Science")
c.drawString(50, height - 450, "[University Name, Year]")

c.save()
print("Resume generated successfully.")
