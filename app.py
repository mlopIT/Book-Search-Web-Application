"""
Flask Book Search Application
Uses the OpenLibrary API to search for books and display results.
"""

import os
import requests
from flask import Flask, render_template, request, flash
from forms import BookSearchForm
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# OpenLibrary API base URL
OPENLIBRARY_API_BASE = 'https://openlibrary.org/search.json'
COVER_IMAGE_BASE = 'https://covers.openlibrary.org/b/id'


def fetch_books(query, search_type, limit):
    """
    Fetch book data from OpenLibrary API.
    
    Args:
        query (str): Search term
        search_type (str): Type of search ('title', 'author', or 'subject')
        limit (int): Maximum number of results
    
    Returns:
        dict: API response or None if request fails
    """
    try:
        # Build API parameters based on search type
        params = {
            'limit': limit,
            'fields': 'key,title,author_name,first_publish_year,isbn,subject,cover_i,language,edition_count,publish_year'
        }
        
        # Map search type to API parameter
        if search_type == 'title':
            params['title'] = query
        elif search_type == 'author':
            params['author'] = query
        elif search_type == 'subject':
            params['subject'] = query
        
        # Make API request with timeout
        response = requests.get(
            OPENLIBRARY_API_BASE,
            params=params,
            timeout=10,
            headers={'User-Agent': 'FlaskBookSearchApp/1.0'}
        )
        
        # Raise exception for bad status codes
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.Timeout:
        flash('Request timed out. Please try again.', 'error')
        return None
    except requests.exceptions.RequestException as e:
        flash(f'Error fetching data from API: {str(e)}', 'error')
        return None
    except ValueError:
        flash('Invalid response from API.', 'error')
        return None


def transform_book_data(api_response):
    """
    Transform raw API data into a cleaner format for display.
    
    Args:
        api_response (dict): Raw API response
    
    Returns:
        list: List of processed book dictionaries
    """
    if not api_response or 'docs' not in api_response:
        return []
    
    books = []
    for doc in api_response['docs']:
        # Calculate publication year range
        publish_year_list = doc.get('publish_year', [])
        if publish_year_list:
            sorted_years = sorted(publish_year_list)
            if len(sorted_years) > 1:
                publish_years = f"{sorted_years[0]}-{sorted_years[-1]}"
            else:
                publish_years = str(sorted_years[0])
        else:
            publish_years = str(doc.get('first_publish_year', 'N/A'))
        
        # Extract and format book information
        # For the project, I decided to show only up to 3 languages to keep the table readable
        book = {
            'title': doc.get('title', 'Unknown Title'),
            'authors': ', '.join(doc.get('author_name', ['Unknown Author'])),
            'year': doc.get('first_publish_year', 'N/A'),
            'isbn': doc.get('isbn', ['N/A'])[0] if doc.get('isbn') else 'N/A',
            'subjects': ', '.join(doc.get('subject', [])[:5]) if doc.get('subject') else 'N/A',
            'edition_count': doc.get('edition_count', 'N/A'),
            'publish_years': publish_years,
            'languages': ', '.join(doc.get('language', ['eng'])[:3]),
            'cover_url': f"{COVER_IMAGE_BASE}/{doc['cover_i']}-M.jpg" if doc.get('cover_i') else None,
            'openlibrary_url': f"https://openlibrary.org{doc['key']}" if doc.get('key') else None
        }
        books.append(book)
    
    return books


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route: Display search form and handle submissions.
    """
    form = BookSearchForm()
    
    if form.validate_on_submit():
        # Get form data
        search_query = form.search_query.data
        search_type = form.search_type.data
        result_limit = form.result_limit.data
        
        # Fetch data from API
        api_response = fetch_books(search_query, search_type, result_limit)
        
        if api_response:
            # Transform data
            books = transform_book_data(api_response)
            
            # Get total number of results found
            total_found = api_response.get('numFound', 0)
            
            # Render results page
            return render_template(
                'results.html',
                books=books,
                search_query=search_query,
                search_type=search_type,
                result_limit=result_limit,
                total_found=total_found
            )
    
    # Display form (GET request or validation failed)
    return render_template('index.html', form=form)


@app.route('/results', methods=['POST'])
def results():
    """
    Results route: Alternative endpoint for form submission.
    Redirects to index route for processing.
    """
    return index()


if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
