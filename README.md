# Book Search Web Application

## Hosted Version

The web application is publicly hosted and available at:

**https://flask-api-project-cgq2.onrender.com/**

You can access the fully running version online without installing anything locally.

---

## A. Project Overview

This is an interactive Flask web application that allows users to search for books using the OpenLibrary API. Users can search by book title, author name, or subject/topic, and view detailed information about each book including cover images, publication details, ISBNs, and more.

**Topic Area:** Books and Literature  
**API Used:** [OpenLibrary Search API](https://openlibrary.org/developers/api)

The application demonstrates modern web development practices including form handling, API integration, data transformation, and responsive design.

---

## B. Technologies Used

### Backend
- **Python:** 3.11
- **Flask:** 3.0.0 - Web framework for routing and request handling
- **Flask-WTF:** 1.2.1 - Form validation and CSRF protection
- **WTForms:** 3.1.1 - Form field definitions and validators
- **Requests:** 2.31.0 - HTTP library for API calls
- **Python-dotenv:** 1.0.0 - Environment variable management

### Frontend
- **Bootstrap 5.3:** Responsive CSS framework (via CDN)
- **Font Awesome 6.4:** Icon library (via CDN)
- **Jinja2:** Template engine (included with Flask)
- **Custom CSS:** Additional styling for enhanced user experience

---

## C. Setup & Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Internet connection (for API calls)

### Installation Steps

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone https://github.com/mlopIT/Book-Search-Web-Application
   cd Book-Search-Web-Application
   
   # Or extract the ZIP file and navigate to the project directory
   ```

2. **Create a Virtual Environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables** (Optional)
   
   Copy the example environment file:
   ```bash
   cp .env
   ```
   
   Edit `.env` file if needed:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=anything_here_if_you_want  # Not required for local use
   ```
   
   **Note:** The OpenLibrary API does not require an API key.

5. **Run the Application**
   
   Option 1 - Using Flask CLI:
   ```bash
   flask run
   ```
   
   Option 2 - Using Python directly:
   ```bash
   python app.py
   ```

6. **Access the Application**
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## D. Usage Instructions

### Accessing the Application
1. Start the Flask application using the instructions above
2. Open `http://127.0.0.1:5000/` in your web browser
3. You will see the main search form

### Form Fields Explained

1. **Search Query** (Required, Text Field)
   - Enter your search term here
   - Examples: "Harry Potter", "Stephen King", "Science Fiction"
   - Must be 1-200 characters long

2. **Search By** (Required, Dropdown Selection)
   - Choose how you want to search:
     - **Book Title:** Search by the book's title
     - **Author Name:** Search by author's name
     - **Subject/Topic:** Search by genre or subject
   - Default: Book Title

3. **Number of Results** (Required, Number Field)
   - Specify how many results you want to see
   - Range: 1-20 results
   - Default: 10 results

### Example Searches

**By Title:**
- Search Query: "The Great Gatsby"
- Search By: Book Title
- Number of Results: 10

**By Author:**
- Search Query: "J.K. Rowling"
- Search By: Author Name
- Number of Results: 15

**By Subject:**
- Search Query: "Mystery"
- Search By: Subject/Topic
- Number of Results: 20

### Results Page Output

After submitting the form, the results page displays:

1. **Search Summary:**
   - Your search query
   - Search type used
   - Total number of books found in the database
   - Number of results displayed

2. **Book Information** (for each result):
   - Book cover image (if available)
   - Title
   - Author(s)
   - First publication year
   - Publication year range (span across all editions)
   - Total number of editions available
   - ISBN (sample from one edition)
   - Language(s)
   - Subject tags (up to 5)
   - Link to view full details on OpenLibrary

3. **Navigation:**
   - "New Search" button to return to the search form
   - "View on OpenLibrary" links for detailed information

---

## E. API Description

### API Name
**OpenLibrary Search API**

### Main Endpoints Used
- **Base URL:** `https://openlibrary.org/search.json`
- **Cover Images:** `https://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg`

### API Parameters

The application uses the following parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `title` | Search by book title | `title=Harry+Potter` |
| `author` | Search by author name | `author=J.K.+Rowling` |
| `subject` | Search by subject/topic | `subject=Fantasy` |
| `limit` | Max number of results | `limit=10` |
| `fields` | Specify which fields to return | `fields=key,title,author_name,...` |

### Form Input to API Mapping

1. **Search Query + Search Type:**
   - If "Book Title" selected: `title={search_query}`
   - If "Author Name" selected: `author={search_query}`
   - If "Subject/Topic" selected: `subject={search_query}`

2. **Number of Results:**
   - Maps to: `limit={result_limit}`

### API Response Format
The API returns JSON with the following structure:
```json
{
  "numFound": 1000,
  "docs": [
    {
      "title": "Book Title",
      "author_name": ["Author Name"],
      "first_publish_year": 2000,
      "edition_count": 25,
      "publish_year": [2000, 2001, 2005, 2010],
      "isbn": ["1234567890"],
      "subject": ["Fiction", "Adventure"],
      "cover_i": 12345,
      "language": ["eng"]
    }
  ]
}
```

### Rate Limits and Caveats
- **No API Key Required:** The OpenLibrary API is completely free
- **Rate Limiting:** The API has rate limits, but they are generous for normal use
- **User-Agent Header:** The application sends a User-Agent header for good API citizenship
- **Timeout:** API requests timeout after 10 seconds to prevent hanging
- **Data Availability:** Not all books have complete information (covers, ISBNs, etc.)
- **Publisher Data:** The API aggregates publishers across all editions (80+ publishers for popular books), so we display edition count and publication year range instead for accuracy

---

## F. Additional Features / Enhancements

### Error Handling
- **API Timeout:** Displays user-friendly message if API takes too long
- **Network Errors:** Catches connection issues and displays appropriate error
- **Invalid Responses:** Handles malformed JSON responses gracefully
- **No Results:** Shows helpful suggestions when no books are found
- **Form Validation:** Real-time validation with helpful error messages
- **Missing Data:** Handles books with incomplete information (no cover, no ISBN, etc.)

### Styling and User Experience
- **Bootstrap 5 Framework:** Modern, responsive design that works on all devices
- **Custom CSS:** Enhanced visual styling for better aesthetics
- **Font Awesome Icons:** Visual icons throughout the interface
- **Card-Based Layout:** Clean, organized presentation of book information
- **Hover Effects:** Interactive elements with smooth transitions
- **Flash Messages:** Alert system for user feedback
- **Loading States:** Visual feedback during form submission
- **Mobile Responsive:** Fully functional on smartphones and tablets

### Extra Features
- **Cover Image Display:** Shows book covers with fallback for missing images
- **External Links:** Direct links to OpenLibrary for more details
- **Example Searches:** Helpful suggestions on the main page
- **Search Summary:** Clear display of what was searched and how many results
- **Edition Information:** Shows total editions available and publication year range
- **Multiple Languages:** Shows all available language information
- **Subject Tags:** Displays relevant topics and genres
- **Data Accuracy:** Prioritizes accurate, edition-specific information over aggregated data

---

## G. Project Requirements Mapping

This project fulfills all the assignment requirements as follows:

### 1. API Integration ✅
- **Requirement:** Use API that provides JSON/XML data
- **Implementation:** OpenLibrary Search API (JSON format)
- **Location:** `app.py` - `fetch_books()` function

### 2. Flask Web Application ✅
- **Requirement:** Set up Flask with proper routing
- **Implementation:** 
  - Main route: `/` (GET, POST)
  - Results route: `/results` (POST)
- **Location:** `app.py` - route decorators

### 3. HTML Form Page ✅
- **Requirement:** HTML file for collecting user inputs
- **Implementation:** Search form with three fields
- **Location:** `templates/index.html`

### 4. Form Fields (Minimum 3) ✅
- **Requirement:** At least three form fields with validation
- **Implementation:**
  1. **StringField:** Search Query (with length validation)
  2. **SelectField:** Search Type (title/author/subject)
  3. **IntegerField:** Result Limit (with range validation 1-20)
- **Location:** `forms.py` - `BookSearchForm` class

### 5. Flask-WTF Form Handling ✅
- **Requirement:** Use Flask-WTF for validation
- **Implementation:** Form class with validators
- **Location:** `forms.py`

### 6. Form Submission Route ✅
- **Requirement:** Flask route to handle POST submissions
- **Implementation:** `index()` function handles POST method
- **Location:** `app.py` - line 92-129

### 7. Fetch Data from API ✅
- **Requirement:** Use user input to query API with requests library
- **Implementation:** `fetch_books()` function with dynamic parameters
- **Location:** `app.py` - line 29-65

### 8. Process and Transform Data ✅
- **Requirement:** Parse and transform JSON/XML data
- **Implementation:** 
  - Parse JSON response
  - Extract relevant fields
  - Format data for display
  - Handle missing values
- **Location:** `app.py` - `transform_book_data()` function (line 68-90)

### 9. Data Display Page ✅
- **Requirement:** HTML page to display processed data using tables/lists
- **Implementation:** 
  - Book cards with formatted information
  - Cover images
  - Detailed book metadata in organized layout
- **Location:** `templates/results.html`

### 10. Error Handling ✅
- **Requirement:** Handle invalid API responses and missing data
- **Implementation:**
  - Try-except blocks for API calls
  - Timeout handling
  - Flash messages for errors
  - Graceful handling of missing book data
- **Location:** `app.py` - `fetch_books()` function

### 11. CSS/Bootstrap Styling ✅
- **Requirement:** Include styling for responsiveness
- **Implementation:**
  - Bootstrap 5 via CDN
  - Custom CSS file
  - Responsive grid system
  - Mobile-friendly design
- **Location:** `templates/base.html`, `static/style.css`

### 12. Interactive Elements ✅
- **Requirement:** Provide interactive features
- **Implementation:**
  - Form validation
  - Dynamic search filtering
  - Clickable links to OpenLibrary
  - Responsive navigation
- **Location:** All template files

---

## Project Structure

```
book-search-app/
│
├── app.py                  # Main Flask application
├── forms.py                # Form definitions and validation
├── requirements.txt        # Python dependencies
├── .env           			# Environment variable
├── .gitignore              # Git ignore patterns
├── README.md               # This file
│
├── templates/
│   ├── base.html           # Base template with navbar/footer
│   ├── index.html          # Search form page
│   └── results.html        # Results display page
│
└── static/
    └── style.css           # Custom CSS styling
```

---

## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'flask'`  
**Solution:** Activate your virtual environment and run `pip install -r requirements.txt`

**Issue:** Application won't start  
**Solution:** Ensure port 5000 is not in use by another application

**Issue:** No search results  
**Solution:** Check your internet connection and try a different search query

**Issue:** API timeout errors  
**Solution:** The OpenLibrary API may be slow; try again in a few moments

---

## Credits and References

- **OpenLibrary API:** https://openlibrary.org/developers/api
- **Flask Documentation:** https://flask.palletsprojects.com/
- **Bootstrap 5:** https://getbootstrap.com/
