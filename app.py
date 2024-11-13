import streamlit as st
from streamlit import button, checkbox

# 1. Displaying text methods
st.title("Learning Streamlit")
# st.header("Heading")
# st.subheader("Subheader Text")
# st.text("Normal text")
#
#
# st.markdown("**Text to be bold** and *Text to be Italicized")
#
# st.markdown("<h1>This is 1 text</h1>", unsafe_allow_html=True)
# st.markdown("<h2>This is 2 text</h2>", unsafe_allow_html=True)
# st.markdown("<h3>This is 3 text</h3>", unsafe_allow_html=True)
# st.markdown("<h4>This is 4 text</h4>", unsafe_allow_html=True)
# st.markdown("<h5>This is 5 text</h5>", unsafe_allow_html=True)
# st.markdown("<h6>This is 6 text</h6>", unsafe_allow_html=True)
# -----------------------------------------


# 2. Displaying Data in Streamlit
# df = {"Customers": ["Emeka", "John", "Smith", "Chris"] }
# st.dataframe(df)
# st.table(df)
# st.json(df)

# print(df["Customers"])

# 3. Adding Interactive widgets
# st.button("Analyze your data")
# st.slider("Select a category", 10, 20)
# st.selectbox("Select a category", ["Chris", "Chuck", "Blessing", "Emeka"])
#
# if st.checkbox("Click to Show data"):
#     st.selectbox("Select a category", ["Chris"])
#
#
# st.radio("Select a category", ["Chris", "Chuck", "Blessing", "Emeka"])
# st.radio("Select a category", ["Option 1", "Option 2"])
# # st.select_slider("Select from a slider", 1, ["John", 40])
#
# color = ["Joe", "Trump", "Kamala", "Vance", "Mr Musk"]
# selected = st.select_slider("Select a name on the slide", ["Joe", "Trump", "Kamala", "Vance", "Mr Musk"])
#
# st.write("Your class prefect selected is: ", selected)

# 3. Adding Interactive charts
df = {"Customers": ["Emeka", "John", "Smith", "Chris"]}
df2 = {"Sales": [100, 120, 55, 67]}

st.line_chart(df)
st.line_chart(df2)
st.bar_chart(df2)

st.file_uploader("Please, Select the image to upload")
