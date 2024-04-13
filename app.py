import streamlit as st

def list_page():
    st.title("List Page")
    st.write("This is the list page.")

def detail_page():
    st.title("Detail Page")
    st.write("This is the detail page.")

def main():
    st.set_page_config(page_title="你的标题")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["List Page", "Detail Page"])

    if selection == "List Page":
        list_page()
    elif selection == "Detail Page":
        detail_page()

if __name__ == "__main__":
    main()
