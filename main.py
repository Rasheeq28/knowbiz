# import streamlit as st
#
# st.set_page_config(page_title="Business Owner Form", page_icon="🔥")
#
# st.title("📋 Student Business Owner Submission Form")
#
# # Form
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#
#     st.subheader("🏪 Business Information")
#     business_name = st.text_input("Name of your Business")
#     business_description = st.text_area("Business Description")
#
#     fb_link = st.text_input("Facebook Page Link")
#     insta_link = st.text_input("Instagram Profile Link")
#
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# # On Submit
# if submitted:
#     st.success("✅ Form submitted successfully!")
#
#     # Display entered data (optional)
#     st.write("### Submitted Info:")
#     st.write("**Owner Name:**", owner_name or "Not provided")
#     st.write("**Email:**", owner_email or "Not provided")
#     st.write("**University:**", university or "Not provided")
#     st.write("**Business Name:**", business_name or "Not provided")
#     st.write("**Description:**", business_description or "Not provided")
#     st.write("**Facebook Link:**", fb_link or "Not provided")
#     st.write("**Instagram Link:**", insta_link or "Not provided")
#
#     if profile_pic:
#         st.image(profile_pic, caption="Uploaded Profile Picture", use_container_width=True)
#     else:
#         st.write("No profile picture uploaded.")


# supabase integration
# import streamlit as st
# from supabase import create_client, Client
# import time
# import uuid
#
# # Supabase credentials
# SUPABASE_URL = "https://udarzmjsmaojceashsld.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkYXJ6bWpzbWFvamNlYXNoc2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk0NzA3MjUsImV4cCI6MjA2NTA0NjcyNX0.d4P1KNfglej-JhvzeFEUYqvfjtwYErsZPzOfMG0pdjI"
#
# # Supabase init
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.set_page_config(page_title="Business Owner Form", page_icon="🔥")
#
# st.title("📋 Student Business Owner Submission Form")
#
# # Form
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# # Submit logic
# if submitted:
#     # Step 1: Upload profile pic (if exists)
#     profile_url = None
#     if profile_pic:
#         file_extension = profile_pic.name.split(".")[-1]
#         unique_name = f"{str(uuid.uuid4())}.{file_extension}"
#         storage_path = f"owner_profiles/{unique_name}"
#
#         # Upload image to storage bucket (public)
#         res = supabase.storage().from_("public").upload(storage_path, profile_pic.read(), {"content-type": profile_pic.type})
#
#         if res.status_code == 200:
#             # Get the public URL
#             profile_url = supabase.storage().from_("public").get_public_url(storage_path)
#         else:
#             st.warning("⚠️ Failed to upload image.")
#
#     # Step 2: Insert into Supabase table
#     data = {
#         "owner_name": owner_name,
#         "owner_email": owner_email,
#         "university": university,
#         "profile_pic": profile_url  # can be None if not uploaded
#     }
#
#
#     insert_res = supabase.table("owner_table").insert(data).execute()
#
#     if insert_res.data is not None:
#         st.success("✅ Form submitted and saved to Supabase!")
#         st.write("### Submitted Info:")
#         st.write("**Owner Name:**", owner_name or "Not provided")
#         st.write("**Email:**", owner_email or "Not provided")
#         st.write("**University:**", university or "Not provided")
#         if profile_url:
#             st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#         else:
#             st.write("No profile picture uploaded.")
#     else:
#         st.error("❌ Failed to submit data to Supabase.")


# profile pic fixing
# import streamlit as st
# from supabase import create_client, Client
# import uuid
# import io
#
# # Supabase credentials
# SUPABASE_URL = "https://udarzmjsmaojceashsld.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkYXJ6bWpzbWFvamNlYXNoc2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk0NzA3MjUsImV4cCI6MjA2NTA0NjcyNX0.d4P1KNfglej-JhvzeFEUYqvfjtwYErsZPzOfMG0pdjI"
#
# # Initialize Supabase client
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.set_page_config(page_title="Business Owner Form", page_icon="🔥")
# st.title("📋 Student Business Owner Submission Form")
#
# # Form
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# if submitted:
#     profile_url = None
#     if profile_pic:
#         try:
#             # Prepare file bytes and reset pointer
#             file_bytes = profile_pic.read()
#             profile_pic.seek(0)
#             file_like = io.BytesIO(file_bytes)
#
#             # Generate unique file name and storage path
#             file_extension = profile_pic.name.split(".")[-1]
#             unique_name = f"{str(uuid.uuid4())}.{file_extension}"
#             storage_path = f"owner_profiles/{unique_name}"
#
#             # Upload to Supabase storage bucket named "public"
#             res = supabase.storage.from_("public").upload(storage_path, file_bytes, {"content-type": profile_pic.type})
#
#             # Check upload result
#             if hasattr(res, "status_code") and res.status_code == 200:
#                 profile_url = supabase.storage().from_("public").get_public_url(storage_path).public_url
#             else:
#                 st.warning("⚠️ Failed to upload image. Please try again.")
#         except Exception as e:
#             st.error(f"⚠️ Error uploading image: {e}")
#
#     # Prepare data to insert
#     data = {
#         "owner_name": owner_name or None,
#         "owner_email": owner_email or None,
#         "university": university or None,
#         "profile_pic": profile_url  # can be None if no upload
#     }
#
#     try:
#         insert_res = supabase.table("owner_table").insert(data).execute()
#         if insert_res.data is not None:
#             st.success("✅ Form submitted and saved to Supabase!")
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**Email:**", owner_email or "Not provided")
#             st.write("**University:**", university or "Not provided")
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             else:
#                 st.write("No profile picture uploaded.")
#         else:
#             st.error("❌ Failed to submit data to Supabase.")
#             st.write(insert_res)
#     except Exception as e:
#         st.error(f"❌ Error saving data: {e}")


# pic02
# import streamlit as st
# from supabase import create_client, Client
# import time
# import uuid
#
# # Supabase credentials
# SUPABASE_URL = "https://udarzmjsmaojceashsld.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVkYXJ6bWpzbWFvamNlYXNoc2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk0NzA3MjUsImV4cCI6MjA2NTA0NjcyNX0.d4P1KNfglej-JhvzeFEUYqvfjtwYErsZPzOfMG0pdjI"
#
# # Supabase init
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.set_page_config(page_title="Business Owner Form", page_icon="🔥")
# st.title("📋 Student Business Owner Submission Form")
#
# # Form
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# # Submit logic
# if submitted:
#     profile_url = None
#
#     # Step 1: Upload profile pic to 'picbucket'
#     if profile_pic:
#         file_extension = profile_pic.name.split(".")[-1]
#         unique_name = f"{str(uuid.uuid4())}.{file_extension}"
#         storage_path = f"owner_profiles/{unique_name}"
#
#         try:
#             # Upload to 'picbucket'
#             res = supabase.storage.from_("picbucket").upload(
#                 storage_path,
#                 profile_pic.read(),
#                 {"content-type": profile_pic.type}
#             )
#
#             if res.status_code == 200:
#                 profile_url = supabase.storage.from_("picbucket").get_public_url(storage_path)
#             else:
#                 st.warning(f"⚠️ Error uploading image: {res.data}")
#         except Exception as e:
#             st.warning(f"⚠️ Error uploading image: {e}")
#
#     # Step 2: Insert into Supabase table
#     try:
#         data = {
#             "owner_name": owner_name,
#             "owner_email": owner_email,
#             "university": university,
#             "profile_pic": profile_url  # can be None if not uploaded
#         }
#
#         insert_res = supabase.table("owner_table").insert(data).execute()
#
#         if insert_res.data is not None:
#             st.success("✅ Form submitted and saved to Supabase!")
#
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**Email:**", owner_email or "Not provided")
#             st.write("**University:**", university or "Not provided")
#
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             else:
#                 st.write("No profile picture uploaded.")
#
#         else:
#             st.error("❌ Failed to submit data to Supabase.")
#
#     except Exception as e:
#         st.error(f"❌ Supabase error: {e}")


# secured
# import streamlit as st
# from supabase import create_client, Client
# import uuid
#
# # Load .env variables
# url = st.secrets["supabase"]["url"]
# key = st.secrets["supabase"]["key"]
# bucket = st.secrets["supabase"]["bucket"]
#
# supabase = create_client(url, key)
#
# st.set_page_config(page_title="Business Owner Form", page_icon="🔥")
# st.title("📋 Student Business Owner Submission Form")
#
# # Form
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# # Submit logic
# if submitted:
#     profile_url = None
#
#     # Step 1: Upload profile pic to 'picbucket'
#     if profile_pic:
#         file_extension = profile_pic.name.split(".")[-1]
#         unique_name = f"{str(uuid.uuid4())}.{file_extension}"
#         storage_path = f"owner_profiles/{unique_name}"
#
#         try:
#             # Upload to 'picbucket'
#             res = supabase.storage.from_("picbucket").upload(
#                 storage_path,
#                 profile_pic.read(),
#                 {"content-type": profile_pic.type}
#             )
#
#             if res.status_code == 200:
#                 profile_url = supabase.storage.from_("picbucket").get_public_url(storage_path)
#             else:
#                 st.warning(f"⚠️ Error uploading image: {res.data}")
#         except Exception as e:
#             st.warning(f"⚠️ Error uploading image: {e}")
#
#     # Step 2: Insert into Supabase table
#     try:
#         data = {
#             "owner_name": owner_name,
#             "owner_email": owner_email,
#             "university": university,
#             "profile_pic": profile_url  # can be None if not uploaded
#         }
#
#         insert_res = supabase.table("owner_table").insert(data).execute()
#
#         if insert_res.data is not None:
#             st.success("✅ Form submitted and saved to Supabase!")
#
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**Email:**", owner_email or "Not provided")
#             st.write("**University:**", university or "Not provided")
#
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             else:
#                 st.write("No profile picture uploaded.")
#
#         else:
#             st.error("❌ Failed to submit data to Supabase.")
#
#     except Exception as e:
#         st.error(f"❌ Supabase error: {e}")

# pic fix, owner form and table works
# import streamlit as st
# from supabase import create_client
# import uuid
#
# # Supabase credentials
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# BUCKET_NAME = st.secrets["supabase"]["bucket"]
#
# # Initialize supabase client
# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("📋 Student Business Owner Submission Form")
#
# with st.form("business_form"):
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# if submitted:
#     profile_url = None
#
#     if profile_pic:
#         file_extension = profile_pic.name.split(".")[-1]
#         unique_filename = f"{uuid.uuid4()}.{file_extension}"
#         storage_path = f"owner_profiles/{unique_filename}"
#
#         try:
#             file_bytes = profile_pic.read()
#
#             upload_response = supabase.storage.from_(BUCKET_NAME).upload(
#                 path=storage_path,
#                 file=file_bytes,
#                 file_options={"content-type": profile_pic.type},
#             )
#
#             # upload_response is just a response object, no .error or .status_code
#             # If no exception, assume success
#             st.success("Profile picture uploaded successfully!")
#
#             # get_public_url returns a string URL
#             profile_url = supabase.storage.from_(BUCKET_NAME).get_public_url(storage_path)
#
#         except Exception as e:
#             st.error(f"⚠️ Error uploading image: {e}")
#
#     data = {
#         "owner_name": owner_name,
#         "owner_email": owner_email,
#         "university": university,
#         "profile_pic": profile_url,  # can be None
#     }
#
#     try:
#         insert_response = supabase.table("owner_table").insert(data).execute()
#
#         if insert_response.data and len(insert_response.data) > 0:
#             st.success("✅ Form submitted and saved to Supabase!")
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**Email:**", owner_email or "Not provided")
#             st.write("**University:**", university or "Not provided")
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             else:
#                 st.write("No profile picture uploaded.")
#         else:
#             st.error(f"❌ Insert failed. Response: {insert_response}")
#
#     except Exception as e:
#         st.error(f"❌ Error inserting data: {e}")
#


# busjness form included
# import streamlit as st
# from supabase import create_client
# import uuid
#
# # Supabase credentials
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# BUCKET_NAME = st.secrets["supabase"]["bucket"]
#
# # Initialize supabase client
# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("📋 Student Business Owner Submission Form")
#
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     st.subheader("🏢 Business Information")
#     business_name = st.text_input("Business Name")
#     business_description = st.text_area("Business Description")
#     business_logo = st.file_uploader("Upload a Business Logo/Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
#     facebook_url = st.text_input("Facebook URL (optional)")
#     instagram_url = st.text_input("Instagram URL (optional)")
#     website_url = st.text_input("Website URL (optional)")
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# def upload_to_supabase(file, folder):
#     try:
#         file_extension = file.name.split(".")[-1]
#         unique_filename = f"{uuid.uuid4()}.{file_extension}"
#         storage_path = f"{folder}/{unique_filename}"
#         file_bytes = file.read()
#
#         supabase.storage.from_(BUCKET_NAME).upload(
#             path=storage_path,
#             file=file_bytes,
#             file_options={"content-type": file.type},
#         )
#         return supabase.storage.from_(BUCKET_NAME).get_public_url(storage_path)
#     except Exception as e:
#         st.error(f"⚠️ Error uploading image: {e}")
#         return None
#
# if submitted:
#     profile_url = upload_to_supabase(profile_pic, "owner_profiles") if profile_pic else None
#     logo_url = upload_to_supabase(business_logo, "business_logos") if business_logo else None
#
#     data = {
#         "owner_name": owner_name,
#         "owner_email": owner_email,
#         "university": university,
#         "profile_pic": profile_url,
#         "business_name": business_name,
#         "business_description": business_description,
#         "business_logo": logo_url,
#         "facebook_url": facebook_url,
#         "instagram_url": instagram_url,
#         "website_url": website_url,
#     }
#
#     try:
#         insert_response = supabase.table("owner_table").insert(data).execute()
#         if insert_response.data and len(insert_response.data) > 0:
#             st.success("✅ Form submitted and saved to Supabase!")
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**University:**", university or "Not provided")
#             st.write("**Business Name:**", business_name or "Not provided")
#             st.write("**Business Description:**", business_description or "Not provided")
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             if logo_url:
#                 st.image(logo_url, caption="Business Logo", use_container_width=True)
#         else:
#             st.error(f"❌ Insert failed. Response: {insert_response}")
#     except Exception as e:
#         st.error(f"❌ Error inserting data: {e}")

# b.email
# import streamlit as st
# from supabase import create_client
# import uuid
#
# # Supabase credentials
# SUPABASE_URL = st.secrets["supabase"]["url"]
# SUPABASE_KEY = st.secrets["supabase"]["key"]
# BUCKET_NAME = st.secrets["supabase"]["bucket"]
#
# # Initialize supabase client
# supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
#
# st.title("📋 Student Business Owner Submission Form")
#
# with st.form("business_form"):
#     st.subheader("👤 Owner Information")
#     owner_name = st.text_input("Your Name")
#     owner_email = st.text_input("Your Email")
#     university = st.text_input("University")
#     profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])
#
#     st.subheader("🏢 Business Information")
#     business_name = st.text_input("Business Name")
#     business_email = st.text_input("Business Email")
#     business_description = st.text_area("Business Description")
#     business_logo = st.file_uploader("Upload a Business Logo/Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
#     facebook_url = st.text_input("Facebook URL (optional)")
#     instagram_url = st.text_input("Instagram URL (optional)")
#     website_url = st.text_input("Website URL (optional)")
#
#     submitted = st.form_submit_button("🚀 Submit")
#
# def upload_to_supabase(file, folder):
#     try:
#         file_extension = file.name.split(".")[-1]
#         unique_filename = f"{uuid.uuid4()}.{file_extension}"
#         storage_path = f"{folder}/{unique_filename}"
#         file_bytes = file.read()
#
#         supabase.storage.from_(BUCKET_NAME).upload(
#             path=storage_path,
#             file=file_bytes,
#             file_options={"content-type": file.type},
#         )
#         return supabase.storage.from_(BUCKET_NAME).get_public_url(storage_path)
#     except Exception as e:
#         st.error(f"⚠️ Error uploading image: {e}")
#         return None
#
# if submitted:
#     profile_url = upload_to_supabase(profile_pic, "owner_profiles") if profile_pic else None
#     logo_url = upload_to_supabase(business_logo, "business_logos") if business_logo else None
#
#     data = {
#         "owner_name": owner_name,
#         "owner_email": owner_email,
#         "university": university,
#         "profile_pic": profile_url,
#         "business_name": business_name,
#         "business_email": business_email,
#         "business_description": business_description,
#         "business_logo": logo_url,
#         "facebook_url": facebook_url,
#         "instagram_url": instagram_url,
#         "website_url": website_url,
#     }
#
#     try:
#         insert_response = supabase.table("owner_table").insert(data).execute()
#         if insert_response.data and len(insert_response.data) > 0:
#             st.success("✅ Form submitted and saved to Supabase!")
#             st.write("### Submitted Info:")
#             st.write("**Owner Name:**", owner_name or "Not provided")
#             st.write("**University:**", university or "Not provided")
#             st.write("**Business Name:**", business_name or "Not provided")
#             st.write("**Business Email:**", business_email or "Not provided")
#             st.write("**Business Description:**", business_description or "Not provided")
#             if profile_url:
#                 st.image(profile_url, caption="Uploaded Profile Picture", use_container_width=True)
#             if logo_url:
#                 st.image(logo_url, caption="Business Logo", use_container_width=True)
#         else:
#             st.error(f"❌ Insert failed. Response: {insert_response}")
#     except Exception as e:
#         st.error(f"❌ Error inserting data: {e}")
#


# ot bt creation + foreign key reln
import streamlit as st
from supabase import create_client
import uuid

# Supabase credentials
SUPABASE_URL = st.secrets["supabase"]["url"]
SUPABASE_KEY = st.secrets["supabase"]["key"]
BUCKET_NAME = st.secrets["supabase"]["bucket"]

# Initialize supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("📋 Student Business Owner Submission Form")

with st.form("business_form"):
    st.subheader("👤 Owner Information")
    owner_name = st.text_input("Your Name")
    owner_email = st.text_input("Your Email")
    university = st.text_input("University")
    profile_pic = st.file_uploader("Upload a Profile Picture (JPG/PNG)", type=["jpg", "jpeg", "png"])

    st.subheader("🏢 Business Information")
    business_name = st.text_input("Business Name")
    business_email = st.text_input("Business Email")
    business_description = st.text_area("Business Description")
    business_logo = st.file_uploader("Upload a Business Logo/Image (JPG/PNG)", type=["jpg", "jpeg", "png"])
    facebook_url = st.text_input("Facebook URL (optional)")
    instagram_url = st.text_input("Instagram URL (optional)")
    website_url = st.text_input("Website URL (optional)")

    submitted = st.form_submit_button("🚀 Submit")

def upload_to_supabase(file, folder):
    try:
        file_extension = file.name.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        storage_path = f"{folder}/{unique_filename}"
        file_bytes = file.read()

        supabase.storage.from_(BUCKET_NAME).upload(
            path=storage_path,
            file=file_bytes,
            file_options={"content-type": file.type},
        )
        return supabase.storage.from_(BUCKET_NAME).get_public_url(storage_path)
    except Exception as e:
        st.error(f"⚠️ Error uploading image: {e}")
        return None

if submitted:
    profile_url = upload_to_supabase(profile_pic, "owner_profiles") if profile_pic else None
    logo_url = upload_to_supabase(business_logo, "business_logos") if business_logo else None

    # Insert only owner-related data
    owner_data = {
        "owner_name": owner_name,
        "owner_email": owner_email,
        "university": university,
        "profile_pic": profile_url,
    }

    try:
        owner_insert = supabase.table("owner_table").insert(owner_data).execute()

        if owner_insert.data and len(owner_insert.data) > 0:
            owner_id = owner_insert.data[0]["id"]

            # Insert business data using the correct owner_id
            business_data = {
                "owner_id": owner_id,
                "business_name": business_name,
                "business_email": business_email,
                "business_description": business_description,
                "business_logo": logo_url,
                "facebook_url": facebook_url,
                "instagram_url": instagram_url,
                "website_url": website_url,
            }

            business_insert = supabase.table("business_table").insert(business_data).execute()

            if business_insert.data and len(business_insert.data) > 0:
                st.success("✅ Owner and Business info submitted successfully!")
                st.write("### Submitted Info:")
                st.write("**Owner Name:**", owner_name)
                st.write("**University:**", university)
                st.write("**Business Name:**", business_name)
                st.write("**Business Email:**", business_email)
                if profile_url:
                    st.image(profile_url, caption="Owner Profile Picture", use_container_width=True)
                if logo_url:
                    st.image(logo_url, caption="Business Logo", use_container_width=True)
            else:
                st.error(f"❌ Failed to insert business info. Response: {business_insert}")
        else:
            st.error("❌ Failed to insert owner info.")
    except Exception as e:
        st.error(f"❌ Error inserting data: {e}")
