import streamlit as st
import urllib


def main():
    
    st.set_page_config(layout="wide")
    st.sidebar.title("What to do")

    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Dashboard", "Prediction"])

    if app_mode == "Dashboard":
        run_dashboard_app()
    elif app_mode == "Prediction":
        run_prediction_app()
    

def run_prediction_app():
    st.title("Prova App")    
       
def run_dashboard_app():
    st.title("Prova App 2")
    
if __name__ == "__main__":
    main()