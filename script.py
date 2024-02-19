import requests
import json

# Base URL for the API
base_url = "https://wgyl9brnpk.execute-api.us-east-1.amazonaws.com/prod"

# Function to make the API call to /login endpoint
def login(username, password):
    login_url = f"{base_url}/login"
    login_data = {"username": username, "password": password}
    login_response = requests.post(login_url, json=login_data)
    login_response.raise_for_status()  # Raise an exception for non-200 responses
    return login_response.json().get("token")

# Function to make the API call to /compliance/posture endpoint
def get_compliance_data(token, time_type, time_amount, time_unit):
    compliance_url = f"{base_url}/compliance/posture"
    headers = {"token": token}
    data = {
        "timeType": time_type,
        "timeAmount": time_amount,
        "timeUnit": time_unit
    }
    compliance_response = requests.get(compliance_url, headers=headers, json=data)
    compliance_response.raise_for_status()  # Raise an exception for non-200 responses
    return compliance_response.json()

# Make the API calls and output the retrieved data
def main():
    # Make login API call
    username = "testuser"
    password = "testpassword"
    token = login(username, password)
    print("Login Successful. Token:", token)

    # Make get_compliance_data API call
    time_type = "relative"
    time_amount = "10"
    time_unit = "hour"
    compliance_data = get_compliance_data(token, time_type, time_amount, time_unit)
    print("Compliance Data:", compliance_data)

if __name__ == "__main__":
    main()