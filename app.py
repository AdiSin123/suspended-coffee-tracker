import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state if not present
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Donated', 'Claimed'])

# Streamlit UI
st.title("☕ Suspended Coffee Tracker")
st.write("Track donated and claimed suspended coffees.")

# Input fields
date = st.date_input("Select Date")
donated = st.number_input("Coffees Donated", min_value=0, step=1)
claimed = st.number_input("Coffees Claimed", min_value=0, step=1)

if st.button("Submit Record"):
    new_data = pd.DataFrame([[date, donated, claimed]], columns=['Date', 'Donated', 'Claimed'])
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.success("Record added successfully!")

# Data display
st.subheader("Coffee Data")
st.dataframe(st.session_state.data)

# Aggregated statistics
total_donated = st.session_state.data['Donated'].sum()
total_claimed = st.session_state.data['Claimed'].sum()
remaining = total_donated - total_claimed

st.metric("Total Donated", total_donated)
st.metric("Total Claimed", total_claimed)
st.metric("Remaining Coffees", max(remaining, 0))

# Visualization
st.subheader("Coffee Donations vs Claims")
fig, ax = plt.subplots()
ax.bar(["Donated", "Claimed", "Remaining"], [total_donated, total_claimed, max(remaining, 0)], color=['green', 'red', 'blue'])
ax.set_ylabel("Number of Coffees")
st.pyplot(fig)

# CSV Download
csv = st.session_state.data.to_csv(index=False).encode('utf-8')
st.download_button("Download Data as CSV", data=csv, file_name="suspended_coffee_data.csv", mime="text/csv")
