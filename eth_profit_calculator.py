import streamlit as st

st.title("💰 ETH 投资收益计算器")

buy_price = st.number_input("买入价 (USD/ETH)", min_value=0.0, format="%.2f")
sell_price = st.number_input("卖出价 (USD/ETH)", min_value=0.0, format="%.2f")
invest_amount = st.number_input("投入金额 (USD)", min_value=0.0, format="%.2f")

if st.button("计算"):
    if buy_price > 0 and sell_price > 0 and invest_amount > 0:
        eth_amount = invest_amount / buy_price
        final_value = eth_amount * sell_price
        profit = final_value - invest_amount

        st.success("计算完成 ✅")
        st.write(f"**买入数量:** {eth_amount:.6f} ETH")
        st.write(f"**卖出总额:** {final_value:.2f} USD")
        st.write(f"**盈利:** {profit:.2f} USD")
    else:
        st.warning("请输入大于 0 的数值！")
