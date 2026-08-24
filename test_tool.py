import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Add parent directory to sys.path so we can import tool.py from the root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tool import web_search, scrape_url

def test_web_search():
    """Test the web_search tool correctly calls Tavily and formats the output."""
    with patch("tool.tavily.search") as mock_search:

        # Mock the response from tavily
        mock_search.return_value = {
            'results': [
                {
                    'title': 'Test Title 1',
                    'url': 'http://test1.com',
                    'content': 'This is a test snippet.'
                },
                { 
                    'title': 'Test Title 2',
                    'url': 'http://test2.com',
                    'content': 'Another snippet.'
                }
            ]
        }
        
        # Invoke the LangChain tool
        result = web_search.invoke({"query": "test query"})
        
        # Verify the mock was called correctly
        mock_search.assert_called_once_with(query="test query", max_results=5)
        
        # Verify the formatted output
        assert "Title: Test Title 1" in result
        assert "URL: http://test1.com" in result
        assert "This is a test snippet." in result
        assert "Title: Test Title 2" in result
        assert "URL: http://test2.com" in result
        assert "Another snippet." in result

def test_scrape_url_success():
    """Test scrape_url tool extracts text and removes unwanted tags."""
    with patch("tool.requests.get") as mock_get:
        # Create a mock response
        mock_resp = MagicMock()
        mock_resp.text = "<html><body><h1>Hello World</h1><script>alert('bad');</script><nav>nav text</nav></body></html>"
        mock_get.return_value = mock_resp
        
        # Invoke the LangChain tool
        result = scrape_url.invoke({"url": "http://test.com"})
        
        # Verify requests.get was called correctly
        mock_get.assert_called_once_with("http://test.com", timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        
        # Verify the content
        assert "Hello World" in result
        # Ensure unwanted tags are removed
        assert "alert('bad')" not in result
        assert "nav text" not in result

def test_scrape_url_exception():
    """Test scrape_url tool gracefully handles exceptions."""
    with patch("tool.requests.get") as mock_get:
        # Simulate a connection error
        mock_get.side_effect = Exception("Connection error")
        
        # Invoke the LangChain tool
        result = scrape_url.invoke({"url": "http://test.com"})
        
        # Verify requests.get was called
        mock_get.assert_called_once_with("http://test.com", timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        
        # Verify exception handling output
        assert "Could not scrape URL: Connection error" in result

if __name__ == "__main__":
    pytest.main(["-v", "--import-mode=importlib", __file__])
