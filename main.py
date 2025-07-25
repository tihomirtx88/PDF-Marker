from fpdf import FPDF, YPos, XPos

pdf = FPDF(orientation="P", unit="mm", format="A4");

pdf.add_page();

pdf.set_font(family="Times", style="B", size=12);

pdf.cell(w=0, h=12, text="Hello There", align="L", border=1,
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(w=0, h=12, text="Hi There", align="L", border=1,
         new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output("output.pdf");