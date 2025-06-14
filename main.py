import streamlit as st

st.set_page_config(page_title="Business Owner Form", page_icon="🔥")

st.title("📋 Student Business Owner Submission Form")

# Form
with st.form("business_form"):
    st.subheader("👤 Owner Information")
    owner_name = st.text_input("Your Name")
    owner_email = st.text_input("Your Email")
    university = st.text_input("University")

    st.subheader("🏪 Business Information")
    business_name = st.text_input("Name of your Business")
    business_description = st.text_area("Business Description")

    fb_link = st.text_input("Facebook Page Link")
    insta_link = st.text_input("Instagram Profile Link")

    profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("🚀 Submit")

# On Submit
if submitted:
    st.success("✅ Form submitted successfully!")

    # Display entered data (optional)
    st.write("### Submitted Info:")
    st.write("**Owner Name:**", owner_name or "Not provided")
    st.write("**Email:**", owner_email or "Not provided")
    st.write("**University:**", university or "Not provided")
    st.write("**Business Name:**", business_name or "Not provided")
    st.write("**Description:**", business_description or "Not provided")
    st.write("**Facebook Link:**", fb_link or "Not provided")
    st.write("**Instagram Link:**", insta_link or "Not provided")

    if profile_pic:
        st.image(profile_pic, caption="Uploaded Profile Picture", use_column_width=True)
    else:
        st.write("No profile picture uploaded.")
