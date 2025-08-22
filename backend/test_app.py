#!/usr/bin/env python3
"""
Simple test to verify FastAPI application can start
"""

def test_imports():
    """Test that all required modules can be imported"""
    try:
        from fastapi import FastAPI
        print("✓ FastAPI imported successfully")
        
        from pydantic import BaseModel
        print("✓ Pydantic imported successfully")
        
        from main import app
        print("✓ Main app imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_app_creation():
    """Test that the FastAPI app can be created"""
    try:
        from main import app
        assert app.title == "FastAPI Project"
        assert app.version == "1.0.0"
        print("✓ FastAPI app created successfully")
        return True
    except Exception as e:
        print(f"✗ App creation error: {e}")
        return False

if __name__ == "__main__":
    print("Running basic tests...")
    print("-" * 40)
    
    success = True
    
    if not test_imports():
        success = False
    
    if not test_app_creation():
        success = False
    
    print("-" * 40)
    if success:
        print("✓ All basic tests passed!")
        print("You can now run the application with: python start.py")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        exit(1)
