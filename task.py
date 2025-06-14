from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    
    lines = data.splitlines()
    word_count = len(data.split())
    char_count = len(data)

    return {
        "Line Count": len(lines),
        "Word Count": word_count,
        "Character Count": char_count
    }

def generate_pdf_report(data_analysis, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Automated Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    for key, value in data_analysis.items():
        c.drawString(100, y, f"{key}: {value}")
        y -= 20

    c.save()

# ====== Example usage ======
input_file = "sample.txt"             # Make sure this file exists
output_pdf = "sample_report.pdf"

analysis = analyze_file(input_file)
generate_pdf_report(analysis, output_pdf)

print("PDF report generated successfully.")