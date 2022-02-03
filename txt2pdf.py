from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
f = open("C:/Users/Eathish/Desktop/GE_Healthcare/recordingtxt.txt", "r")
for x in f:
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.output("print.pdf")
