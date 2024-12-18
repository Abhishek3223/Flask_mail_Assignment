

# Flask Wellfound Messaging Web App

This is a simple web application that allows users to send messages to a thread on **Wellfound** (formerly AngelList) using a Python Flask-based backend server. The app includes a minimal front-end UI where users can enter a message and submit it to the specified email.

## Features
- **Flask Backend**: Handles the email sending logic using **Flask-Mail**.
- **Frontend UI**: Allows users to input and submit a message.
- **Simple Setup**: Easy-to-follow setup instructions and a simple user interface.

## Technologies Used
- **Backend**: Flask (Python), Flask-Mail
- **Frontend**: HTML, CSS
- **Environment Variables**: dotenv for managing secrets

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Pip (for installing dependencies)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-link>
   cd <project-folder>
   ```

2. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**
   Create a `.env` file in the root directory and add the following variables:
   ```env
   FLASK_SECRET_KEY=your_secret_key
   EMAIL_USER=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   RECIPIENT_EMAIL=recipient@example.com
   ```

   - `FLASK_SECRET_KEY`: A secret key for Flask sessions and flashing messages.
   - `EMAIL_USER`: Your email address (e.g., a Gmail address).
   - `EMAIL_PASSWORD`: Your email account's password (or app-specific password).
   - `RECIPIENT_EMAIL`: The recipient email address to send messages to.

5. **Run the Flask Server**
   ```bash
   flask run
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage
1. Open the web application in your browser.
2. Enter your message in the provided text box.
3. Click the **Send Message** button to send the email.
4. A success message will appear if the email was successfully sent; otherwise, an error message will be displayed.

## Example Workflow
1. The user enters a message in the message text area.
2. When the user clicks **Send Message**, the message is sent via email to the specified recipient email address using the Gmail SMTP server.
3. The app responds with a success or error message based on whether the email was successfully sent.



