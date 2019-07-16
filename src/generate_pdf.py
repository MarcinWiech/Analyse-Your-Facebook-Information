import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
import locale

from src.conversation_util import Table_One_Object


class Document():
    
    def render_document(self, owner, table_one_objects):
        
        # Create doc from Template
        doc = SimpleDocTemplate("Facebook Analysis.pdf",pagesize=letter,
                                rightMargin=72,leftMargin=72,
                                topMargin=72,bottomMargin=72)
        Story=[]
        first_name = owner
        
        formatted_time = time.ctime()

        # Add space when displaying thousands
        locale.setlocale(locale.LC_ALL, '')
        
        # Add fonts
        pdfmetrics.registerFont(TTFont('Roboto-Light', 'Roboto-Light.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

        # Add mapping
        addMapping('Roboto-Light', 0, 0, 'Roboto-Light') #normal
        addMapping('Roboto-Light', 1, 0, 'Roboto-Regular') #bold
        
        # Add styles
        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontName='Roboto-Regular'))
        styles.add(ParagraphStyle(name='Normal_Mine', fontName='Roboto-Regular'))
        styles.add(ParagraphStyle(name='Table_Centre', fontName='Roboto-Light',fontSize=10,leading=12,spaceBefore=6, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Table', fontName='Roboto-Regular',fontSize=10,leading=12,spaceBefore=6))

        # Add header
        ptext = '<font size=16>%s\'s Document</font>' % first_name
        Story.append(Paragraph(ptext, styles["Center"]))

        # Add space
        Story.append(Spacer(1, 25))
        
        # Top conversations
        ptext = '<font size=12>Top conversations:</font>'
        Story.append(Paragraph(ptext, styles["Normal_Mine"]))

        # Add space
        Story.append(Spacer(1, 15))
        
        # Data for cells
        data = []
      
        # Table Headings
        data.append([
        Paragraph("", styles['Table']), 
        Paragraph("<b>Name</b>", styles['Table']), 
        Paragraph("<b>Number of messages</b>", styles['Table_Centre']), 
        Paragraph("<b>Your contribution to the conversation</b>", styles['Table_Centre'])
        ])

        
        # Add populate "data" array 
        for idx, table_one_object in enumerate(table_one_objects):
            idx_par = Paragraph(str(idx+1), styles['Table_Centre'])
            name_par = Paragraph(str(table_one_object.participant_name), styles['Table'])
            msgs_par = Paragraph("{0:n}".format(table_one_object.number_of_mssgs), styles['Table_Centre'])
            con_par = Paragraph(str(table_one_object.owners_contribution), styles['Table_Centre'])
            data.append([idx_par,name_par, msgs_par, con_par])
       
        # Create a table, define columns widths
        t=Table(data, colWidths =[0.4*inch,2*inch,2*inch,2*inch])

        # Make first row vertically aligned
        t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP')]))

        Story.append(t)

        doc.build(Story)