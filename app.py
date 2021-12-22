import streamlit as st
import urllib


def main():
    
    st.set_page_config(layout="wide")
    readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    st.sidebar.title("What to do")


    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Instructions", "Show the source code", "Dashboard", "Prediction"])
    if app_mode == "Instructions":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Show the source code":
        readme_text.empty()
        st.code(get_file_content_as_string("app.py"))
    elif app_mode == "Dashboard":
        readme_text.empty()
        run_dashboard_app()
    elif app_mode == "Prediction":
        readme_text.empty()
        run_prediction_app()
    


def run_prediction_app():
    st.title("Prova App")    
       
def run_dashboard_app():
    st.title("Prova App 2")
    
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    url = 'https://github.com/mattiarigiroliacc/streamlit_example/main/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")


if __name__ == "__main__":
    main()