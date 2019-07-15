import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from conversation_util import Table_One_Object


class Document():
    
    def render_document(self, owner, table_one_objects):

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
        
        pdfmetrics.registerFont(TTFont('Roboto-Light', 'Roboto-Light.ttf'))
        
        
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontName='Roboto-Light'))
        styles.add(ParagraphStyle(name='Normal_Mine', fontName='Roboto-Light'))

        # Add header
        ptext = '<font size=16>%s\'s Document</font>' % first_name
        Story.append(Paragraph(ptext, styles["Center"]))

        # Add space
        Story.append(Spacer(1, 20))
        
        # Top friends
        ptext = '<font size=12>Top conversations:</font>'
        Story.append(Paragraph(ptext, styles["Normal_Mine"]))

        # Add space
        Story.append(Spacer(1, 5))

        # Print conversation numbers
        for idx, table_one_object in enumerate(table_one_objects):
            Story.append(Spacer(1, 3))
            ptext = '<font size=12>%s. %s - %s - %s</font>' % (idx+1, table_one_object.participant_name, table_one_object.number_of_mssgs, table_one_object.owners_contribution)
            Story.append(Paragraph(ptext, styles["Normal_Mine"]))   

        doc.build(Story)