import os
import string
import json
import random
import streamlit as st
import google.oauth2.credentials
from google.cloud import aiplatform
from google.cloud import secretmanager
from google.oauth2 import service_account


print(os.environ['HOME'])
st.write(os.environ['HOME'])


code = """
credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
credentials_data = json.loads(credentials_json)
# private_key = credentials_data.pop("private_key")  # Extract private key
project_id = credentials_data.pop("project_id", None)  # Store project ID separately (optional)
credentials = google.oauth2.service_account.Credentials.from_service_account_info(
    credentials_data,
    scopes=None  # Optional: Specify OAuth 2.0 scopes if needed
)
"""

st.code(code, language='python')

credentials_json = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
credentials_data = json.loads(credentials_json)
# private_key = credentials_data.pop("private_key")  # Extract private key
project_id = credentials_data.pop("project_id", None)  # Store project ID separately (optional)
credentials = google.oauth2.service_account.Credentials.from_service_account_info(
    credentials_data,
    scopes=None  # Optional: Specify OAuth 2.0 scopes if needed
)

# Example usage with Vertex AI:


# credentials = google.oauth2.service_account.Credentials.from_service_account_info(json.loads(credentials_json))
# credentials = google.oauth2.credentials.Credentials(**json.loads(credentials_json))


# endpoint = aiplatform.Endpoint(
#     endpoint_name="projects/603505641991/locations/us-central1/endpoints/6876277550390181888"
# )

aiplatform.init(project=project_id, credentials=credentials)  # Use optional project_id if stored
endpoint = aiplatform.Endpoint(endpoint_name="projects/603505641991/locations/us-central1/endpoints/6876277550390181888")
# ... proceed with endpoint operations ...


# def generate_random_string(length):
#     characters = string.ascii_letters + string.digits
#     random_string = ''.join(random.choice(characters) for _ in range(length))
#
#     return random_string

def generate_random_numbers(length):
    # Generate the random numbers
    random_numbers = ''.join(random.choice('0123456789') for _ in range(length))

    return random_numbers

def main():
    # Streamlit app title and expander for defining or updating the knowledge base
    st.title("TEST AutoML deployement")

    ## Inputs
    loan = st.slider("LOAN", 0, 100, key='1001')
    age = st.slider("AGE", 0, 100, key='1002')
    Income = st.slider("INCOME", 0, 100, key='1003')

    # Check if all fields have been filled
    if loan and age and Income:

        if st.button("Get Answer"):
            # Generate Client ID
            ClientID = generate_random_numbers(11)
            st.error(f'Your ID: {ClientID}')
            # Create a dictionary
            data = {
                "loan": str(loan),
                "age": str(age),
                "income": str(Income),
                "ClientID": str(ClientID)
            }
            # Now 'data' is a dictionary that holds your data

            st.json(data)
            ENDPOINT_ID = "4966625964059525120"
            PROJECT_ID = os.getenv("BUILD_SPECIFIC_GCLOUD_PROJECT")

            instance_dict = data
            response = endpoint.predict([instance_dict])

            # print('API response: ', response)
            st.success(f'API response: {response}')
    else:
        st.write("Please fill all the fields.")


# Run the Streamlit app
if __name__ == "__main__":
    main()

# https://meet.google.com/jjb-jpjj-pyy
