#3 feedback system

# if the password is weal , suggest improvments,
# if the pasword is strong display a success message

import re
import streamlit as st

#page styling
st.set_page_config(page_title="password strenth checker by Asad Ali", page_icon="🔑", layout="centered")
#custom css
st.markdown("""
<style>
      .main {text-align: center;}
      .stTextInput {width: 60% !important; marin:auto;}      
      .stButton button {width:50%; background-color #4caf50; color: white; font-size: 17px;}
      .stButton button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)
#page tital and decription
st.title ("🔐 password strenght Genrator")
st.write(" Enter your password below to check its security level! 🔍")

#function to check password strength
def chec_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("password should be **atleast 8 character long**⛑️")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else :
        feedback.append("password should include **both upper case(A-Z) and lower case (a-z) letters**⛑️")

    if re.search (r"\d", password):
        score += 1
    else:
        feedback.append("password should include **at atlest one number (0-9) **⛑️")
    
    #spacial charaters
    if re.search(r"[!@$&^%]", password):
        score +=1
    else:
        feedback.append("include **at least one special charater (!@$&^%)**⛑️")

    #display password strength result
    if score == 4:
        st.success ("✔️ **strong password** - your password is secure,")
    elif score == 3:
        st.info ("⚠️ ** moderate password** - consider imporving security by adding more feature ")
    else:
        st.error ("⛑️ **weak password** - follow the suggestion below to strength it,")
     
    #feedback
    if feedback:
        with st.expander("🔍**improve your password**"):
            for item in feedback:
                  st.write(item)

    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

    #Butoon Working
    if st.button("Check strength"):
        if password:
            chec_password_strength(password)
        else:
            st.warning("⚠️ please enter a password first!") #show warning if password empty
