#!/usr/bin/env python3
"""
Simple API Test Script
Test the prompt engineering backend API
"""

import requests
import json

BASE_URL = "http://localhost:5001/api"

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")

def test_analyze_task():
    """Test task analysis"""
    try:
        data = {
            "task": "Python ile bir web uygulaması geliştir",
            "context": "Flask framework kullanılacak"
        }
        response = requests.post(f"{BASE_URL}/analyze-task", json=data)
        if response.status_code == 200:
            print("✅ Task analysis passed")
            result = response.json()
            print(f"   Task type: {result.get('task_type')}")
            print(f"   Complexity: {result.get('complexity')}")
            print(f"   Recommended: {result.get('recommended_technique')}")
        else:
            print(f"❌ Task analysis failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Task analysis error: {e}")

def test_templates():
    """Test templates endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/templates")
        if response.status_code == 200:
            print("✅ Templates fetch passed")
            templates = response.json().get('templates', [])
            print(f"   Found {len(templates)} templates")
            for template in templates[:3]:
                print(f"   - {template.get('name')}: {template.get('technique')}")
        else:
            print(f"❌ Templates fetch failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Templates fetch error: {e}")

def test_techniques():
    """Test techniques endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/techniques")
        if response.status_code == 200:
            print("✅ Techniques fetch passed")
            techniques = response.json().get('techniques', [])
            print(f"   Found {len(techniques)} techniques")
        else:
            print(f"❌ Techniques fetch failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Techniques fetch error: {e}")

def test_statistics():
    """Test statistics endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/statistics")
        if response.status_code == 200:
            print("✅ Statistics fetch passed")
            stats = response.json()
            print(f"   Total prompts: {stats.get('total_prompts', 0)}")
        else:
            print(f"❌ Statistics fetch failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Statistics fetch error: {e}")

if __name__ == "__main__":
    print("🧪 Testing Prompt Engineering API")
    print("=" * 40)
    
    test_health()
    print()
    test_analyze_task()
    print()
    test_templates()
    print()
    test_techniques()
    print()
    test_statistics()
    
    print("\n🎯 API testing completed!")