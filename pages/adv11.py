import streamlit as st
from utils import init_page

init_page()
st.title("這是標題")
st.write(
    "這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)

# 展開元件\
st.write("expander 展開元件")
with st.expander("這是一個展開元件"):
    st.write("這是一個展開元件的內容")

st.write("這是展開元件的外層內容")


# 數字元件
st.write("# number_input 數字元件")
number = st.number_input("輸入數字", min_value=0, max_value=100, value=50, step=5)
st.write(f"你輸入的數字是 {number}")


# 文字元件
st.write("# text_input 文字元件")
text = st.text_input("輸入文字", value="Hello, Streamlit!")
st.write(f"你輸入的文字是 {text}")

# 按鈕元件
st.write("# button 按鈕元件")
if st.button("点我"):
    st.write("你点我了")
    st.balloons()


st.write("---")

# 選項元件
st.write("# selectbox 選項元件")
selectbox = st.selectbox("選擇選項", ("選項1", "選項2", "選項3"))
st.write(f"你選擇的選項是 {selectbox}")

# 欄位元件
st.write("# st.columns 欄位元件")
col1, col2 = st.columns(2)
col1.write("這是左側欄位")
if col1.button("点我", key="col1"):
    col1.write("你点我了")
    st.balloons()

col2.write("這是右側欄位")
if col2.button("点我", key="col2"):
    col2.write("你点我了")
    st.balloons()


col1, col2 = st.columns(2)  # 建立2欄  col1和col2都是可以改變的變數，從左到右新增欄位
col1.button("按鈕1")  # 在第一欄建立按鈕
col2.button("按鈕2")  # 在第二欄建立按鈕

col1, col2 = st.columns([1, 2])  # 建立2欄 ，用list(1比2)改變欄位大小
col1.button("按鈕1", key="btn1")  # 在第一欄建立按鈕
col2.button("按鈕2", key="btn2")  # 在第二欄建立按鈕

with col1:  # 在col1中建立任意的元件
    st.markdown("欄位1")
    st.button("左按鈕")
with col2:  # 在col2中建立任意的元件
    st.markdown("欄位2")
    st.button("右按鈕")

cols = st.columns([3, 3, 1])  # 建立3欄 ，用list(3比3比1)改變欄位大小
cols[0].button("按鈕1", key="1")  # 在第一欄建立按鈕
cols[1].button("按鈕2", key="2")  # 在第二欄建立按鈕
cols[2].button("按鈕3", key="3")  # 在第三欄建立按鈕
# 將欄位吋到同一個變數中，讓cols變成一個list
