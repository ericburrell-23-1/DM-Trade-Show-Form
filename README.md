# D&M Imaging Visitor Registration App

This is a simple desktop application built with Python and `ttkbootstrap` that allows visitors to register their contact information at D&M Imaging. The app provides a clean and user-friendly interface for entering visitor details, saving them to a CSV file on the user's desktop, and showing a confirmation screen upon successful submission.

## Features

- Modern, themed UI using `ttkbootstrap`
- Form fields for first name, last name, phone number, and email
- Validation and feedback if data fails to save
- Confirmation screen with a friendly message
- Data saved in CSV format to a file named `visitor_data.csv` on the desktop
- Ability to register multiple visitors without restarting the app

## Installation

1. Clone the repository with `git clone`.
2. Navigate into the project directory.
3. Install required dependencies: `ttkbootstrap` and `Pillow`.

## Usage

Run the application by executing the main Python script.

Fill out the visitor form and click "Submit." Upon successful submission, you'll see a confirmation screen. You can register another visitor by clicking "Register Another."

## Project Structure

- `app.py`: The main application script launching the app window.
- `views/`: Contains the GUI page classes (`FormPageView` and `ConfirmationPageView`).
- `assets/`: Contains image assets such as the company logo.
- `visitor_data.csv`: Output CSV file created on the desktop to store visitor data.

## Future Improvements

- Add input validation (e.g., email format, phone number digits).
- Improve error handling and logging.
- Option to export or email visitor data.
- Integrate animation or multimedia feedback.
- Add lightweight database storage for data backup.

## License

This project is open source under the MIT License.
