from PyPDF2 import PdfReader, PdfWriter, PdfMerger
################
# Reading PDFs #
################
# Create a PDF Reader
reader = PdfReader("COMP1112_W11.pdf")

# The pages property is a list of all pages in the PDF
for page in reader.pages:
    print(page.extract_text())

body_parts = []
head_parts = []

# Visitor methods can pick and choose what text they want to keep.
# They include a few standard variables that give us information 
# about the text we are reading, the varaibles are:
# text: the raw text data read in as a string
# cm: current transformation matrix (handles how the the text is displayed on the page, based on the Adobe PDF spec)
# tm: text matrix, the most important elements are tm[4] and tm[5], the text's x and y position on the page. The elements in order are [Scale_x, Scale_y, Shear_x, Shear_y, Offset_x, Offset_y]
# fontDict: Information about the font and character encoding
# fontSize: the size of the font as an integer

# The body visitor only keeps text with fontSize == 18
def visitor_body(text, cm, tm, fontDict, fontSize):
    if fontSize == 18:
        body_parts.append(text)

# The header visitor only keeps text larger than fontSize > 24
def visitor_headers(text, cm, tm, fontDict, fontSize):
    if fontSize > 24:
        head_parts.append(text)

# Extract text using our visitors
for page in reader.pages:
    page.extract_text(visitor_text=visitor_body)

print("".join(body_parts))

for page in reader.pages:
    page.extract_text(visitor_text=visitor_headers)

print("\n".join(head_parts))

################
# Editing PDFs #
################

## Split a PDF ##
for i in range(len(reader.pages)):
    # For each page, create a new PDF writer
    singleWriter = PdfWriter()

    # Add the single page to writer
    singleWriter.add_page(reader.pages[i])

    # Write the PDF
    with open(f"COMP1112_W11_P{i}.pdf", "wb") as f:
        singleWriter.write(f)

## Merging PDFs ##
# Create readers for each PDF to merge
merger = PdfMerger()

# The merger only requires the file paths to run
for pdf in ["COMP1112_W11_P0.pdf", "COMP1112_W11_P1.pdf", "COMP1112_W11_P2.pdf"]:
    merger.append(pdf)

# The merger can handle writing to a file as well
merger.write("merged.pdf")

merger.close() # Remeber to close the merger! You could use with-as syntax here too.

## Password Protect a PDF ##
cryptWriter = PdfWriter()

# Add pages to writer
for page in reader.pages:
    cryptWriter.add_page(page)

# Encrypt with a password of your choosing
cryptWriter.encrypt("password")

# Write encrypted file
with open("COMP1112_W11_locked.pdf", "wb") as f:
    cryptWriter.write(f)