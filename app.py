import streamlit as st 
from utils.chatbot_logic import load_advisory_data, get_best_match

file_path = 'data/advisory_data.csv'

advisory_dict = load_advisory_data(file_path)

# Streamlit setup
st.title("বাংলা কৃষি পরামর্শ চ্যাটবট")
st.write("আপনি যেকোনো কৃষি সমস্যা নিয়ে পরামর্শ চান তাহলে এখানে লিখুন।")

# User input 
user_input = st.text_input("আপনার প্রশ্ন লিখুন:")

if st.button("পরামর্শ প্রদান করুন"):
    if user_input:
        # Find the best match
        best_match = get_best_match(user_input, advisory_dict)
        if best_match:
            # Display the corresponding answer
            st.write("চ্যাটবটের উত্তর:", best_match)  # Directly display best_match as the answer
        else:
            st.write("দুঃখিত, আমি আপনার প্রশ্নের উত্তর খুঁজে পাইনি।")
    else:
        st.warning("দয়া করে একটি প্রশ্ন লিখুন।")
