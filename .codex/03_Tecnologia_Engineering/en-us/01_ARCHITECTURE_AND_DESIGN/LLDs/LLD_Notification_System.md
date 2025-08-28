# Low-Level Design - Notification System

**Document ID:** `LLD_NOTIFICATION_SYSTEM`  
**Version:** 1.0  
**Last Updated:** 2025-01-20  
**Status:** Active  
**Owner:** Engineering Team  
**Tags:** [notifications, system-design, multi-channel, real-time]  

---

## Executive Summary

This document details the low-level design for the **Notification System** of Recoloca.ai, a comprehensive multi-channel notification infrastructure that supports in-app, email, and PWA push notifications. The system is designed to provide personalized, scalable, and reliable communication with users across different touchpoints in their job search journey.

### Key Features
- **Multi-channel delivery**: In-app, email, and PWA push notifications
- **User preference management**: Granular control over notification types and channels
- **Template-based system**: Flexible content management with internationalization support
- **Real-time delivery**: WebSocket integration for instant in-app notifications
- **Analytics and monitoring**: Comprehensive delivery metrics and user engagement tracking
- **Scalable architecture**: Designed to handle high-volume notification processing

---

## System Architecture

### Architecture Overview

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[Flutter PWA] --> B[Notification Center]
        A --> C[Settings Page]
        A --> D[Service Worker]
    end
    
    subgraph "Backend Services"
        E[Notification API] --> F[Notification Dispatcher]
        F --> G[Channel Handlers]
        G --> H[In-App Handler]
        G --> I[Email Handler]
        G --> J[Push Handler]
    end
    
    subgraph "External Services"
        K[Supabase Auth]
        L[Firebase Cloud Messaging]
        M[Email Service]
    end
    
    subgraph "Database"
        N[(Notifications)]
        O[(User Preferences)]
        P[(Templates)]
        Q[(Logs)]
    end
    
    subgraph "Event Sources"
        R[Job Status Changes]
        S[CV Analysis]
        T[AI Coach]
        U[System Events]
    end
    
    R --> E
    S --> E
    T --> E
    U --> E
    
    H --> A
    I --> M
    J --> L
    
    E --> N
    E --> O
    F --> P
    F --> Q
    
    I --> K
    J --> K
end
```

### Data Flow

1. **Event Trigger**: System events (job updates, CV analysis completion, etc.) trigger notifications
2. **Dispatcher**: Central dispatcher receives notification requests and processes them
3. **Preference Check**: System validates user preferences for the notification type and channels
4. **Template Selection**: Appropriate template is selected based on notification type and user language
5. **Content Generation**: Dynamic content is generated using template variables
6. **Multi-channel Delivery**: Notification is sent through enabled channels (in-app, email, push)
7. **Logging**: All delivery attempts and results are logged for analytics and debugging

---

## Technical Components

### Core Services

#### NotificationService
```python
class NotificationService:
    """
    Core service for notification management
    """
    
    async def create_notification(
        self,
        user_id: UUID,
        notification_type: str,
        title: str,
        content: str,
        data: Dict = None,
        scheduled_at: Optional[datetime] = None
    ) -> Notification:
        """
        Creates a new notification
        """
        pass
    
    async def send_notification(self, notification_id: UUID) -> bool:
        """
        Sends notification through configured channels
        """
        pass
    
    async def mark_as_read(self, notification_id: UUID, user_id: UUID) -> bool:
        """
        Marks notification as read
        """
        pass
    
    async def get_user_notifications(
        self,
        user_id: UUID,
        limit: int = 20,
        offset: int = 0,
        unread_only: bool = False
    ) -> List[Notification]:
        """
        Retrieves user notifications
        """
        pass
```

#### API Endpoints
```python
@router.get("/notifications")
async def get_notifications(
    current_user: User = Depends(get_current_user),
    limit: int = Query(20, le=100),
    offset: int = Query(0, ge=0),
    unread_only: bool = Query(False)
):
    """
    GET /api/v1/notifications
    Retrieves notifications for authenticated user
    """
    pass

@router.post("/notifications/{notification_id}/read")
async def mark_notification_read(
    notification_id: UUID,
    current_user: User = Depends(get_current_user)
):
    """
    POST /api/v1/notifications/{id}/read
    Marks notification as read
    """
    pass

@router.get("/notifications/preferences")
async def get_notification_preferences(
    current_user: User = Depends(get_current_user)
):
    """
    GET /api/v1/notifications/preferences
    Retrieves user notification preferences
    """
    pass

@router.put("/notifications/preferences")
async def update_notification_preferences(
    preferences: NotificationPreferencesUpdate,
    current_user: User = Depends(get_current_user)
):
    """
    PUT /api/v1/notifications/preferences
    Updates user notification preferences
    """
    pass
```

### Data Models

#### Notification Model
```python
class Notification(BaseModel):
    id: UUID
    user_id: UUID
    type: str
    title: str
    content: str
    data: Optional[Dict] = None
    read_at: Optional[datetime] = None
    scheduled_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
```

#### User Preferences Model
```python
class NotificationPreferences(BaseModel):
    user_id: UUID
    notification_type: str
    in_app_enabled: bool = True
    email_enabled: bool = True
    push_enabled: bool = True
    frequency: str = "immediate"  # immediate, daily, weekly, disabled
    quiet_hours_start: Optional[time] = None
    quiet_hours_end: Optional[time] = None
```

#### Template Model
```python
class NotificationTemplate(BaseModel):
    id: UUID
    type: str
    channel: str  # in_app, email, push
    language: str = "en-US"
    subject_template: str
    content_template: str
    variables: Dict[str, str]
    created_at: datetime
    updated_at: datetime
```

---

## Channel Implementation

### In-App Notifications

**Frontend (Flutter):**
```dart
class NotificationCenter extends StatefulWidget {
  @override
  _NotificationCenterState createState() => _NotificationCenterState();
}

class _NotificationCenterState extends State<NotificationCenter> {
  final NotificationService _notificationService = NotificationService();
  List<AppNotification> _notifications = [];
  
  @override
  void initState() {
    super.initState();
    _loadNotifications();
    _setupRealTimeUpdates();
  }
  
  void _setupRealTimeUpdates() {
    // WebSocket or Server-Sent Events for real-time updates
    _notificationService.onNewNotification.listen((notification) {
      setState(() {
        _notifications.insert(0, notification);
      });
    });
  }
}
```

**Backend Handler:**
```python
class InAppNotificationHandler:
    """
    Handler for in-app notifications
    """
    
    async def send_notification(
        self,
        user_id: UUID,
        notification: Notification
    ) -> bool:
        """
        Sends in-app notification via WebSocket/SSE
        """
        try:
            # Send via WebSocket if user is online
            if await self.is_user_online(user_id):
                await self.websocket_manager.send_to_user(
                    user_id,
                    {
                        "type": "notification",
                        "data": notification.dict()
                    }
                )
            
            # Save to database for later retrieval
            await self.save_notification(notification)
            return True
            
        except Exception as e:
            logger.error(f"Error sending in-app notification: {e}")
            return False
```

### Email Notifications

```python
class EmailNotificationHandler:
    """
    Handler for email notifications using Supabase
    """
    
    def __init__(self):
        self.supabase_client = get_supabase_client()
        self.template_engine = Jinja2Templates(directory="templates/email")
    
    async def send_notification(
        self,
        user_email: str,
        notification: Notification
    ) -> bool:
        """
        Sends email notification
        """
        try:
            # Get template
            template = await self.get_email_template(
                notification.type,
                "en-US"
            )
            
            # Render content
            subject = self.template_engine.render_string(
                template.subject_template,
                **notification.data
            )
            
            html_content = self.template_engine.render_string(
                template.content_template,
                **notification.data
            )
            
            # Send via Supabase
            response = await self.supabase_client.auth.admin.send_email(
                email=user_email,
                subject=subject,
                html=html_content
            )
            
            return response.get("success", False)
            
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return False
```

### PWA Push Notifications

**Service Worker (JavaScript):**
```javascript
// sw.js - Service Worker
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

// Firebase configuration
firebase.initializeApp({
  apiKey: "your-api-key",
  authDomain: "recoloca-ai.firebaseapp.com",
  projectId: "recoloca-ai",
  storageBucket: "recoloca-ai.appspot.com",
  messagingSenderId: "123456789",
  appId: "your-app-id"
});

const messaging = firebase.messaging();

// Background message handler
messaging.onBackgroundMessage((payload) => {
  console.log('Background message received:', payload);
  
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    data: payload.data,
    actions: [
      {
        action: 'open',
        title: 'Open App'
      },
      {
        action: 'dismiss',
        title: 'Dismiss'
      }
    ]
  };
  
  self.registration.showNotification(notificationTitle, notificationOptions);
});
```

**Backend Handler:**
```python
class PushNotificationHandler:
    """
    Handler for push notifications via Firebase Cloud Messaging
    """
    
    def __init__(self):
        # Initialize Firebase Admin SDK
        if not firebase_admin._apps:
            cred = credentials.Certificate("path/to/serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
    
    async def send_notification(
        self,
        device_tokens: List[str],
        notification: Notification
    ) -> bool:
        """
        Sends push notification to devices
        """
        try:
            message = messaging.MulticastMessage(
                notification=messaging.Notification(
                    title=notification.title,
                    body=notification.content
                ),
                data={
                    "notification_id": str(notification.id),
                    "type": notification.type,
                    **notification.data
                },
                tokens=device_tokens,
                webpush=messaging.WebpushConfig(
                    notification=messaging.WebpushNotification(
                        icon="/icons/icon-192x192.png",
                        badge="/icons/badge-72x72.png",
                        actions=[
                            messaging.WebpushNotificationAction(
                                action="open",
                                title="Open App"
                            )
                        ]
                    )
                )
            )
            
            response = messaging.send_multicast(message)
            
            # Log results
            logger.info(f"Push sent: {response.success_count} successes, {response.failure_count} failures")
            
            return response.success_count > 0
            
        except Exception as e:
            logger.error(f"Error sending push notification: {e}")
            return False
```

---

## Notification Templates

### Notification Types

```python
class NotificationTypes:
    # Job updates
    JOB_STATUS_CHANGED = "job_status_changed"
    NEW_JOB_MATCH = "new_job_match"
    JOB_DEADLINE_REMINDER = "job_deadline_reminder"
    
    # CV analysis
    CV_ANALYSIS_COMPLETE = "cv_analysis_complete"
    CV_OPTIMIZATION_SUGGESTION = "cv_optimization_suggestion"
    
    # AI Coach
    COACH_WEEKLY_TIPS = "coach_weekly_tips"
    COACH_INTERVIEW_PREP = "coach_interview_prep"
    
    # System
    SUBSCRIPTION_EXPIRING = "subscription_expiring"
    WELCOME_MESSAGE = "welcome_message"
    FEATURE_ANNOUNCEMENT = "feature_announcement"
    
    # Reminders
    DAILY_ACTIVITY_REMINDER = "daily_activity_reminder"
    WEEKLY_PROGRESS_SUMMARY = "weekly_progress_summary"
```

### Template Examples

```json
{
  "type": "job_status_changed",
  "channel": "push",
  "language": "en-US",
  "subject_template": "Job Update: {{ job_title }}",
  "content_template": "Your application for {{ job_title }} at {{ company_name }} has been updated to: {{ new_status }}",
  "variables": {
    "job_title": "string",
    "company_name": "string",
    "new_status": "string",
    "application_date": "datetime"
  }
}
```

```json
{
  "type": "cv_analysis_complete",
  "channel": "email",
  "language": "en-US",
  "subject_template": "Your CV Analysis is Ready! 📄✨",
  "content_template": "<h2>Hello {{ user_name }}!</h2><p>Your CV analysis has been completed with a score of <strong>{{ score }}/100</strong>.</p><p>Key improvement suggestions:</p><ul>{% for suggestion in suggestions %}<li>{{ suggestion }}</li>{% endfor %}</ul><p><a href='{{ cv_url }}'>View complete analysis</a></p>",
  "variables": {
    "user_name": "string",
    "score": "number",
    "suggestions": "array",
    "cv_url": "string"
  }
}
```

---

## User Preferences Management

### Default Preferences

```python
DEFAULT_NOTIFICATION_PREFERENCES = {
    "job_status_changed": {
        "in_app_enabled": True,
        "email_enabled": True,
        "push_enabled": True,
        "frequency": "immediate"
    },
    "new_job_match": {
        "in_app_enabled": True,
        "email_enabled": True,
        "push_enabled": True,
        "frequency": "immediate"
    },
    "cv_analysis_complete": {
        "in_app_enabled": True,
        "email_enabled": True,
        "push_enabled": True,
        "frequency": "immediate"
    },
    "coach_weekly_tips": {
        "in_app_enabled": True,
        "email_enabled": True,
        "push_enabled": False,
        "frequency": "weekly"
    },
    "daily_activity_reminder": {
        "in_app_enabled": False,
        "email_enabled": False,
        "push_enabled": True,
        "frequency": "daily"
    }
}
```

### Settings Interface (Flutter)

```dart
class NotificationSettingsPage extends StatefulWidget {
  @override
  _NotificationSettingsPageState createState() => _NotificationSettingsPageState();
}

class _NotificationSettingsPageState extends State<NotificationSettingsPage> {
  Map<String, NotificationPreference> _preferences = {};
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Notification Settings'),
      ),
      body: ListView(
        children: [
          _buildSectionHeader('Job Updates'),
          _buildNotificationTile(
            'job_status_changed',
            'Status Changes',
            'Get updates when your application status changes'
          ),
          _buildNotificationTile(
            'new_job_match',
            'New Job Matches',
            'Be notified about jobs that match your profile'
          ),
          
          _buildSectionHeader('CV Analysis'),
          _buildNotificationTile(
            'cv_analysis_complete',
            'Analysis Complete',
            'Receive your CV analysis results'
          ),
          
          _buildSectionHeader('AI Coach'),
          _buildNotificationTile(
            'coach_weekly_tips',
            'Weekly Tips',
            'Get personalized tips to improve your job search'
          ),
          
          _buildSectionHeader('Reminders'),
          _buildNotificationTile(
            'daily_activity_reminder',
            'Daily Reminder',
            'Stay active in your job search'
          ),
          
          _buildQuietHoursSection(),
        ],
      ),
    );
  }
}
```

---

## Monitoring and Analytics

### Delivery Metrics

```python
class NotificationAnalytics:
    """
    Analytics for notification system
    """
    
    async def get_delivery_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """
        Delivery metrics by channel and type
        """
        query = """
        SELECT 
            n.type,
            nl.channel,
            nl.status,
            COUNT(*) as count,
            AVG(EXTRACT(EPOCH FROM (nl.created_at - n.created_at))) as avg_delivery_time
        FROM notifications n
        JOIN notification_logs nl ON n.id = nl.notification_id
        WHERE n.created_at BETWEEN %s AND %s
        GROUP BY n.type, nl.channel, nl.status
        """
        
        results = await self.db.fetch_all(query, [start_date, end_date])
        return self._format_metrics(results)
    
    async def get_engagement_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """
        User engagement metrics
        """
        query = """
        SELECT 
            n.type,
            COUNT(*) as sent,
            COUNT(n.read_at) as read,
            AVG(EXTRACT(EPOCH FROM (n.read_at - n.created_at))) as avg_read_time
        FROM notifications n
        WHERE n.created_at BETWEEN %s AND %s
        GROUP BY n.type
        """
        
        results = await self.db.fetch_all(query, [start_date, end_date])
        return self._format_engagement_metrics(results)
```

### Key Performance Indicators

- **Delivery Rate**: Percentage of notifications successfully delivered
- **Open Rate**: Percentage of notifications opened/read by users
- **Click-through Rate**: Percentage of notifications that led to app engagement
- **Unsubscribe Rate**: Percentage of users who disabled specific notification types
- **Average Delivery Time**: Time from creation to delivery
- **Channel Performance**: Comparative performance across channels

---

## Testing Strategy

### Unit Tests
- **Service Layer**: Test notification creation, sending, and preference management
- **Handler Classes**: Test individual channel handlers (in-app, email, push)
- **Template Engine**: Test template rendering with various data inputs
- **Analytics**: Test metric calculation and reporting functions

### Integration Tests
- **End-to-End Flow**: Test complete notification flow from trigger to delivery
- **Multi-channel Delivery**: Test simultaneous delivery across all channels
- **Preference Enforcement**: Test that user preferences are respected
- **External Service Integration**: Test Firebase and Supabase integrations

### Performance Tests
- **Load Testing**: Test system under high notification volume
- **Delivery Speed**: Measure notification delivery times
- **Database Performance**: Test query performance under load
- **Memory Usage**: Monitor memory consumption during batch processing

---

## Security and Privacy

### Data Protection
- **Encryption**: All notification data encrypted at rest and in transit
- **Access Control**: Role-based access to notification management
- **Data Retention**: Automatic cleanup of old notification logs
- **Privacy Compliance**: GDPR/LGPD compliant data handling

### Security Measures
- **Input Validation**: All notification content validated and sanitized
- **Rate Limiting**: Protection against notification spam
- **Authentication**: Secure API endpoints with proper authentication
- **Audit Logging**: Comprehensive logging of all notification activities

---

## Deployment and Configuration

### Environment Variables
```bash
# Firebase Configuration
FIREBASE_PROJECT_ID=recoloca-ai
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_PRIVATE_KEY=your-private-key
FIREBASE_CLIENT_EMAIL=firebase-adminsdk@recoloca-ai.iam.gserviceaccount.com

# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Notification Settings
NOTIFICATION_BATCH_SIZE=100
NOTIFICATION_RETRY_ATTEMPTS=3
NOTIFICATION_RETRY_DELAY=5
```

### Database Migrations
```sql
-- Create notifications table
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    type VARCHAR(100) NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    data JSONB,
    read_at TIMESTAMP WITH TIME ZONE,
    scheduled_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create notification preferences table
CREATE TABLE notification_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id),
    notification_type VARCHAR(100) NOT NULL,
    in_app_enabled BOOLEAN DEFAULT TRUE,
    email_enabled BOOLEAN DEFAULT TRUE,
    push_enabled BOOLEAN DEFAULT TRUE,
    frequency VARCHAR(20) DEFAULT 'immediate',
    quiet_hours_start TIME,
    quiet_hours_end TIME,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, notification_type)
);

-- Create notification templates table
CREATE TABLE notification_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type VARCHAR(100) NOT NULL,
    channel VARCHAR(20) NOT NULL,
    language VARCHAR(10) DEFAULT 'en-US',
    subject_template TEXT NOT NULL,
    content_template TEXT NOT NULL,
    variables JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(type, channel, language)
);

-- Create notification logs table
CREATE TABLE notification_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notification_id UUID NOT NULL REFERENCES notifications(id),
    channel VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL,
    error_message TEXT,
    delivered_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## Acceptance Criteria

### Functional Requirements
- [ ] Users can receive notifications through in-app, email, and push channels
- [ ] Users can configure notification preferences for each notification type
- [ ] System supports real-time in-app notifications via WebSocket
- [ ] Email notifications are sent using Supabase Auth
- [ ] PWA push notifications work via Firebase Cloud Messaging
- [ ] Notification templates support multiple languages
- [ ] System handles notification scheduling and batching
- [ ] Analytics dashboard shows delivery and engagement metrics

### Non-Functional Requirements
- [ ] System can handle 10,000+ notifications per hour
- [ ] Notification delivery time < 5 seconds for immediate notifications
- [ ] 99.9% uptime for notification service
- [ ] All notification data is encrypted
- [ ] System complies with GDPR/LGPD privacy requirements
- [ ] Comprehensive logging and monitoring in place

### Technical Requirements
- [ ] RESTful API endpoints for notification management
- [ ] Database schema supports all notification features
- [ ] Service Worker properly handles background push notifications
- [ ] Flutter app displays notifications in real-time
- [ ] Error handling and retry mechanisms implemented
- [ ] Unit and integration tests achieve 90%+ coverage

---

## Related Documents

- [System Architecture Overview](../SYSTEM_ARCHITECTURE.md)
- [API Documentation](../../API_DOCUMENTATION.md)
- [Database Schema](../DATABASE_SCHEMA.md)
- [Security Guidelines](../../SECURITY_GUIDELINES.md)
- [Deployment Guide](../../DEPLOYMENT_GUIDE.md)

---

**Document Control:**
- **Created:** 2025-01-20
- **Last Review:** 2025-01-20
- **Next Review:** 2025-02-20
- **Approved By:** Engineering Lead
- **Version History:** v1.0 - Initial version