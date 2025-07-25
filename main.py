from fpdf import FPDF, YPos, XPos;
import pandas as pd;

pdf = FPDF(orientation="P", unit="mm", format="A4");
df = pd.read_csv("topics.csv");

for index, row in df.iterrows():
    pdf.add_page();
    pdf.set_text_color(100, 100, 100);
    pdf.set_font(family="Times", style="B", size=24);
    pdf.cell(w=0, h=12, text=row["Topic"], align="L", border=0,
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.line(x1=10, y1=21, x2=200, y2=22);

    for i in range(row["Pages"] - 1):
        pdf.add_page();

pdf.output("output.pdf");