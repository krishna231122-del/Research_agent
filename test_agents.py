import sys
import os
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import agents

def test_search_agent():
    """test the build_search_agent that it working and give output correctly"""
    
    with patch("agents.build_search_agent") as mock_build_search:
        fake_agent = MagicMock()
        fake_agent.invoke.return_value = "Title: Test Title agent 1\nURL: http://agenttest1.com\nThis is a test snippet.\nTitle: Test Title agent 2\nURL: http://agenttest2.com\nAnother snippet."
        mock_build_search.return_value = fake_agent
        
        agent = agents.build_search_agent()
        result = agent.invoke({"input": "test query"})

        fake_agent.invoke.assert_called_once_with({"input": "test query"})

        assert "Title: Test Title agent 1" in result
        assert "URL: http://agenttest1.com" in result
        assert "This is a test snippet." in result
        assert "Title: Test Title agent 2" in result
        assert "URL: http://agenttest2.com" in result
        assert "Another snippet." in result



def test_reader_agent():
    """test the build_reader_agent that it working and give output correctly"""
    
    with patch("agents.build_reader_agent") as mock_build_reader:
        fake_agent = MagicMock()
        fake_agent.invoke.return_value = "Title: Test Title agent 1\nURL: http://readtest1.com\nThis is a test snippet.\nTitle: Test Title agent 2\nURL: http://readtest2.com\nAnother snippet."
        mock_build_reader.return_value = fake_agent
        
        agent = agents.build_reader_agent()
        result = agent.invoke({"input": "test query"})
    
        fake_agent.invoke.assert_called_once_with({"input": "test query"})
    
        assert "Title: Test Title agent 1" in result
        assert "URL: http://readtest1.com" in result
        assert "This is a test snippet." in result
        assert "Title: Test Title agent 2" in result
        assert "URL: http://readtest2.com" in result
        assert "Another snippet." in result
    
if __name__ == "__main__":
    pytest.main(["-v", "--import-mode=importlib", __file__])