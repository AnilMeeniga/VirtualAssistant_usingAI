from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "MEENIGA ANIL", ln=True, align="C")
        self.set_font("Arial", size=12)
        self.cell(0, 8, "Rajahmundry, Andhra Pradesh", ln=True, align="C")
        self.cell(0, 8, "Phone: +91 7989280782 | Email: anilmeeniga574@gmail.com", ln=True, align="C")
        self.cell(0, 8, "LinkedIn: linkedin.com/in/anil-meeniga-04078b257", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 14)
        self.set_fill_color(200, 200, 200)
        self.cell(0, 8, title, ln=True, fill=True)
        self.ln(4)
        self.set_font("Arial", size=10)
        for line in content.split("\n"):
            self.multi_cell(0, 8, line)
        self.ln(4)

pdf = ResumePDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add sections
pdf.add_section("Career Objective", 
                "Motivated Computer Science student with a strong foundation in software development and data analytics. "
                "Eager to contribute innovative solutions and enhance organizational productivity.")

pdf.add_section("Education",
                "Bachelor of Technology in Computer Science and Engineering\n"
                "B.V.C College of Engineering, Palacharla (JNTUK) | 2021 - 2025 | CGPA: 7.8/10\n\n"
                "Intermediate (MPC)\n"
                "S.G.P Junior College, Darsi (APBIE) | 2019 - 2021 | Percentage: 95%\n\n"
                "Secondary School (Class X)\n"
                "AP Model School & Junior College, Mundlamur (APSSC) | 2018 - 2019 | CGPA: 9.7/10")

pdf.add_section("Technical Skills",
                "- Programming Languages: Python, SQL\n"
                "- Web Technologies: HTML, CSS, JavaScript (Basic)\n"
                "- Concepts: Algorithms, Machine Learning, Problem Solving")

pdf.add_section("Internship Experience",
                "Web Technologies and Soft Skills Intern\n"
                "HQL Edu Tech (Virtual) | May 2023 - June 2023\n"
                "- Gained hands-on experience in HTML, CSS, and JavaScript.\n"
                "- Improved communication and presentation skills.\n\n"
                "Artificial Intelligence and Machine Learning Intern\n"
                "ExcelR (Virtual) | June 2024 - Aug 2024\n"
                "- Developed AI-driven prompts to enhance NLP.\n"
                "- Collaborated on refining chatbot models for improved interactions.")

pdf.add_section("Projects",
                "Virtual Assistant\n"
                "- Developed a voice-activated virtual assistant.\n"
                "- Technologies Used: Python, NLP, Speech Recognition API\n\n"
                "Speech Recognition System\n"
                "- Built a speech-to-text system.\n"
                "- Technologies Used: Python, Speech Recognition Library, Google Speech API")

pdf.add_section("Certifications",
                "- Basics of Python - HackerRank\n"
                "- AI & ML Internship Certificate - ExcelR\n"
                "- Web Technologies and Soft Skills Certificate - HQL Edu Tech")

pdf.add_section("Extracurricular Activities",
                "- Participated in college coding competitions and hackathons.\n"
                "- Active member of the college technical club.")

pdf.add_section("Additional Information",
                "Hobbies: Playing cricket, listening to music, working out.")

# Save the PDF
pdf_file_path = "Anil_Meeniga_Resume.pdf"
pdf.output(pdf_file_path)

print(f"Resume saved as {pdf_file_path}")