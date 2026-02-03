# SMC Road Repair - Copilot Instructions

## Project Overview

This repository contains a mobile-friendly web application for the Solapur Municipal Corporation (SMC) Smart Road Reporting system. It allows citizens to report road damage by uploading photos, capturing GPS location, and providing descriptions. The project is a static HTML application with no backend dependencies.

## Technology Stack

- **HTML5**: Single-page application
- **CSS3**: Inline styles with gradient backgrounds and responsive design
- **Vanilla JavaScript**: For handling image uploads, geolocation, and form submission
- **Target Platform**: Mobile browsers (with desktop support)

## Project Structure

```
smc-road-repair/
├── index.html          # Main application file (contains all HTML, CSS, and JS)
└── README.md           # Project documentation
```

## Key Features

1. **Photo Upload**: Camera/gallery access for capturing road damage images
2. **GPS Location**: Automatic geolocation detection using browser APIs
3. **Image Preview**: Real-time preview of uploaded photos
4. **Responsive Design**: Mobile-first design with desktop compatibility
5. **Form Validation**: Client-side validation before submission

## Build & Development

### Running the Application

**This is a static HTML project with no build steps required.**

To run the application:
1. Simply open `index.html` in a web browser, OR
2. Use a local development server (recommended for testing geolocation):
   ```bash
   # Using Python 3
   python3 -m http.server 8000
   
   # Using Python 2
   python -m SimpleHTTPServer 8000
   
   # Using Node.js (if http-server is installed)
   npx http-server -p 8000
   ```
3. Access the application at `http://localhost:8000` (or open `index.html` directly)

**Note**: Geolocation features require HTTPS in production or localhost for testing due to browser security restrictions.

### Testing

**There are currently no automated tests in this repository.**

Manual testing should include:
- Photo upload functionality (both camera and gallery)
- GPS location detection
- Image preview rendering
- Form submission
- Responsive layout on different screen sizes
- Browser compatibility (Chrome, Safari, Firefox mobile browsers)

### Linting & Code Quality

**There are no linters or code quality tools configured.**

When making changes:
- Follow the existing code style (indentation, naming conventions)
- Ensure HTML is valid
- Test JavaScript functionality in multiple browsers
- Validate CSS for responsive behavior

## Making Changes

### HTML Changes
- All HTML is in `index.html`
- The structure is semantic with proper form elements
- Maintain mobile-first responsive design principles

### CSS Changes
- All styles are inline within the `<style>` tag in `index.html`
- The design uses CSS Grid/Flexbox for layout
- Color scheme: Purple gradient primary (#667eea to #764ba2)
- Maintain the existing design system (border-radius, shadows, transitions)

### JavaScript Changes
- All JavaScript is inline within the `<script>` tag in `index.html`
- Uses vanilla JavaScript (no frameworks or libraries)
- Key functions:
  - `getLocation()`: Handles GPS detection
  - Image upload event listeners
  - Form submission handler
- Always test geolocation features on HTTPS or localhost

## Common Gotchas

1. **Geolocation Permissions**: Browser will prompt for location access; this requires HTTPS or localhost
2. **File Input on Mobile**: The `capture="environment"` attribute opens the camera directly on mobile
3. **No Backend**: Form currently just shows an alert on submission; integrating with a backend will require AJAX/fetch API
4. **Browser Compatibility**: Always test geolocation and file upload on target mobile browsers

## Validation Steps

Before committing changes:
1. Open `index.html` in a browser to ensure it renders correctly
2. Test photo upload functionality
3. Verify geolocation detection works (may need localhost server)
4. Check responsive design on mobile viewport (use browser dev tools)
5. Ensure form submission still works
6. Validate no JavaScript console errors appear

## Future Enhancements

The application is currently a frontend prototype. Future work may include:
- Backend API integration for storing reports
- Database for road damage records
- Admin dashboard for viewing reports
- AI-powered damage classification
- Integration with municipal management systems

## Important Notes for Copilot Coding Agent

- **No build process**: Do not add unnecessary build tools or package managers unless specifically requested
- **Keep it simple**: This is intentionally a single-file application for easy deployment
- **Mobile-first**: Always consider mobile user experience when making changes
- **Test locally**: Use a local server for testing geolocation features
- **Preserve styling**: Maintain the existing purple gradient theme and modern UI design
- **No dependencies**: Keep the project dependency-free unless absolutely necessary
