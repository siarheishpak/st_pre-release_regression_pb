import streamlit as st
import time
import datetime
import pandas as pd
import numpy as np

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
	time.sleep(3)  # 👈 This makes the function take 2s to run
	st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
	return a ** b

if st.checkbox('Cache'):
    st.header('Cache')
    a = st.number_input("Provide the first number", value=3)
    b = st.number_input("Provide the second number", value=5)
    res = expensive_computation(a, b)
    st.write("Result:", res)

if st.checkbox('Upload an image'):
    uploaded_image = st.file_uploader(label="Choose a file", type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        st.image(uploaded_image.getvalue())

if st.checkbox('Upload a csv'):
    uploaded_csv = st.file_uploader(label="Choose a file", type=['csv'])
    if uploaded_csv:
        csv_data = pd.read_csv(uploaded_csv, index_col=0)
        st.line_chart(csv_data)

if st.checkbox('Camera'):
    camera_image = st.camera_input("camera_widget")
    if camera_image:
        st.write(camera_image)
        st.image(camera_image.getvalue())

if st.checkbox('Property "disabled=True"'):
	st.button('disabled button', disabled=True)
	st.camera_input("disabled camera", disabled=True)
	st.download_button(label="disabled download_button", data='https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f41b.svg', disabled=True)
	st.checkbox("disabled checkobx", disabled=True)
	st.radio("disabled radio", options=('one', 'two', 'three'), disabled=True)
	st.selectbox("disableld selectbox", options=('one', 'two', 'three'), disabled=True)
	st.multiselect("disabled multiselect", options=('one', 'two', 'three'), default=['one', 'three'], disabled=True)
	st.slider("disabled slider", disabled=True)
	st.text_input('disabled text_input', value='Lorem ipsum', disabled=True)
	st.number_input('disabled number_input', min_value=5, max_value=15, value=6, disabled=True)
	st.text_area('disabled text_area', value="Lorem ipsum", disabled=True)
	st.date_input('disabled date_input', value=datetime.datetime.today(), disabled=True)
	st.time_input('disabled time_input', value=datetime.datetime.now().time(), disabled=True)
	st.file_uploader('disabled file_uploader', disabled=True)
	st.color_picker('disabled color_picker', disabled=True)
	st.select_slider('disabled select_slider', options=('one', 'two', 'three'), value='two', disabled=True)

if st.checkbox('Property "disabled=False"'):
	st.button('disabled button', disabled=False)
	st.camera_input("disabled camera", disabled=False)
	st.download_button(label="disabled download_button", data='https://notion-emojis.s3-us-west-2.amazonaws.com/prod/svg-twitter/1f41b.svg', disabled=False)
	st.checkbox("disabled checkobx", disabled=False)
	st.radio("disabled radio", options=('one', 'two', 'three'), disabled=False)
	st.selectbox("disableld selectbox", options=('one', 'two', 'three'), disabled=False)
	st.multiselect("disabled multiselect", options=('one', 'two', 'three'), default=['one', 'three'], disabled=False)
	st.slider("disabled slider", disabled=False)
	st.text_input('disabled text_input', value='Lorem ipsum', disabled=False)
	st.number_input('disabled number_input', min_value=5, max_value=15, value=6, disabled=False)
	st.text_area('disabled text_area', value="Lorem ipsum", disabled=False)
	st.date_input('disabled date_input', value=datetime.datetime.today(), disabled=False)
	st.time_input('disabled time_input', value=datetime.datetime.now().time(), disabled=False)
	st.file_uploader('disabled file_uploader', disabled=False)
	st.color_picker('disabled color_picker', disabled=False)
	st.select_slider('disabled select_slider', options=('one', 'two', 'three'), value='two', disabled=False)

if st.checkbox('clear() function'):
	@st.experimental_memo
	def experimental_memo_clear(a, b):
		time.sleep(3)
		return a ** b

	@st.experimental_singleton
	def experimental_singleton_clear(a, b):
		time.sleep(3)
		return a ** b

	@st.cache
	def cache_clear(a, b):
		time.sleep(3)
		return a ** b

	a = st.number_input("Provide the first number", value=3)
	b = st.number_input("Provide the second number", value=5)
	st.subheader('experimental_memo')
	res1 = experimental_memo_clear(a, b)
	st.write("Result:", res1)
	if st.button('clear experimental_memo'):
		st.experimental_memo.clear()
	st.subheader('experimental_singleton')
	res2 = experimental_singleton_clear(a, b)
	st.write("Result:", res2)
	if st.button('clear experimental_singleton'):
		st.experimental_singleton.clear()
	st.subheader('cache')
	res3 = cache_clear(a, b)
	st.write("Result:", res3)
	if st.button('clear cache'):
		st.cache.clear() # should not work!

if st.checkbox("Nested tags + unsafe_allow_html"):
	st.markdown('### <span><span>Test</span></span>', unsafe_allow_html=True)
	st.write('### <span><span>Test</span></span>', unsafe_allow_html=True)
	st.markdown('<span>hello <span>world</span></span>', unsafe_allow_html=True)
