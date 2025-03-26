# E-Voting Website

A secure and user-friendly electronic voting platform built with HTML, CSS, and JavaScript.

## Features

- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and intuitive user interface for easy navigation
- **Secure Voting**: Built with security in mind (to be implemented)
- **Real-time Results**: View election results as they come in (to be implemented)
- **User Authentication**: Secure login and registration system
- **User Management**: Admin panel for managing users

## Project Structure

```
E-voting/
├── public/                # Public-facing files
│   ├── index.html         # Main landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── dashboard.html     # User dashboard
│   ├── assets/            # Static assets
│   │   ├── css/           # CSS stylesheets
│   │   │   ├── styles.css # Main stylesheet
│   │   │   ├── login.css  # Login page styles
│   │   │   ├── register.css # Registration page styles
│   │   │   └── dashboard.css # Dashboard styles
│   │   ├── js/            # JavaScript files
│   │   │   ├── script.js  # Main JavaScript
│   │   │   ├── login.js   # Login functionality
│   │   │   ├── register.js # Registration functionality
│   │   │   └── dashboard.js # Dashboard functionality
│   │   └── images/        # Image assets
└── README.md              # Project documentation
```

## Pages Implemented

- **Home Page**: Landing page with information about the platform
- **Login Page**: User authentication system
- **Registration Page**: New user registration
- **Dashboard**: User dashboard after login with admin controls

## Pages to be Implemented

- **Election Details**: Detailed view of each election
- **Voting Page**: Interface for casting votes
- **Results Page**: Display of election results

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6+)
- Font Awesome (for icons)
- LocalStorage (for client-side database)

## Getting Started

1. Clone the repository
2. Open `public/index.html` in your browser
3. Navigate through the website

## Login Credentials

For testing purposes, you can use the following credentials:

- **Admin**: User ID: `admin123`, Password: `admin123`
- **Voter**: User ID: `voter123`, Password: `voter123`

## Database Management

The application uses browser's localStorage as a client-side database for demonstration purposes:

- **User Management**: Admins can view, edit, and delete users
- **Registration**: New users can register with validation
- **Authentication**: Secure login with session management

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Future Enhancements

- Backend integration with Node.js/Express
- Database integration for storing user data and votes
- Two-factor authentication for enhanced security
- Blockchain technology for vote verification
- Advanced admin panel for election management
- Email verification for new registrations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Font Awesome for the icons
- Google Fonts for typography

---

**Note**: This is a front-end prototype. The user management functionality uses localStorage for demonstration purposes. In a production environment, a proper backend database would be implemented.