from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def clean_report(report):
    report = report.replace("**", "")
    report = report.replace("* ", "• ")
    return report


def create_pdf(patient_data, report):

    filename = "Medical_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER

    story = []

    story.append(
        Paragraph("AI Medical Symptom Checker Report", title)
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(f"<b>Patient Name:</b> {patient_data['name']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Age:</b> {patient_data['age']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Gender:</b> {patient_data['gender']}", styles["BodyText"])
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph("<b>Symptoms</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(patient_data["symptoms"], styles["BodyText"])
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph("<b>AI Medical Report</b>", styles["Heading2"])
    )

    cleaned_report = clean_report(report)

    story.append(
        Paragraph(
            cleaned_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Disclaimer:</b> This report is AI-generated and should not replace professional medical advice.",
            styles["Italic"]
        )
    )

    doc.build(story)

    return filename