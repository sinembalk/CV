from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

# Text
Name = 'Sinem Balkuvar'
Contact = '            Istanbul, Turkey\n         +90 533 570 6432\n    sinembalkuvar@gmail.com\nlinkedin.com/in/sinem-balkuvar\n         github.com/sinembalk'
Info = 'I am working as a data scientist at ING with enthusiasm about driving value\nfrom data. I have 3 years of experience in building data products, from data\nexploration to implementation'
WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'ING, Turkey | Data Scientist'
WorkOneTime = 'June 2021 - Present'
WorkOneDesc = '- Experimenting supervised machine learning models to derive actionable\ninsights from massive customer data for customer conversion on retail credits'
WorkTwoTitle = 'ING, The Netherlands | Data Scientist'
WorkTwoTime = 'October 2020 - June 2021'
WorkTwoDesc = '- Developed an unsupervised machine learning model to help business\nstakeholders identify trade-based money laundering transactions\n\n- Built dashboard in Superset to showcase model output for model end users'
WorkThreeTitle = 'ING, Turkey | Data Scientist'
WorkThreeTime = 'July 2018 - October 2020'
WorkThreeDesc = '- Developed supervised machine learning models using complex Credit Bureau\n data to mitigate default risk in retail credits\n\n- Built interactive and automated reporting system in Plotly Dash to help\nmonitor retail credit limits\n\n- Built automated HTML reports and decks in Python to assist in analysing\ncertain risk-based metrics for retail credits'
WorkFourTitle = 'Sabanci University | Teaching Assistant'
WorkFourTime = 'September 2016 - July 2018'
WorkFourDesc = '- Conducted Econometrics and Microeconomics recitation classes'
EduHeader = 'EDUCATION'
EduOneTitle = 'Ozyegin University, Turkey | M.S. in Data Science'
EduOneTime = 'September 2019 - Present'
EduTwoTitle = 'Sabanci University, Turkey | M.A. in Economics'
EduTwoTime = 'September 2016 - June 2018'
EduTwoDesc = 'Thesis: The quality of immigrant human capital and market outcomes'
EduThreeTitle = 'Middle East Technical University, Turkey | B.S. in Economics'
EduThreeTime = 'September 2012- June 2016'
EduFourTitle= 'Chuo University, Japan | Exchange'
EduFourTime= 'February 2015- June 2015'
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Spark\n- SQL\n- HTML\n- Command Line\n- Git and Version Control\n- Data Visualization\n- Data Manipulation\n- NLP/ text mining techniques\n- Probability/ Statistics\n'
ExtrasTitle = 'Interests'
ExtrasDesc = '- Volleyball\n- Travelling\n- Plants'
LanguageTitle = 'Languages'
LanguageDesc = '- English (Fluent)\n- German (Intermediate)\n- Turkish (Native)'

# Setting style for bar graphs
import matplotlib.pyplot as plt
%matplotlib inline
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))

# set the background boxes
#plt.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.0, color='#000000', alpha=0.5, linewidth=290)
plt.axvline(x=.0, color='#000000', alpha=0.01, linewidth=1500)

# set background color
ax.set_facecolor('white')

plt.axis('off')
plt.annotate(Name, (0.32,.96), weight='bold', fontsize=28)
plt.annotate(Contact, (0.015,.62), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(Info, (0.32,.89), weight='regular', fontsize=10, alpha= 0.75 )
plt.annotate(WorkHeader, (0.32,.84), weight='bold', fontsize=13, color='#2c7f84')
plt.annotate(WorkOneTitle, (0.32,.82), weight='bold', fontsize=11)
plt.annotate(WorkOneTime, (0.32,.80), weight='regular', fontsize=10, alpha=.75)
plt.annotate(WorkOneDesc, (0.32,.76), weight='regular', fontsize=10)
plt.annotate(WorkTwoTitle, (0.32,.72), weight='bold', fontsize=11)
plt.annotate(WorkTwoTime, (0.32,.70), weight='regular', fontsize=10, alpha=.75)
plt.annotate(WorkTwoDesc, (0.32,.62), weight='regular', fontsize=10)
plt.annotate(WorkThreeTitle, (0.32,.58), weight='bold', fontsize=11)
plt.annotate(WorkThreeTime, (0.32,.56), weight='regular', fontsize=10, alpha=.75)
plt.annotate(WorkThreeDesc, (0.32,.40), weight='regular', fontsize=10)
plt.annotate(WorkFourTitle, (0.32,0.36), weight='bold', fontsize=11)
plt.annotate(WorkFourTime, (0.32,0.34), weight='regular', fontsize=10, alpha=.75)
plt.annotate(WorkFourDesc, (0.32,0.315), weight='regular', fontsize=10)
plt.annotate(EduHeader, (0.32,.26), weight='bold', fontsize=13, color='#2c7f84')
plt.annotate(EduOneTitle, (0.32,.24), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (0.32,.22), weight='regular', fontsize=10, alpha=.75)
plt.annotate(EduTwoTitle, (0.32,.19), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (0.32,.17), weight='regular', fontsize=10, alpha=.75)
plt.annotate(EduTwoDesc, (0.32,.15), weight='regular', fontsize=10)
plt.annotate(EduThreeTitle, (0.32,.12), weight='bold', fontsize=10)
plt.annotate(EduThreeTime, (0.32,.10), weight='regular', fontsize=10, alpha=.75)
plt.annotate(EduFourTitle, (0.32,.075), weight='bold', fontsize=10)
plt.annotate(EduFourTime, (0.32,.055), weight='regular', fontsize=10, alpha=.75)
plt.annotate(SkillsHeader, (0.1,.55), weight='bold', fontsize=12, color='#ffffff')
plt.annotate(SkillsDesc, (0.01,.34), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(LanguageTitle, (0.08,.30), weight='bold', fontsize=12, color='#ffffff')
plt.annotate(LanguageDesc, (0.01,.23), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (0.09,.175), weight='bold', fontsize=12, color='#ffffff')
plt.annotate(ExtrasDesc, (0.01,.105), weight='bold', fontsize=10, color='#ffffff')
arr_code = mpimg.imread('sbalkuvar.jpg')
imagebox = OffsetImage(arr_code, zoom=0.23)
ab = AnnotationBbox(offsetbox=imagebox, frameon=False, xy= (0.152, 0.85))
ax.add_artist(ab)
plt.savefig('sbalkuvar_cv.pdf',  bbox_inches='tight')