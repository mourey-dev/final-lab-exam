# Installation Guide

## Client Installation

1. Navigate to the `client` directory:
   ```sh
   cd client
   ```
2. Install the required dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```

## Server Installation

1. Navigate to the `server` directory:
   ```sh
   cd server
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the server:
   ```sh
   python manage.py runserver
   ```

## Notes

- Ensure you have Node.js and npm installed for the client setup.
- Ensure you have Python installed for the server setup.
- For database migrations, run:
  ```sh
  python manage.py migrate
  ```