import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Business Information Form", layout="centered")

    st.title("Business Information Submission")
    st.write("Please fill out the form below with your details.")

    with st.form("business_info_form"):
        # Text Inputs
        your_name = st.text_input("Your Name:")
        business_name = st.text_input("Your Business Name:")
        university = st.text_input("Your University:")
        business_description = st.text_area("Small Description of Your Business:")

        # File Uploader for Picture
        uploaded_picture = st.file_uploader("Upload a Picture of you or your Business (JPG or PNG):", type=["jpg", "png"])

        # Submit Button
        submit_button = st.form_submit_button("Submit Information")

        if submit_button:
            if your_name and business_name and university and business_description:
                st.success("Information Submitted Successfully!")
                st.write(f"**Your Name:** {your_name}")
                st.write(f"**Business Name:** {business_name}")
                st.write(f"**University:** {university}")
                st.write(f"**Business Description:** {business_description}")

                if uploaded_picture is not None:
                    try:
                        image = Image.open(uploaded_picture)
                        st.image(image, caption="Uploaded Picture", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error loading image: {e}")
                else:
                    st.warning("No picture was uploaded.")
            else:
                st.error("Please fill in all the text fields before submitting.")

if __name__ == "__main__":
    main()