import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

data = list(range(-29, 31, 3))
print(data)




c1 = st.sidebar.radio('선의 색을 선택하시오',['red', 'green', 'blue', 'orange'])
s1 = st.sidebar.radio('선의 형태을 선택하시오', ['-', ':', '--'])
m1 = st.sidebar.radio('마커의 형태를 선택하시오',['o', '^', 's', 'p'])
     
love= []
y= []
for i in range(-20, 21, 3):
    love.append(i)
    y.append(-2*i*i + 3*i + 5)

plt.plot(love, y, color = c1, linestyle = s1, marker = m1)

st.pyplot(fig)

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)