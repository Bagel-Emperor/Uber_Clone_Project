"""
Session Management Module for Uber Clone Project

This module provides comprehensive session management functionality for the 
ride-sharing platform, including basic sessions, sliding expiration, and 
persistent storage options.

Classes:
    SessionManager: Basic session management with fixed expiration
    SlidingSessionManager: Auto-refresh sessions on access
    PersistentSessionManager: File-backed session storage
"""

from .session_manager import SessionManager, SlidingSessionManager, PersistentSessionManager

__all__ = ['SessionManager', 'SlidingSessionManager', 'PersistentSessionManager']