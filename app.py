import streamlit as st

def app():
    st.header('錢包輸入')
    st.write('注意！目前僅支援三條鏈，分別為 Ethereum, Polygon, Binance Smart Chain, 目前正在開發 Line Blockchain Service 中的 Daphne 網路')
    st.subheader('Ethereum 錢包地址')
    ethereum_wallet = st.text_input('','')
    st.subheader('Polygon 錢包地址','')
    polygon_wallet = st.text_input(' ','')
    st.subheader('Binance Smart Chain 錢包地址')
    bnb_wallet = st.text_input('   ','')
    clicked = st.button('確認')
    

import os
if __name__ == '__main__':
    app()