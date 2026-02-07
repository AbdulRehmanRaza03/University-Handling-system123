# University Management System

A comprehensive University Management System built with Streamlit, featuring role-based access for Admin, Faculty, and Students.

## Features

### Admin Dashboard
- Manage Students & Faculty
- Course Management
- Attendance Tracking
- Finance & Fee Collection
- Notices & Announcements

### Faculty Dashboard
- View Classes
- Assignment Management
- Attendance Records
- Exam Management
- Notices

### Student Dashboard
- View Profile
- Course Information
- Assignments
- Attendance Records
- Exam Results
- Notices

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd OOP_Lab
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
streamlit run university_project.py
```

The application will open in your browser at `http://localhost:8501`

## Login Credentials

### Admin
- Username: `admin`
- Password: `admin123`

### Faculty
- Username: `faculty1`
- Password: `fac123`

### Student
- Username: `stud001` or `Abdul`
- Password: `stud123` or `12345`

## Technologies Used

- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **Matplotlib** - Data visualization
- **Streamlit-Lottie** - Animations
- **Requests** - HTTP library

## Project Structure

```
OOP_Lab/
├── university_project.py   # Main application file
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
└── .gitignore             # Git ignore rules
```

## Future Enhancements

- Database integration (MySQL/PostgreSQL)
- Email notifications
- Report generation (PDF)
- Advanced analytics
- Mobile responsive design

## Author

Created as part of OOP Lab coursework

## License

This project is for educational purposes.
