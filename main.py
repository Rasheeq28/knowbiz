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
#     # IMPORTANT: If you already have data in student_businesses.db,
#     # adding a new column 'email' might require you to:
#     # 1. Delete the old 'student_businesses.db' file (losing existing data).
#     # 2. Or, run an ALTER TABLE command:
#     #    c.execute('ALTER TABLE student_businesses ADD COLUMN email TEXT;')
#     #    You should only run ALTER TABLE once. For simplicity, if this is development,
#     #    it's often easiest to just delete the .db file and let it recreate.
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS student_businesses (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL, -- ADDED: Email field
#             business_name TEXT NOT NULL,
#             university TEXT NOT NULL,
#             business_description TEXT NOT NULL,
#             picture_data BLOB -- Stores the image as binary data
#         )
#     ''')
#     conn.commit()
#     conn.close()
#
# # Updated insert_data to accept 'email'
# def insert_data(name, email, business_name, university, description, picture_bytes):
#     """
#     Inserts a new record into the 'student_businesses' table.
#     """
#     conn = sqlite3.connect(DB_FILE)
#     c = conn.cursor()
#     try:
#         c.execute('''
#             INSERT INTO student_businesses (name, email, business_name, university, business_description, picture_data)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (name, email, business_name, university, description, picture_bytes))
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
#         your_email = st.text_input("Personal Email Address:") # ADDED: Email input
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
#             # Check if all required text fields are filled (including email)
#             if your_name and your_email and business_name and university and business_description:
#                 picture_bytes_to_store = None
#                 if uploaded_picture is not None:
#                     # Read the uploaded image file into bytes for database storage
#                     picture_bytes_to_store = uploaded_picture.read()
#
#                     # Optionally, display the uploaded image for preview before saving
#                     try:
#                         image_preview = Image.open(uploaded_picture)
#                         st.image(image_preview, caption="Uploaded Picture Preview", use_container_width=True)
#                     except Exception as e:
#                         st.warning(f"Could not display image preview: {e}")
#
#                 # Call insert_data with the new 'email' parameter
#                 if insert_data(your_name, your_email, business_name, university, business_description, picture_bytes_to_store):
#                     st.success("Information Submitted Successfully and Stored in Database!")
#                     st.write(f"**Your Name:** {your_name}")
#                     st.write(f"**Your Email:** {your_email}") # Display email
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
#     # Select all columns, including 'email'
#     c.execute("SELECT name, email, business_name, university, business_description, picture_data FROM student_businesses ORDER BY id DESC")
#     rows = c.fetchall()
#     conn.close()
#
#     if rows:
#         for i, row in enumerate(rows):
#             # Remember the order of columns in 'row' corresponds to your SELECT statement
#             # row[0] = name, row[1] = email, row[2] = business_name, etc.
#             st.write(f"**Entry {len(rows) - i}:**") # Numbering from newest to oldest
#             st.write(f"  - **Name:** {row[0]}")
#             st.write(f"  - **Email:** {row[1]}") # Display email
#             st.write(f"  - **Business Name:** {row[2]}")
#             st.write(f"  - **University:** {row[3]}")
#             st.write(f"  - **Description:** {row[4]}")
#             if row[5]: # picture_data is now at index 5
#                 try:
#                     image_from_db = Image.open(io.BytesIO(row[5]))
#                     # Make sure the caption and use_container_width match the original logic
#                     st.image(image_from_db, caption=f"Picture for {row[2]}", width=250) # Use business name for caption
#                 except Exception as e:
#                     st.write(f"  - (Could not display picture for {row[2]}: {e})")
#             else:
#                 st.write("  - (No picture uploaded for this entry)")
#             st.markdown("---") # Separator between entries
#     else:
#         st.info("No business information has been submitted yet.")
#
# if __name__ == "__main__":
#     main()
#
#


# supabase integration
import streamlit as st
from supabase import create_client, Client
import io
from PIL import Image
import uuid  # For generating unique filenames for images

# --- Supabase Configuration ---
# Load secrets from .streamlit/secrets.toml
SUPABASE_URL = "https://udarzmjsmaojceashsld.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkYXJ6bWpzbWFvamNlYXNoc2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk0NzA3MjUsImV4cCI6MjA2NTA0NjcyNX0.d4P1KNfglej-JhvzeFEUYqvfjtwYErsZPzOfMG0pdjI"


# Initialize Supabase client
@st.cache_resource
def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_KEY)


supabase: Client = get_supabase_client()


# --- Database Operations (Supabase) ---

# No init_db() needed for Supabase; tables are created via SQL in Supabase UI/migrations

def upload_image_to_storage(image_bytes: bytes, folder: str = "profile_pictures") -> str | None:
    """Uploads an image to Supabase Storage and returns its public URL."""
    try:
        # Generate a unique filename
        file_extension = Image.open(io.BytesIO(image_bytes)).format.lower()
        if file_extension == 'jpeg':  # PIL might return 'jpeg' for JPG
            file_extension = 'jpg'
        filename = f"{uuid.uuid4()}.{file_extension}"
        filepath = f"{folder}/{filename}"

        # Upload the image
        response = supabase.storage.from_('images').upload(filepath, image_bytes,
                                                           {'content-type': f'image/{file_extension}'})

        if response.status_code == 200:
            # Get the public URL
            public_url_response = supabase.storage.from_('images').get_public_url(filepath)
            return public_url_response
        else:
            st.error(f"Failed to upload image to storage. Status: {response.status_code}, Error: {response.json()}")
            return None
    except Exception as e:
        st.error(f"Error during image upload: {e}")
        return None


def insert_owner_and_business(name, personal_email, business_name, business_email, university, business_description,
                              profile_picture_url):
    """
    Inserts data into 'owners' and 'businesses' tables.
    """
    try:
        # 1. Insert into 'owners' table
        owner_data = {
            "name": name,
            "email": personal_email,
            "university": university,
            "profile_picture_url": profile_picture_url  # This will be the URL from Supabase Storage
        }
        owner_response = supabase.table("owners").insert(owner_data).execute()

        if owner_response.data:
            owner_id = owner_response.data[0]['id']  # Get the ID of the newly created owner

            # 2. Insert into 'businesses' table
            business_data = {
                "owner_id": owner_id,
                "business_name": business_name,
                "business_email": business_email,  # Business contact email
                "business_description": business_description,
                "business_logo_url": profile_picture_url
                # Reusing the same picture for business logo if desired, or add another uploader
            }
            business_response = supabase.table("businesses").insert(business_data).execute()

            if business_response.data:
                return True
            else:
                st.error(f"Supabase Business Insertion Error: {business_response.json()}")
                return False
        else:
            st.error(f"Supabase Owner Insertion Error: {owner_response.json()}")
            return False

    except Exception as e:
        st.error(f"An unexpected error occurred during data insertion: {e}")
        return False


def fetch_all_business_entries():
    """Fetches all business entries along with their owner details from Supabase."""
    try:
        # We need to join businesses with owners to get all display info
        # Supabase's PostgREST allows embedding related data directly.
        # This will fetch businesses and embed the related owner object.
        response = supabase.table("businesses").select("*, owners(*)").order("created_at", desc=True).execute()

        if response.data:
            return response.data
        else:
            st.info("No business information found.")
            return []
    except Exception as e:
        st.error(f"Error fetching data from Supabase: {e}")
        return []


# --- Streamlit App ---
def main():
    st.set_page_config(page_title="Student Business Owners Platform", layout="centered")

    st.title("Business Information Submission")
    st.write("Please fill out the form below with your details.")

    with st.form("business_info_form"):
        # Text Inputs
        your_name = st.text_input("Your Name:")
        your_personal_email = st.text_input("Personal Email Address:")
        business_name = st.text_input("Your Business Name:")
        business_contact_email = st.text_input("Business Email Address:")
        university = st.text_input("Your University:")
        business_description = st.text_area("Small Description of Your Business:")

        # File Uploader for Picture
        uploaded_picture = st.file_uploader("Upload a Picture of you or your Business (JPG or PNG):",
                                            type=["jpg", "png"])

        # Submit Button
        submit_button = st.form_submit_button("Submit Information")

        if submit_button:
            # Check if all required text fields are filled (including both emails)
            if your_name and your_personal_email and business_name and business_contact_email and university and business_description:
                picture_url_to_store = None
                if uploaded_picture is not None:
                    picture_bytes_to_store = uploaded_picture.read()
                    picture_url_to_store = upload_image_to_storage(picture_bytes_to_store)

                    if picture_url_to_store:
                        try:
                            image_preview = Image.open(uploaded_picture)
                            st.image(image_preview, caption="Uploaded Picture Preview", use_container_width=True)
                        except Exception as e:
                            st.warning(f"Could not display image preview: {e}")
                    else:
                        st.error("Image upload failed. Please try again.")
                        st.stop()  # Stop execution if image upload fails

                # Insert data into the database
                if insert_owner_and_business(your_name, your_personal_email, business_name, business_contact_email,
                                             university, business_description, picture_url_to_store):
                    st.success("Information Submitted Successfully and Stored in Database!")
                    st.write(f"**Your Name:** {your_name}")
                    st.write(f"**Personal Email:** {your_personal_email}")
                    st.write(f"**Business Name:** {business_name}")
                    st.write(f"**Business Email:** {business_contact_email}")
                    st.write(f"**University:** {university}")
                    st.write(f"**Business Description:** {business_description}")
                else:
                    st.error("Failed to store information in the database. Please check the logs.")
            else:
                st.error("Please fill in all the required text fields before submitting.")

    st.markdown("---")
    st.subheader("Currently Stored Business Entries:")

    # --- Display Stored Data (from Supabase) ---
    business_entries = fetch_all_business_entries()

    if business_entries:
        for i, entry in enumerate(business_entries):
            # The 'owners' data will be embedded if the select query was `*, owners(*)`
            owner_data = entry.get('owners', {})  # Access the embedded owner data

            st.write(f"**Entry {len(business_entries) - i}:**")
            st.write(f"  - **Owner Name:** {owner_data.get('name', 'N/A')}")
            st.write(f"  - **Personal Email:** {owner_data.get('email', 'N/A')}")
            st.write(f"  - **University:** {owner_data.get('university', 'N/A')}")
            st.write(f"  - **Business Name:** {entry.get('business_name', 'N/A')}")
            st.write(f"  - **Business Email:** {entry.get('business_email', 'N/A')}")
            st.write(f"  - **Description:** {entry.get('business_description', 'N/A')}")

            # Display pictures from their public URLs
            profile_pic_url = owner_data.get('profile_picture_url')
            if profile_pic_url:
                try:
                    st.image(profile_pic_url, caption=f"Picture for {owner_data.get('name', 'Owner')}", width=250)
                except Exception as e:
                    st.write(f"  - (Could not display picture from URL: {e})")
            else:
                st.write("  - (No picture uploaded for this entry)")
            st.markdown("---")  # Separator between entries
    else:
        st.info("No business information has been submitted yet.")


if __name__ == "__main__":
    main()