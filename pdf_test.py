import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
 
doc = SimpleDocTemplate("Facebook Analysis.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story=[]
first_name = "Marcin"
 
formatted_time = time.ctime()

convs = [('Person one', (52005, [('Person one', 29127), ('Owner', 22878)], [('Person one', 116645), ('Owner', 91674)])),
('Person two', (39369, [('Person two', 20481), ('Owner', 18888)], [('Person two', 82124), ('Owner', 75740)])),
('Person three', (12664, [('Owner', 6389), ('Person three', 6275)], [('Owner', 25625), ('Person three', 25264)])),
('Person four', (12595, [('Person four', 6871), ('Owner', 5724)], [('Person four', 27538), ('Owner', 22918)]))]
 

 
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))

# Add header
ptext = '<font size=16>%s\'s Document</font>' % first_name
Story.append(Paragraph(ptext, styles["Center"]))

# Add space
Story.append(Spacer(1, inch))
 
# Top friends
ptext = '<font size=12>Top friends:</font>'
Story.append(Paragraph(ptext, styles["Normal"]))

# Add space
Story.append(Spacer(1, 5))

# Print conversation numbers
for conv in convs:
    ptext = '<font size=12>%s : %s</font>' % (conv[0], conv[1][0])
    Story.append(Paragraph(ptext, styles["Normal"]))   

doc.build(Story)