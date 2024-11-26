import streamlit as st
import joblib

# Load the model
phish_model = joblib.load('phishing.pkl')

# Streamlit application
def main():
    # Add a cover photo with a specific width
    st.image("p.jpg", width=700)  # Ensure you have a p.jpg in your working directory

    # Sidebar for navigation or additional information
    st.sidebar.title("Navigation")
    st.sidebar.write("Use this app to detect phishing websites.")
    
    # Use markdown to style the title and description
    st.markdown("<h1 style='color: cyan;'>Phishing Site Detection</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: lightblue;'>Enter the features of the website to check if it's a phishing site or not.</h3>", unsafe_allow_html=True)

    # Input features
    features = st.text_input("Enter features (comma-separated):", "")
    
    if st.button("Predict"):
        if features:
            # Prepare the input for prediction
            X_predict = [features]  # Wrap the input string in a list
            
            # Perform prediction
            y_predict = phish_model.predict(X_predict)
            
            # Display the result with colors
            if y_predict[0] == 'bad':
                st.markdown("<h2 style='color: red; font-weight: bold;'>🚨 This is a Phishing Site 🚨</h2>", unsafe_allow_html=True)
            else:
                st.markdown("<h2 style='color: green; font-weight: bold;'>✅ This is not a Phishing Site ✅</h2>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter the features.")

    # Security Tips Section
    st.markdown("<h3 style='color: orange;'>🔒 Security Tips to Avoid Phishing:</h3>", unsafe_allow_html=True)
    st.markdown("""
        <ul style='color: white;'>
            <li>Always check the URL before clicking on links. Look for misspellings or unusual domain names.</li>
            <li>Be cautious with emails or messages that create a sense of urgency, especially those asking for personal information.</li>
            <li>Verify the sender's email address. Phishers often use addresses that look similar to legitimate ones.</li>
            <li>Do not enter sensitive information on websites that do not have a secure connection (look for HTTPS in the URL).</li>
            <li>Keep your software, browser, and security tools up to date to protect against the latest threats.</li>
            <li>Use two-factor authentication (2FA) wherever possible for an extra layer of security.</li>
            <li>Educate yourself about common phishing tactics and be skeptical of unsolicited communications.</li>
        </ul>
    """, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
