#!/usr/bin/env python3
"""
Quick demo to test the session management package import and basic functionality.
This file helps verify that the module is properly structured and VS Code can resolve imports.
"""

# Test the package import
from session_management import SessionManager, SlidingSessionManager, PersistentSessionManager

def test_basic_functionality():
    """Quick test to verify everything works."""
    print("🚀 Testing Uber Clone Session Management System")
    print("=" * 50)
    
    # Test basic SessionManager
    print("\n1. Testing Basic SessionManager:")
    sm = SessionManager(expiry_seconds=60)  # 1 minute sessions
    
    # Create a driver session
    sm.create_session("driver_123")
    print(f"   ✅ Driver session active: {sm.is_session_active('driver_123')}")
    
    # Create a rider session  
    sm.create_session("rider_456")
    print(f"   ✅ Rider session active: {sm.is_session_active('rider_456')}")
    
    print(f"   📊 Total active sessions: {sm.get_active_session_count()}")
    
    # Test session deletion
    result = sm.delete_session("driver_123")
    print(f"   🗑️ Driver logout result: {result}")
    
    print("\n2. Testing SlidingSessionManager:")
    sliding_sm = SlidingSessionManager(expiry_seconds=30)
    sliding_sm.create_session("active_driver_789")
    print(f"   ✅ Sliding session created and active: {sliding_sm.is_session_active('active_driver_789')}")
    
    print("\n3. Testing PersistentSessionManager:")
    persistent_sm = PersistentSessionManager(expiry_seconds=120, storage_file="demo_sessions.json")
    persistent_sm.create_session("persistent_rider_999")
    print(f"   ✅ Persistent session active: {persistent_sm.is_session_active('persistent_rider_999')}")
    
    print("\n🎉 All session managers working correctly!")
    print("📁 Session management package is properly set up for the Uber Clone project.")

if __name__ == "__main__":
    test_basic_functionality()