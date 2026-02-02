# DEPLOYMENT & MOBILE ACCESS PROTOCOLS

## 📱 OPTION 1: INSTANT LOCAL ACCESS (Testing)
**Requirement:** Your phone and computer must be on the **SAME Wi-Fi network**.

1.  **System Frequency (IP Address):** `192.168.12.212`
2.  **Port:** `8501`
3.  **Mobile Link:** 
    Open your Android browser and type:
    👉 **`http://192.168.12.212:8501`**

*Note: If this times out, check your computer's firewall settings to allow incoming connections on port 8501.*

## ☁️ OPTION 2: GLOBAL DEPLOYMENT (Public Release)
To make the app accessible from *anywhere* (not just your home Wi-Fi), you need to deploy it to the cloud.

### Step 1: Push to GitHub
1.  Create a GitHub repository.
2.  Upload `app.py`, `utils.py`, `auth.py`, `style.css`, and `requirements.txt`.

### Step 2: Streamlit Community Cloud (Free)
1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Login with GitHub.
3.  Click "New App".
4.  Select your repository and branch.
5.  Main file path: `app.py`.
6.  Click **Deploy**.

The system will give you a public URL (e.g., `https://decoherence-log.streamlit.app`) that works on any device, anywhere in the multiverse.
