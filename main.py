# import streamlit as st
# from PIL import Image
#
# def main():
#     st.set_page_config(page_title="Business Information Form", layout="centered")
#
#     st.title("Business Information Submission")
#     st.write("Please fill out the form below with your details.")
#
#     with st.form("business_info_form"):
#         # Text Inputs
#         your_name = st.text_input("Your Name:")
#         business_name = st.text_input("Your Business Name:")
#         university = st.text_input("Your University:")
#         business_description = st.text_area("Small Description of Your Business:")
#
#         # File Uploader for Picture
#         uploaded_picture = st.file_uploader("Upload a Picture of you or your Business (JPG or PNG):", type=["jpg", "png"])
#
#         # Submit Button
#         submit_button = st.form_submit_button("Submit Information")
#
#         if submit_button:
#             if your_name and business_name and university and business_description:
#                 st.success("Information Submitted Successfully!")
#                 st.write(f"**Your Name:** {your_name}")
#                 st.write(f"**Business Name:** {business_name}")
#                 st.write(f"**University:** {university}")
#                 st.write(f"**Business Description:** {business_description}")
#
#                 if uploaded_picture is not None:
#                     try:
#                         image = Image.open(uploaded_picture)
#                         st.image(image, caption="Uploaded Picture", use_column_width=True)
#                     except Exception as e:
#                         st.error(f"Error loading image: {e}")
#                 else:
#                     st.warning("No picture was uploaded.")
#             else:
#                 st.error("Please fill in all the text fields before submitting.")
#
# if __name__ == "__main__":
#     main()

#
# import streamlit as st
# from PIL import Image
# import sqlite3
# import io # Needed to convert bytes back to image for display
#
# # --- Database Configuration ---
# # The name of your SQLite database file
# DB_FILE = "student_businesses.db"
#
# def init_db():
#     """
#     Initializes the SQLite database and creates the 'student_businesses' table
#     if it doesn't already exist.
#     """
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS student_businesses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             business_name TEXT NOT NULL,
#             university TEXT NOT NULL,
#             business_description TEXT NOT NULL,
#             picture_data BLOB -- Stores the image as binary data
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# def insert_data(name, business_name, university, description, picture_bytes):
#     """
#     Inserts a new record into the 'student_businesses' table.
#     """
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     try:
#         c.execute('''
#             INSERT INTO student_businesses (name, business_name, university, business_description, picture_data)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (name, business_name, university, description, picture_bytes))
#         conn.commit()
#         return True
#     except sqlite3.Error as e:
#         st.error(f"Database insertion error: {e}")
#         return False
#     finally:
#         conn.close()
#
# # --- Streamlit App ---
# def main():
#     st.set_page_config(page_title="Student Business Owners Platform", layout="centered")
#
#     # Call init_db() first to ensure the database and table are ready
#     init_db()
#
#     st.title("Business Information Submission")
#     st.write("Please fill out the form below with your details.")
#
#     with st.form("business_info_form"):
#         # Text Inputs
#         your_name = st.text_input("Your Name:")
#         business_name = st.text_input("Your Business Name:")
#         university = st.text_input("Your University:")
#         business_description = st.text_area("Small Description of Your Business:")
#
#         # File Uploader for Picture
#         uploaded_picture = st.file_uploader("Upload a Picture of you or your Business (JPG or PNG):", type=["jpg", "png"])
#
#         # Submit Button
#         submit_button = st.form_submit_button("Submit Information")
#
#         if submit_button:
#             # Check if all required text fields are filled
#             if your_name and business_name and university and business_description:
#                 picture_bytes_to_store = None
#                 if uploaded_picture is not None:
#                     # Read the uploaded image file into bytes for database storage
#                     picture_bytes_to_store = uploaded_picture.read()
#
#                     # Optionally, display the uploaded image for preview before saving
#                     try:
#                         image_preview = Image.open(uploaded_picture)
#                         # --- CHANGE IS HERE ---
#                         st.image(image_preview, caption="Uploaded Picture Preview", use_container_width=True)
#                     except Exception as e:
#                         st.warning(f"Could not display image preview: {e}")
#
#                 # Insert data into the database
#                 if insert_data(your_name, business_name, university, business_description, picture_bytes_to_store):
#                     st.success("Information Submitted Successfully and Stored in Database!")
#                     st.write(f"**Your Name:** {your_name}")
#                     st.write(f"**Business Name:** {business_name}")
#                     st.write(f"**University:** {university}")
#                     st.write(f"**Business Description:** {business_description}")
#                 else:
#                     st.error("Failed to store information in the database. Please check the logs.")
#             else:
#                 st.error("Please fill in all the required text fields before submitting.")
#
#     st.markdown("---")
#     st.subheader("Currently Stored Business Entries:")
#
#     # --- Display Stored Data (for demonstration) ---
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     # Fetch all data from the table
#     c.execute("SELECT name, business_name, university, business_description, picture_data FROM student_businesses ORDER BY id DESC")
#     rows = c.fetchall()
#     conn.close()
#
#     if rows:
#         for i, row in enumerate(rows):
#             st.write(f"**Entry {len(rows) - i}:**") # Numbering from newest to oldest
#             st.write(f"  - **Name:** {row[0]}")
#             st.write(f"  - **Business Name:** {row[1]}")
#             st.write(f"  - **University:** {row[2]}")
#             st.write(f"  - **Description:** {row[3]}")
#             if row[4]: # If picture_data exists
#                 try:
#                     # Convert the binary data back to an image object for display
#                     image_from_db = Image.open(io.BytesIO(row[4]))
#                     # The width parameter is fine, no change needed here if you want fixed width.
#                     # If you want it to also fill the container, you could use use_container_width=True here as well.
#                     st.image(image_preview, caption="Uploaded Picture Preview", use_container_width=True)
#                 except Exception as e:
#                     st.write(f"  - (Could not display picture for {row[1]}: {e})")
#             else:
#                 st.write("  - (No picture uploaded for this entry)")
#             st.markdown("---") # Separator between entries
#     else:
#         st.info("No business information has been submitted yet.")
#
# if __name__ == "__main__":
#     main()


import streamlit as st
from PIL import Image
import sqlite3
import io # Needed to convert bytes back to image for display

# --- Database Configuration ---
# The name of your SQLite database file
DB_FILE = "student_businesses.db"

def init_db():
    """
    Initializes the SQLite database and creates the 'student_businesses' table
    if it doesn't already exist.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # IMPORTANT: If you already have data in student_businesses.db,
    # adding a new column 'email' might require you to:
    # 1. Delete the old 'student_businesses.db' file (losing existing data).
    # 2. Or, run an ALTER TABLE command:
    #    c.execute('ALTER TABLE student_businesses ADD COLUMN email TEXT;')
    #    You should only run ALTER TABLE once. For simplicity, if this is development,
    #    it's often easiest to just delete the .db file and let it recreate.
    c.execute('''
        CREATE TABLE IF NOT EXISTS student_businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL, -- ADDED: Email field
            business_name TEXT NOT NULL,
            university TEXT NOT NULL,
            business_description TEXT NOT NULL,
            picture_data BLOB -- Stores the image as binary data
        )
    ''')
    conn.commit()
    conn.close()

# Updated insert_data to accept 'email'
def insert_data(name, email, business_name, university, description, picture_bytes):
    """
    Inserts a new record into the 'student_businesses' table.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO student_businesses (name, email, business_name, university, business_description, picture_data)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, business_name, university, description, picture_bytes))
        conn.commit()
        return True
    except sqlite3.Error as e:
        st.error(f"Database insertion error: {e}")
        return False
    finally:
        conn.close()

# --- Streamlit App ---
def main():
    st.set_page_config(page_title="Student Business Owners Platform", layout="centered")

    # Call init_db() first to ensure the database and table are ready
    init_db()

    st.title("Business Information Submission")
    st.write("Please fill out the form below with your details.")

    with st.form("business_info_form"):
        # Text Inputs
        your_name = st.text_input("Your Name:")
        your_email = st.text_input("Your Email Address:") # ADDED: Email input
        business_name = st.text_input("Your Business Name:")
        university = st.text_input("Your University:")
        business_description = st.text_area("Small Description of Your Business:")

        # File Uploader for Picture
        uploaded_picture = st.file_uploader("Upload a Picture of you or your Business (JPG or PNG):", type=["jpg", "png"])

        # Submit Button
        submit_button = st.form_submit_button("Submit Information")

        if submit_button:
            # Check if all required text fields are filled (including email)
            if your_name and your_email and business_name and university and business_description:
                picture_bytes_to_store = None
                if uploaded_picture is not None:
                    # Read the uploaded image file into bytes for database storage
                    picture_bytes_to_store = uploaded_picture.read()

                    # Optionally, display the uploaded image for preview before saving
                    try:
                        image_preview = Image.open(uploaded_picture)
                        st.image(image_preview, caption="Uploaded Picture Preview", use_container_width=True)
                    except Exception as e:
                        st.warning(f"Could not display image preview: {e}")

                # Call insert_data with the new 'email' parameter
                if insert_data(your_name, your_email, business_name, university, business_description, picture_bytes_to_store):
                    st.success("Information Submitted Successfully and Stored in Database!")
                    st.write(f"**Your Name:** {your_name}")
                    st.write(f"**Your Email:** {your_email}") # Display email
                    st.write(f"**Business Name:** {business_name}")
                    st.write(f"**University:** {university}")
                    st.write(f"**Business Description:** {business_description}")
                else:
                    st.error("Failed to store information in the database. Please check the logs.")
            else:
                st.error("Please fill in all the required text fields before submitting.")

    st.markdown("---")
    st.subheader("Currently Stored Business Entries:")

    # --- Display Stored Data (for demonstration) ---
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # Select all columns, including 'email'
    c.execute("SELECT name, email, business_name, university, business_description, picture_data FROM student_businesses ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    if rows:
        for i, row in enumerate(rows):
            # Remember the order of columns in 'row' corresponds to your SELECT statement
            # row[0] = name, row[1] = email, row[2] = business_name, etc.
            st.write(f"**Entry {len(rows) - i}:**") # Numbering from newest to oldest
            st.write(f"  - **Name:** {row[0]}")
            st.write(f"  - **Email:** {row[1]}") # Display email
            st.write(f"  - **Business Name:** {row[2]}")
            st.write(f"  - **University:** {row[3]}")
            st.write(f"  - **Description:** {row[4]}")
            if row[5]: # picture_data is now at index 5
                try:
                    image_from_db = Image.open(io.BytesIO(row[5]))
                    # Make sure the caption and use_container_width match the original logic
                    st.image(image_from_db, caption=f"Picture for {row[2]}", width=250) # Use business name for caption
                except Exception as e:
                    st.write(f"  - (Could not display picture for {row[2]}: {e})")
            else:
                st.write("  - (No picture uploaded for this entry)")
            st.markdown("---") # Separator between entries
    else:
        st.info("No business information has been submitted yet.")

if __name__ == "__main__":
    main()