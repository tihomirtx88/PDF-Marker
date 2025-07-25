from fpdf import FPDF, YPos, XPos;
import pandas as pd;

pdf = FPDF(orientation="P", unit="mm", format="A4");
pdf.set_auto_page_break(auto=False, margin=0);

df = pd.read_csv("topics.csv");

for index, row in df.iterrows():
    pdf.add_page();

    # Set the header
    pdf.set_text_color(100, 100, 100);
    pdf.set_font(family="Times", style="B", size=24);
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", border=0,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(x1=10, y1=21, x2=200, y2=22);

    # Set footer
    pdf.ln(265);
    pdf.set_font(family="Times", style="I", size=8);
    pdf.set_text_color(180, 180, 180);
    pdf.cell(w=0, h=10, text=row["Topic"], align="R", border=0,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    for i in range(row["Pages"] - 1):
        pdf.add_page();

        # Set footer
        pdf.ln(277);
        pdf.set_font(family="Times", style="I", size=8);
        pdf.set_text_color(180, 180, 180);
        pdf.cell(w=0, h=10, text=row["Topic"], align="R", border=0,
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("output.pdf");