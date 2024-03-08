# Run me with
# streamlit run example.py

import streamlit as st

from streamlit_alpine import streamlit_alpine

st.set_page_config(page_title="Streamlit + Alpine.js", page_icon="😛")

st.subheader("Streamlit + Alpine.js")

# Create an instance of our component with a constant `name` arg, and
# print its output value.
num_clicks = streamlit_alpine("World")
st.markdown("Streamlit says you've clicked %s times!" % int(num_clicks))

st.markdown("---")
st.subheader("Component with variable args")

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
name_input = st.text_input("Enter a name", value="Streamlit")
num_clicks = streamlit_alpine(name_input, key="foo")
st.markdown("Streamlit says you've clicked %s times!" % int(num_clicks))