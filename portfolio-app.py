import requests
import streamlit as st


#Set Page Configuration
st.set_page_config(
    page_title="Utkarsh Sahaya", 
    layout="wide",
)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")




# ---- LANDING SECTION ----
with st.container():
    left_column, right_column = st.columns([3, 1])
    with left_column:
        st.subheader('''Aspiring to dive deeper into the world of "Quantitative Finance"''')
        st.title("Hello, I am Utkarsh Sahaya from India :wave:")
        text = '''I am currently pursuing a Bachelor of Technology in Computer Science and Engineering from the <a href="https://www.iiitdmj.ac.in/">Indian Institute of Information Technology Design and Manufacturing, Jabalpur</a>. 
        I am passionate about Data Science and applying it to the field of finance. I continuously find ways by which 
        I can put to use my Computer Science knowledge in getting a better understanding and analysis of the Capital Market.
            '''
        st.markdown(text, unsafe_allow_html=True)
        st.write(
            '''The covid lockdown and online college gave me enough time to explore things, that's when I started to explore this field and it has been no looking back since then. 
        I taught myself topics of finance and went deeper to realize that mathematics plays a vital role. This is when I started to catch up with mathematics. 
        I also gave the GARP FRM Level 1 in May 2022 clearing it with a quartile score (1, 1, 1, 2).    
            ''')
        components = """
            <a href="###" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Resume</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="https://www.linkedin.com/in/utkarsh-sahaya/" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>LinkedIn</strong></button> </a>
            &nbsp; &nbsp;
            <a href="https://github.com/ut-upwards" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a>
            <br><br> """
        st.markdown(components, unsafe_allow_html=True)

    with right_column:
        st.image("profile_circle.png")



# ---- WHAT I KNOW ----
with st.container():
    st.write("---")
    st.header("What I know")
    left_column, right_column = st.columns(2)
    with right_column:
        st.write(
            """
            Being a Final-year student of Computer Science, I am very well familiar with the following topics:
            - C++ and Standard Template Library (STL) of C++ 
            - Python language including its popular libraries pandas, numpy, matplotlib
            - Object-Oriented Programming paradigm in both C++ and Python
            - Exploratory Data Analysis and Supervised Machine Learning (Regression)
            - Relational Database Management System, MySQL database, Structured Query Language (SQL)
            """
        )
    with left_column:
        st.write(
            """
            Topics of finance interest me a lot and I have taught myself the following:
            - Option Pricing and Option Greeks
            - Interest Rate Parity
            - Technical analysis and Fundamental analysis
            - Financial Risk Management (FRM Level 1) with Quartile scores (1,1,1,2)
            - Fixed Income Securities
            """
        )
st.write("##")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Mathematics is the most important in Quantitative Finance.
            I am working hard to catch up with the intense mathematics involved in this field, having an understanding of the following topics:
            - Probability and Statistics
            - Random Variables and their distribution
            - Hypothesis Testing 
            - Linear Regression and Multivariate Regression Analysis
            - Time Series Analysis
            - Simulation and Bootstrapping
            """
        )
    with right_column:
        st.write(
            """
            Tools I know:
            - MS Excel (Intermediate)
            - MS PowerPoint (Advanced)
            - Power BI Visualization Tool (Basic)
            - VS Code, Jupyter Notebook, Pycharm 
            """
        )


with st.container():
    st.write("---")
    st.header("My Personal Projects")
    st.subheader('My Approach of doing a Project')
    st.write('''My approach to doing a project is different because none of my projects are standard projects that could be found on google search. 
    All the projects are my answer to the problems I faced in the financial markets. 
    This is how I got really interested in the field of research and hence looking for an undergraduate research opportunity to learn and apply my passion and knowledge.''')
    st.write("---")


# ---- PROJECTS ----
with st.container():
    text_column, image_column = st.columns([2, 1])
    with image_column:
        st.image('nifty.jpg')
    with text_column:
        st.subheader("Nifty 21 Years")
            
        st.write(
            """- ***Problem Statement*** :&nbsp; I was new to the Stock market in 2021 and wanted to understand the historical behavior of Nifty50
            """
        )
        st.write("""- ***About*** :&nbsp; Descriptive analysis of 21 years of NIFTY 50 data along with macro-economic data
            """
        )
        st.write("""- ***Results*** :&nbsp; Simple and effective graphs along with other statistical results including **Time Series Analysis** giving insights of NIFTY 50 data of 21 years
            """
        )
        st.write("""- ***Concepts Used*** :&nbsp; Exploratory data analysis • pandas, numpy, matplotlib • Time Series Analysis
            """
        )
        components = """
            <a href="https://github.com/ut-upwards/NIFTY-21-years" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="https://github.com/ut-upwards/NIFTY-21-years/blob/b50f73ede9b16b81302b99ac10082d6e01243710/NIFTY%20%2021-Years.ipynb" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Jupyter Notebook</strong></button> </a>
            <br><br>"""
        st.markdown(components, unsafe_allow_html=True)


st.write("---")


with st.container():
    image_column, text_column = st.columns([1, 2])
    with image_column:
        st.image('techfin.png')
    with text_column:
        st.subheader("techfin- A python package for technical analysis ")
        st.write(
            """- ***Problem Statement*** :&nbsp; I wanted a clear understanding of how the indicators are calculated so that I could code strategies that are modifications of those standard indicators as per my need. 
            """
        )
        st.write("""- ***About*** :&nbsp; techfin is a python library still in the initial phase. It has 7 popular technical indicators implemented along with their graphical depiction. 
            """
        )
        st.write("""- ***Results*** :&nbsp;  Built a python package and deployed it on pypi.org, making it open source and ready to use for anybody. To install use the command 
        **pip install techfin**. 
            """
        )
        st.write("""- ***Future Improvements*** :&nbsp;  This package is still in initial phase and more indicators along with other functionalities will be added making it more extensive. 
            """
        )
        st.write("""- ***Concepts Used*** :&nbsp; Technical Analysis • Object-Oriented Programming
            """
        )

        components = """
            <a href="https://github.com/ut-upwards/techfin" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="https://pypi.org/project/techfin/" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>pypi.org</strong></button> </a>
            &nbsp; &nbsp;
            <a href="https://github.com/ut-upwards/techfin/blob/main/Technical_Indicators.ipynb" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Jupyter Notebook</strong></button> </a>
            <br>"""
        st.markdown(components, unsafe_allow_html=True)


st.write("---")


with st.container():
    text_column, image_column = st.columns([2, 1])
    with image_column:
        st.image('AnalyzeBhavCopy.jpg')
    with text_column:
        st.subheader("Analyze BhavCopy")
        st.write(
            """- ***Problem Statement*** :&nbsp; Used to go through the daily BhavCopy manually. Realized that I could automate this analysis.  
            """
        )
        st.write("""- ***About*** :&nbsp; BhavCopy is a csv file released daily by NSE. It has data on O-H-L-C, volume, and percentage delivery of all financial instruments being traded on NSE.
            """
        )
        st.write("""- ***Results*** :&nbsp;  Automated the analysis of the bhavCopy CSV file. Built a python app that has a simple drag-and-drop graphical interface to select the CSV file. 
        The app has further filters based on which the filtering and sorting of data is done. The app is deployed on the heroku platform and can be used by anybody.
            """
        )
        st.write("""- ***Concepts Used*** :&nbsp; Data Analysis • Basic Capital market knowledge for coding appropriate filters • heroku-Platform as a Service (PaaS)
            """
        )
        components = """
            <a href="https://github.com/ut-upwards/Analyze-BhavCopy" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="https://analyze-bhavcopy.herokuapp.com/" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>See Live</strong></button> </a>
            <br><br>"""
        st.markdown(components, unsafe_allow_html=True)


st.write("---")


with st.container():
    image_column, text_column = st.columns([1, 2])
    with image_column:
        st.image('niftybees.png')
    with text_column:
        st.subheader("NiftyBeeS-Nifty Pricing Analysis (***Ongoing Project***)")
        st.write(
            """- ***Problem Statement*** :&nbsp; Wanted to invest my internship stipend into Nifty ETF but was not sure about the correct price to enter. 
            ETFs in India are relatively less liquid compared to any popular stock hence the pricing is not the most efficient.  
            """
        )
        st.write("""- ***About*** :&nbsp; A simple analysis of Nifty Bees ETF and Nifty50 index to find efficient pricing and the trend in pricing of ETF.
            """
        )
        st.write("""- ***Results*** :&nbsp;  The analysis revealed that the ETF price is a factor of 1/90 times the index price and this factor has been on a steady decline since 2016 (the time when liquidity in Indian markets started improving rapidly).
            """
        )
        st.write("""- ***Future Improvements*** :&nbsp; Plans to get more insights about the pricing of ETF by analyzing to India Vix (Volatility) 
            """
        )
        st.write("""- ***Concepts Used*** :&nbsp; Basic Finance • Python
            """
        )
        components = """
            <a href="https://github.com/ut-upwards/NiftyBees-Nifty-Analysis" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="https://github.com/ut-upwards/NiftyBees-Nifty-Analysis/blob/d53a392d80d377aa2b968850027e88d3c9990eb7/Nifty%20&%20NiftyBees%20Analysis.ipynb" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Jupyter Notebook</strong></button> </a>
            <br>"""
        st.markdown(components, unsafe_allow_html=True)


st.write("---")


with st.container():
    text_column, image_column = st.columns([2, 1])
    with image_column:
        st.image('portfolio.png')
    with text_column:
        st.subheader("Portfolio Website")
        st.write(
            """- ***Problem Statement*** :&nbsp; I wanted a portfolio website to showcase my profile and my interests. I am a Computer Science and Engineering student and hence did not want to pay for website building.  
            """
        )
        st.write("""- ***About*** :&nbsp; A simple portfolio website that showcases my project and my interest in the field of Quantitative Finance.
            """
        )
        st.write("""- ***Results*** :&nbsp;  Coded a simple and responsive website using the **streamlit framework** of python. Deployed it on the heroku platform.
        It also has a contact form at the last so please feel free to send me your valuable suggestions or contact me for any queries.
            """
        )
        st.write("""- ***Concepts Used*** :&nbsp; Streamlit framework • CSS
            """
        )
        components = """
            <a href="###" target=_blank> 
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong>Github</strong></button> </a> 
            &nbsp; &nbsp; 
            <a href="###" target=_blank>
            <button style="padding:5px 15px 5px 15px; margin-top:3px"><strong> You are Live </strong></button> </a>
            <br><br>"""
        st.markdown(components, unsafe_allow_html=True)


st.write("---")


# ---- CERTIFICATIONS ----
with st.container():
    st.header("Certifications")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.image('GARP_frm.png')
        st.subheader('GARP FRM Level 1')
        st.write('''- Quartile Scores (1,1,1,2)
        ''')
        st.write('''- Financial Markets and Products
        ''')
        st.write('''-  Valuation and Risk Models
        ''')
    with middle_column:
        st.image('investment_foundations.png')
        st.subheader('CFA Investment Foundations Certificate')
        st.write('''- Macroeconomics & Microeconomics
        ''')
        st.write('''- Structure of Investment Industry
        ''')
    with right_column:
        st.image('NSEacademy.png')
        st.subheader('NSE Academy Certified Derivaties Pro')
        st.write('''- Module 1: Equity Derivatives Beginner Module
        ''')
        st.write('''- Module 2: Derivatives Market (Dealers Module)
        ''')
        st.write('''- Module 3: Option Trading Strategies Module
        ''')



# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact - Happy to answer any of your queries!")
    left_column, right_column = st.columns([3, 1])
    #st.write("##")
    with left_column:
        contact_form = """
        <form action="https://formsubmit.co/sahaya.utkarsh@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
