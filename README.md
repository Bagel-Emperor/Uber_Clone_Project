# Uber Clone Project - Perpex Internship

This repository contains the implementation of a ride-sharing platform (Uber Clone) developed as part of the Perpex internship program. The project is structured in tasks, each building upon the previous foundation to create a comprehensive understanding of real-time applications, session management, authentication, and API development.

## 📋 Project Overview

The Uber Clone project simulates a ride-sharing platform focusing on:
- **Session Management** - Custom session handling for drivers and riders
- **User Authentication** - Secure login/logout mechanisms  
- **Real-time Features** - Driver-rider matching and tracking
- **RESTful APIs** - Django REST Framework implementation
- **Security** - Token-based authentication and session expiration

## 🎯 Task 1: Session Management System ✅

**Objective**: Build a foundational session manager using pure Python to understand session handling in stateless environments.

### Requirements Implemented:

#### Core SessionManager Class
- ✅ `__init__(self, expiry_seconds)` - Initialize with configurable session expiry
- ✅ `create_session(self, session_id)` - Create sessions with `time.time()` timestamps
- ✅ `is_session_active(self, session_id)` - Validate sessions with automatic cleanup
- ✅ `delete_session(self, session_id)` - Manual session deletion ("Deleted"/"Not Found")

#### Key Features:
- **In-memory storage** using Python dictionaries
- **Automatic expiration** - Sessions auto-delete when expired
- **Thread-safe implementation** with proper logging
- **Production-ready** with comprehensive error handling

#### Bonus Features Implemented:
- ✅ **SlidingSessionManager** - Auto-refresh sessions on access (sliding expiration)
- ✅ **PersistentSessionManager** - File-backed storage, survives application restarts
- ✅ **Comprehensive test suite** - 26+ test cases with `time.sleep()` expiry testing
- ✅ **Django integration examples** - Middleware and view implementations

### 📁 Project Structure

```
session_management/
├── __init__.py                 # Package initialization
├── session_manager.py          # Core SessionManager classes
├── test_session_manager.py     # Comprehensive test suite (26+ tests)
├── session_integration_examples.py  # Django integration patterns
└── session_demo.py            # Usage examples and demonstrations
```

### 🚀 Quick Start

```python
from session_management import SessionManager

# Initialize session manager with 30-minute expiry
sm = SessionManager(expiry_seconds=1800)

# Create a session for a driver
sm.create_session("driver_123")

# Check if session is active
if sm.is_session_active("driver_123"):
    print("Driver is online!")

# Manual logout
result = sm.delete_session("driver_123")  # Returns "Deleted"
```

### 🧪 Running Tests

```bash
python session_management/test_session_manager.py
```

### 📊 Test Coverage

The implementation includes comprehensive testing:
- ✅ Session creation and validation
- ✅ Expiry logic with `time.sleep()` delays
- ✅ Edge cases and error handling
- ✅ Sliding expiration behavior
- ✅ Persistent storage functionality
- ✅ Thread safety and concurrent access
- ✅ Django middleware integration

---

## 🛠 Technologies Used

- **Python 3.8+** - Core implementation language
- **Django 4.2+** - Web framework (for future tasks)
- **time** module - Session timestamp management
- **unittest** - Testing framework
- **uuid** - Session ID generation
- **json** - Persistent storage serialization

## 📝 Development Notes

This session management system serves as the foundation for upcoming tasks:
- **Task 2**: Rider/Driver Models
- **Task 3**: Registration API
- **Task 4**: JWT Authentication

The implementation prioritizes educational value, demonstrating how sessions work "under the hood" before integrating with Django's built-in session framework.

## 👤 Author

**Perpex Intern** - Session Management Implementation  
*Built for educational purposes and portfolio demonstration*

## 📄 License

MIT License - See LICENSE file for details