import streamlit as st
from scrapper import scrape_website,split_dom_content,clean_body_content,extract_body_content
from parse import parse_with_ollama

st.title('AI Web Scrapper')
url = st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    content = scrape_website(url)
    body_content = extract_body_content(content)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content ## allow us to access it later

    with st.expander("View DOM Content"):
        st.text_area("DOM Content",cleaned_content,height=300)



if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse ?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks=dom_chunks,parse_description=parse_description)
            st.write(result)


