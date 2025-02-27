import streamlit as st 

# Sidebar Menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select options", ["Home", "Calculators", "About", "Setting"])

# Initialize theme in session state if not set
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"  # Default theme

# Function to apply CSS for the selected theme
def apply_theme(theme):
    if theme == "Dark":
        dark_theme_css = """
            <style>
                body, .stApp, .block-container { background-color: #0e1117 !important; color: white !important; }
                .stTextInput>div>div>input, .stSelectbox>div>div, .stNumberInput>div>div>input { 
                    background-color: #1c1e26 !important; 
                    color: white !important; 
                    border-radius: 5px !important;
                }
                .stButton>button { background-color: #444 !important; color: white !important; }
                .stMarkdown, .stTitle, .stHeader, .stText { color: white !important; }
            </style>
        """
        st.markdown(dark_theme_css, unsafe_allow_html=True)
    else:
        light_theme_css = """
            <style>
                body, .stApp, .block-container { background-color: white !important; color: black !important; }
                .stMarkdown, .stTitle, .stHeader, .stText { color: black !important; }
            </style>
        """    

        st.markdown(light_theme_css, unsafe_allow_html=True)

# Apply the selected theme
apply_theme(st.session_state.theme)

# Home section
if option == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Home Page!")

#calculators
elif option == "Calculators":
    calculator_options = st.selectbox("Select Your Calculator", ["Simple Calculator", "Scientific Calculator"])

    if calculator_options == "Simple Calculator":
        st.title("SIMPLE CALCULATOR")
        num1 = st.number_input("Enter first number", value=0)
        num2 = st.number_input("Enter second number", value=0)
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"

        st.write("✅ Result:", result)

#About section
elif option == "About":
    st.title("About")
    st.write("""
    This is a simple calculator app built using Streamlit.
    It allows basic arithmetic operations such as addition, subtraction, multiplication, and division.
    """)

#setting section
elif option == "Setting":
    st.title("Settings")
    theme_choice = st.radio("Select Theme", ["Light", "Dark"], index=0 if st.session_state.theme == "Light" else 1)

    # Update theme in session state
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()  # Force re-run to apply the new theme

    st.write(f"Selected Theme: {st.session_state.theme}")