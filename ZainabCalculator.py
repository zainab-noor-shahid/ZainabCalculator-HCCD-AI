import streamlit as st

st.set_page_config(page_title="Streamlit Calculator", layout="centered")
st.title("🧮Zainab Calculator🧮")
# Styling
st.markdown("""
    <style>
    .calc-display {
        font-size: 48px;
        text-align: right;
        background-color: #002855;
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Session state for input
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to handle click
def handle_click(label):
    exp = st.session_state.expression
    if label == "C":
        st.session_state.expression = ""
    elif label == "+/-":
        if exp.startswith("-"):
            st.session_state.expression = exp[1:]
        else:
            st.session_state.expression = "-" + exp
    elif label == "%":
        try:
            st.session_state.expression = str(float(eval(exp)) / 100)
        except:
            st.session_state.expression = "Error"
    elif label == "=":
        try:
            result = eval(exp)
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
    else:
        if label in "+-/" and (not exp or exp[-1] in "+-/"):
            return  # prevent double operators
        st.session_state.expression += label

# Display current expression
st.markdown(f"<div class='calc-display'>{st.session_state.expression or '0'}</div>", unsafe_allow_html=True)

# Button grid: exactly 4 items in every row
buttons = [
    ["C", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Create buttons
for row in buttons:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if label != "":
            if cols[i].button(label, use_container_width=True):
                handle_click(label)
                st.rerun()
        else:
            cols[i].markdown(" ")