from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    make_shirtificate(name)

def make_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Add header text
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

    # Add shirt image
    pdf.image("shirtificate.png", x=10, y=50, w=190)

    # Overlay name on shirt (adjust based on image position)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 125)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

