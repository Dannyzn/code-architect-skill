#!/usr/bin/env python3
"""
Generate PDF using ReportLab (pure Python, no external dependencies).
Fallback when pandoc is not available.
"""

import sys
import json
from pathlib import Path

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False

def generate_pdf_reportlab(repo_info, output_path):
    """Generate PDF using ReportLab."""
    if not REPORTLAB_AVAILABLE:
        print("Error: reportlab not installed. Install with: pip install reportlab")
        return None
    
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkblue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    story.append(Paragraph(f"{repo_info['name']} - Learning Guide", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Project Overview
    story.append(Paragraph("Project Overview", styles['Heading2']))
    story.append(Paragraph(f"<b>Purpose:</b> {repo_info.get('purpose', 'N/A')}", styles['Normal']))
    story.append(Paragraph(f"<b>Tech Stack:</b> {repo_info.get('tech_stack', 'N/A')}", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Architecture
    story.append(Paragraph("Architecture", styles['Heading2']))
    arch_text = repo_info.get('architecture', 'Architecture details...').replace('\n', '<br/>')
    story.append(Paragraph(arch_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Core Components
    story.append(Paragraph("Core Components", styles['Heading2']))
    comp_text = repo_info.get('components', 'Component details...').replace('\n', '<br/>')
    story.append(Paragraph(comp_text, styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(story)
    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: generate_pdf_simple.py <repo_info.json> [output.pdf]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else "learning_guide.pdf"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        repo_info = json.load(f)
    
    pdf_path = generate_pdf_reportlab(repo_info, output_pdf)
    if pdf_path:
        print(f"✓ Generated PDF: {pdf_path}")

if __name__ == '__main__':
    main()
