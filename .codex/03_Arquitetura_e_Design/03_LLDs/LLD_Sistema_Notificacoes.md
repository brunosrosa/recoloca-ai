# LLD - Sistema de Notificações

**Versão:** 1.1 (Orquestração Inteligente e Specialized Intelligence)  
**Data de Criação:** 06 de junho de 2025  
**Última Atualização:** Junho de 2025  
**Autor:** Maestro (Bruno S. Rosa)  
**Status:** Em Desenvolvimento  
**Baseado em:** [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1), [[docs/02_Requisitos/01_ERS.md]] (v1.1), [[docs/03_Arquitetura_e_Design/01_HLD.md]] (v1.1)  

## 1. Visão Geral

Este documento detalha o design de baixo nível do Sistema de Notificações do Recoloca.ai, responsável por enviar notificações in-app, por email e push PWA para manter os usuários engajados e informados sobre atualizações importantes em seu processo de recolocação.

### 1.1 Objetivos

- **Engajamento:** Manter usuários ativos e engajados com a plataforma
- **Comunicação Efetiva:** Informar sobre eventos importantes (novas vagas, atualizações de status, lembretes)
- **Personalização:** Permitir configuração granular de preferências de notificação
- **Performance:** Garantir entrega rápida e confiável das notificações
- **Escalabilidade:** Suportar crescimento da base de usuários

### 1.2 Escopo

**Incluído neste LLD:**
- Notificações in-app (Should Have)
- Notificações por email (Should Have)
- Notificações push PWA (Should Have)
- Sistema de preferências do usuário
- Templates de notificação
- Logs e analytics de entrega

**Fora do Escopo:**
- Notificações SMS (Won't Have para MVP)
- Integração com apps móveis nativos (Won't Have para MVP)

## 2. Arquitetura do Sistema

### 2.1 Componentes Principais

```mermaid
graph TB
    subgraph "Frontend (Flutter PWA)"
        A["Notification Center"]
        B["Notification Settings"]
        C["Service Worker"]
    end
    
    subgraph "Backend (FastAPI)"
        D["Notification Service"]
        E["Template Engine"]
        F["Preference Manager"]
        G["Event Dispatcher"]
    end
    
    subgraph "External Services"
        H["Firebase Cloud Messaging"]
        I["Email Provider (Supabase)"]
    end
    
    subgraph "Database (Supabase)"
        J["notifications"]
        K["notification_preferences"]
        L["notification_templates"]
        M["notification_logs"]
    end
    
    A --> D
    B --> F
    C --> H
    D --> E
    D --> F
    D --> G
    E --> L
    F --> K
    G --> H
    G --> I
    D --> J
    D --> M
```

### 2.2 Fluxo de Dados

1. **Evento Trigger:** Sistema detecta evento que requer notificação
2. **Event Dispatcher:** Processa evento e determina tipo de notificação
3. **Preference Check:** Verifica preferências do usuário
4. **Template Selection:** Seleciona template apropriado
5. **Content Generation:** Gera conteúdo personalizado
6. **Multi-Channel Delivery:** Envia via canais configurados
7. **Logging:** Registra tentativas e resultados de entrega

## 3. Modelos de Dados

### 3.1 Tabela: notifications

```sql
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL, -- 'job_update', 'cv_analysis', 'reminder', 'system'
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    data JSONB, -- Dados adicionais específicos do tipo
    channels VARCHAR[] NOT NULL, -- ['in_app', 'email', 'push']
    priority VARCHAR(20) DEFAULT 'normal', -- 'low', 'normal', 'high', 'urgent'
    status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'sent', 'delivered', 'failed', 'read'
    scheduled_at TIMESTAMP WITH TIME ZONE,
    sent_at TIMESTAMP WITH TIME ZONE,
    read_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Índices
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_status ON notifications(status);
CREATE INDEX idx_notifications_type ON notifications(type);
CREATE INDEX idx_notifications_scheduled_at ON notifications(scheduled_at);
```

### 3.2 Tabela: notification_preferences

```sql
CREATE TABLE notification_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    notification_type VARCHAR(50) NOT NULL,
    in_app_enabled BOOLEAN DEFAULT true,
    email_enabled BOOLEAN DEFAULT true,
    push_enabled BOOLEAN DEFAULT true,
    frequency VARCHAR(20) DEFAULT 'immediate', -- 'immediate', 'daily', 'weekly', 'disabled'
    quiet_hours_start TIME,
    quiet_hours_end TIME,
    timezone VARCHAR(50) DEFAULT 'America/Sao_Paulo',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, notification_type)
);

-- Índices
CREATE INDEX idx_notification_preferences_user_id ON notification_preferences(user_id);
```

### 3.3 Tabela: notification_templates

```sql
CREATE TABLE notification_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    type VARCHAR(50) NOT NULL,
    channel VARCHAR(20) NOT NULL, -- 'in_app', 'email', 'push'
    language VARCHAR(5) DEFAULT 'pt-BR',
    subject_template TEXT,
    content_template TEXT NOT NULL,
    variables JSONB, -- Variáveis disponíveis no template
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(type, channel, language)
);
```

### 3.4 Tabela: notification_logs

```sql
CREATE TABLE notification_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notification_id UUID NOT NULL REFERENCES notifications(id) ON DELETE CASCADE,
    channel VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL, -- 'sent', 'delivered', 'failed', 'bounced'
    external_id VARCHAR(255), -- ID do provedor externo (FCM, email)
    error_message TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Índices
CREATE INDEX idx_notification_logs_notification_id ON notification_logs(notification_id);
CREATE INDEX idx_notification_logs_status ON notification_logs(status);
```

## 4. APIs e Endpoints

### 4.1 Notification Service API

```python
# /api/v1/notifications

class NotificationService:
    """
    Serviço principal para gerenciamento de notificações
    """
    
    async def create_notification(
        self,
        user_id: UUID,
        notification_type: str,
        title: str,
        content: str,
        data: Optional[Dict] = None,
        channels: List[str] = None,
        priority: str = "normal",
        scheduled_at: Optional[datetime] = None
    ) -> Notification:
        """
        Cria uma nova notificação
        """
        pass
    
    async def send_notification(self, notification_id: UUID) -> bool:
        """
        Envia notificação através dos canais configurados
        """
        pass
    
    async def mark_as_read(self, notification_id: UUID, user_id: UUID) -> bool:
        """
        Marca notificação como lida
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
        Recupera notificações do usuário
        """
        pass
```

### 4.2 Endpoints REST

```python
# Endpoints principais

@router.get("/notifications")
async def get_notifications(
    current_user: User = Depends(get_current_user),
    limit: int = Query(20, le=100),
    offset: int = Query(0, ge=0),
    unread_only: bool = Query(False)
):
    """
    GET /api/v1/notifications
    Recupera notificações do usuário autenticado
    """
    pass

@router.post("/notifications/{notification_id}/read")
async def mark_notification_read(
    notification_id: UUID,
    current_user: User = Depends(get_current_user)
):
    """
    POST /api/v1/notifications/{id}/read
    Marca notificação como lida
    """
    pass

@router.get("/notifications/preferences")
async def get_notification_preferences(
    current_user: User = Depends(get_current_user)
):
    """
    GET /api/v1/notifications/preferences
    Recupera preferências de notificação do usuário
    """
    pass

@router.put("/notifications/preferences")
async def update_notification_preferences(
    preferences: NotificationPreferencesUpdate,
    current_user: User = Depends(get_current_user)
):
    """
    PUT /api/v1/notifications/preferences
    Atualiza preferências de notificação
    """
    pass

@router.post("/notifications/register-device")
async def register_push_device(
    device_data: PushDeviceRegistration,
    current_user: User = Depends(get_current_user)
):
    """
    POST /api/v1/notifications/register-device
    Registra dispositivo para notificações push
    """
    pass
```

## 5. Implementação por Canal

### 5.1 Notificações In-App

**Frontend (Flutter):**
```dart
// notification_center.dart
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
    // WebSocket ou Server-Sent Events para atualizações em tempo real
    _notificationService.onNewNotification.listen((notification) {
      setState(() {
        _notifications.insert(0, notification);
      });
    });
  }
}
```

**Backend (FastAPI):**
```python
# in_app_notifications.py
class InAppNotificationHandler:
    """
    Handler para notificações in-app
    """
    
    async def send_notification(
        self,
        user_id: UUID,
        notification: Notification
    ) -> bool:
        """
        Envia notificação in-app via WebSocket/SSE
        """
        try:
            # Enviar via WebSocket se usuário estiver online
            if await self.is_user_online(user_id):
                await self.websocket_manager.send_to_user(
                    user_id,
                    {
                        "type": "notification",
                        "data": notification.dict()
                    }
                )
            
            # Salvar no banco para recuperação posterior
            await self.save_notification(notification)
            return True
            
        except Exception as e:
            logger.error(f"Erro ao enviar notificação in-app: {e}")
            return False
```

### 5.2 Notificações por Email

```python
# email_notifications.py
class EmailNotificationHandler:
    """
    Handler para notificações por email usando Supabase
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
        Envia notificação por email
        """
        try:
            # Buscar template
            template = await self.get_email_template(
                notification.type,
                "pt-BR"
            )
            
            # Renderizar conteúdo
            subject = self.template_engine.render_string(
                template.subject_template,
                **notification.data
            )
            
            html_content = self.template_engine.render_string(
                template.content_template,
                **notification.data
            )
            
            # Enviar via Supabase
            response = await self.supabase_client.auth.admin.send_email(
                email=user_email,
                subject=subject,
                html=html_content
            )
            
            return response.get("success", False)
            
        except Exception as e:
            logger.error(f"Erro ao enviar email: {e}")
            return False
```

### 5.3 Notificações Push PWA (Firebase Cloud Messaging)

**Service Worker (JavaScript):**
```javascript
// sw.js - Service Worker
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/9.0.0/firebase-messaging-compat.js');

// Configuração Firebase
firebase.initializeApp({
  apiKey: "your-api-key",
  authDomain: "recoloca-ai.firebaseapp.com",
  projectId: "recoloca-ai",
  storageBucket: "recoloca-ai.appspot.com",
  messagingSenderId: "123456789",
  appId: "your-app-id"
});

const messaging = firebase.messaging();

// Handler para mensagens em background
messaging.onBackgroundMessage((payload) => {
  console.log('Mensagem recebida em background:', payload);
  
  const notificationTitle = payload.notification.title;
  const notificationOptions = {
    body: payload.notification.body,
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    data: payload.data,
    actions: [
      {
        action: 'open',
        title: 'Abrir App'
      },
      {
        action: 'dismiss',
        title: 'Dispensar'
      }
    ]
  };
  
  self.registration.showNotification(notificationTitle, notificationOptions);
});

// Handler para cliques na notificação
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  
  if (event.action === 'open') {
    // Abrir ou focar na aba do app
    event.waitUntil(
      clients.matchAll({ type: 'window' }).then((clientList) => {
        for (const client of clientList) {
          if (client.url.includes('recoloca.ai') && 'focus' in client) {
            return client.focus();
          }
        }
        if (clients.openWindow) {
          return clients.openWindow('/dashboard');
        }
      })
    );
  }
});
```

**Backend (Python):**
```python
# push_notifications.py
import firebase_admin
from firebase_admin import credentials, messaging

class PushNotificationHandler:
    """
    Handler para notificações push via Firebase Cloud Messaging
    """
    
    def __init__(self):
        # Inicializar Firebase Admin SDK
        if not firebase_admin._apps:
            cred = credentials.Certificate("path/to/serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
    
    async def send_notification(
        self,
        device_tokens: List[str],
        notification: Notification
    ) -> bool:
        """
        Envia notificação push para dispositivos
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
                                title="Abrir App"
                            )
                        ]
                    )
                )
            )
            
            response = messaging.send_multicast(message)
            
            # Log resultados
            logger.info(f"Push enviado: {response.success_count} sucessos, {response.failure_count} falhas")
            
            return response.success_count > 0
            
        except Exception as e:
            logger.error(f"Erro ao enviar push notification: {e}")
            return False
    
    async def register_device(
        self,
        user_id: UUID,
        device_token: str,
        device_info: Dict
    ) -> bool:
        """
        Registra dispositivo para receber notificações
        """
        try:
            # Salvar token no banco
            await self.save_device_token(user_id, device_token, device_info)
            return True
        except Exception as e:
            logger.error(f"Erro ao registrar dispositivo: {e}")
            return False
```

## 6. Templates de Notificação

### 6.1 Tipos de Notificação

```python
# notification_types.py
class NotificationTypes:
    # Atualizações de vagas
    JOB_STATUS_CHANGED = "job_status_changed"
    NEW_JOB_MATCH = "new_job_match"
    JOB_DEADLINE_REMINDER = "job_deadline_reminder"
    
    # Análise de CV
    CV_ANALYSIS_COMPLETE = "cv_analysis_complete"
    CV_OPTIMIZATION_SUGGESTION = "cv_optimization_suggestion"
    
    # Coach IA
    COACH_WEEKLY_TIPS = "coach_weekly_tips"
    COACH_INTERVIEW_PREP = "coach_interview_prep"
    
    # Sistema
    SUBSCRIPTION_EXPIRING = "subscription_expiring"
    WELCOME_MESSAGE = "welcome_message"
    FEATURE_ANNOUNCEMENT = "feature_announcement"
    
    # Lembretes
    DAILY_ACTIVITY_REMINDER = "daily_activity_reminder"
    WEEKLY_PROGRESS_SUMMARY = "weekly_progress_summary"
```

### 6.2 Templates de Exemplo

```json
{
  "type": "job_status_changed",
  "channel": "push",
  "language": "pt-BR",
  "subject_template": "Atualização na vaga: {{ job_title }}",
  "content_template": "Sua candidatura para {{ job_title }} na {{ company_name }} foi atualizada para: {{ new_status }}",
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
  "language": "pt-BR",
  "subject_template": "Sua análise de CV está pronta! 📄✨",
  "content_template": "<h2>Olá {{ user_name }}!</h2><p>Sua análise de CV foi concluída com uma pontuação de <strong>{{ score }}/100</strong>.</p><p>Principais melhorias sugeridas:</p><ul>{% for suggestion in suggestions %}<li>{{ suggestion }}</li>{% endfor %}</ul><p><a href='{{ cv_url }}'>Ver análise completa</a></p>",
  "variables": {
    "user_name": "string",
    "score": "number",
    "suggestions": "array",
    "cv_url": "string"
  }
}
```

## 7. Configurações e Preferências

### 7.1 Preferências Padrão

```python
# default_preferences.py
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

### 7.2 Interface de Configuração (Flutter)

```dart
// notification_settings_page.dart
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
        title: Text('Configurações de Notificação'),
      ),
      body: ListView(
        children: [
          _buildSectionHeader('Atualizações de Vagas'),
          _buildNotificationTile(
            'job_status_changed',
            'Mudanças de status',
            'Receba atualizações quando o status de suas candidaturas mudar'
          ),
          _buildNotificationTile(
            'new_job_match',
            'Novas vagas compatíveis',
            'Seja notificado sobre vagas que combinam com seu perfil'
          ),
          
          _buildSectionHeader('Análise de CV'),
          _buildNotificationTile(
            'cv_analysis_complete',
            'Análise concluída',
            'Receba o resultado da análise do seu currículo'
          ),
          
          _buildSectionHeader('Coach IA'),
          _buildNotificationTile(
            'coach_weekly_tips',
            'Dicas semanais',
            'Receba dicas personalizadas para melhorar sua busca'
          ),
          
          _buildSectionHeader('Lembretes'),
          _buildNotificationTile(
            'daily_activity_reminder',
            'Lembrete diário',
            'Lembre-se de manter sua busca ativa'
          ),
          
          _buildQuietHoursSection(),
        ],
      ),
    );
  }
  
  Widget _buildNotificationTile(
    String type,
    String title,
    String description
  ) {
    final preference = _preferences[type];
    if (preference == null) return SizedBox.shrink();
    
    return ExpansionTile(
      title: Text(title),
      subtitle: Text(description),
      children: [
        SwitchListTile(
          title: Text('Notificações no app'),
          value: preference.inAppEnabled,
          onChanged: (value) => _updatePreference(type, 'in_app', value),
        ),
        SwitchListTile(
          title: Text('Notificações por email'),
          value: preference.emailEnabled,
          onChanged: (value) => _updatePreference(type, 'email', value),
        ),
        SwitchListTile(
          title: Text('Notificações push'),
          value: preference.pushEnabled,
          onChanged: (value) => _updatePreference(type, 'push', value),
        ),
        ListTile(
          title: Text('Frequência'),
          trailing: DropdownButton<String>(
            value: preference.frequency,
            items: [
              DropdownMenuItem(value: 'immediate', child: Text('Imediato')),
              DropdownMenuItem(value: 'daily', child: Text('Diário')),
              DropdownMenuItem(value: 'weekly', child: Text('Semanal')),
              DropdownMenuItem(value: 'disabled', child: Text('Desabilitado')),
            ],
            onChanged: (value) => _updatePreference(type, 'frequency', value),
          ),
        ),
      ],
    );
  }
}
```

## 8. Monitoramento e Analytics

### 8.1 Métricas de Entrega

```python
# notification_analytics.py
class NotificationAnalytics:
    """
    Analytics para sistema de notificações
    """
    
    async def get_delivery_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """
        Métricas de entrega por canal e tipo
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
        ORDER BY n.type, nl.channel
        """
        
        results = await self.db.fetch_all(query, [start_date, end_date])
        return self._format_delivery_metrics(results)
    
    async def get_engagement_metrics(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """
        Métricas de engajamento (abertura, cliques)
        """
        query = """
        SELECT 
            type,
            COUNT(*) as total_sent,
            COUNT(read_at) as total_read,
            ROUND(COUNT(read_at)::numeric / COUNT(*)::numeric * 100, 2) as read_rate
        FROM notifications
        WHERE created_at BETWEEN %s AND %s
        AND status = 'sent'
        GROUP BY type
        ORDER BY read_rate DESC
        """
        
        results = await self.db.fetch_all(query, [start_date, end_date])
        return self._format_engagement_metrics(results)
```

### 8.2 Dashboard de Monitoramento

```python
# monitoring_dashboard.py
@router.get("/admin/notifications/dashboard")
async def get_notification_dashboard(
    start_date: datetime = Query(...),
    end_date: datetime = Query(...),
    current_user: User = Depends(get_admin_user)
):
    """
    Dashboard administrativo para monitoramento de notificações
    """
    analytics = NotificationAnalytics()
    
    return {
        "delivery_metrics": await analytics.get_delivery_metrics(start_date, end_date),
        "engagement_metrics": await analytics.get_engagement_metrics(start_date, end_date),
        "error_summary": await analytics.get_error_summary(start_date, end_date),
        "top_performing_templates": await analytics.get_top_templates(start_date, end_date)
    }
```

## 9. Tratamento de Erros e Retry

### 9.1 Estratégia de Retry

```python
# retry_handler.py
from tenacity import retry, stop_after_attempt, wait_exponential

class NotificationRetryHandler:
    """
    Handler para retry de notificações falhadas
    """
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def send_with_retry(
        self,
        handler: Any,
        notification: Notification
    ) -> bool:
        """
        Envia notificação com retry automático
        """
        try:
            result = await handler.send_notification(notification)
            if result:
                await self._log_success(notification.id, handler.channel)
                return True
            else:
                await self._log_failure(notification.id, handler.channel, "Send failed")
                raise Exception("Send failed")
                
        except Exception as e:
            await self._log_failure(notification.id, handler.channel, str(e))
            raise
    
    async def process_failed_notifications(self):
        """
        Processa notificações falhadas para retry
        """
        failed_notifications = await self._get_failed_notifications()
        
        for notification in failed_notifications:
            try:
                await self.send_with_retry(
                    self._get_handler(notification.channel),
                    notification
                )
            except Exception as e:
                logger.error(f"Falha definitiva na notificação {notification.id}: {e}")
                await self._mark_as_permanently_failed(notification.id)
```

## 10. Segurança e Privacidade

### 10.1 Proteção de Dados

```python
# security.py
class NotificationSecurity:
    """
    Implementações de segurança para notificações
    """
    
    def sanitize_content(self, content: str) -> str:
        """
        Sanitiza conteúdo para prevenir XSS
        """
        return bleach.clean(
            content,
            tags=['b', 'i', 'u', 'strong', 'em'],
            strip=True
        )
    
    def encrypt_sensitive_data(self, data: Dict) -> Dict:
        """
        Criptografa dados sensíveis antes de armazenar
        """
        sensitive_fields = ['email', 'phone', 'personal_info']
        
        for field in sensitive_fields:
            if field in data:
                data[field] = self.encryption_service.encrypt(data[field])
        
        return data
    
    async def validate_user_permissions(
        self,
        user_id: UUID,
        notification_id: UUID
    ) -> bool:
        """
        Valida se usuário tem permissão para acessar notificação
        """
        notification = await self.get_notification(notification_id)
        return notification and notification.user_id == user_id
```

### 10.2 Rate Limiting

```python
# rate_limiting.py
class NotificationRateLimiter:
    """
    Rate limiting para prevenir spam de notificações
    """
    
    def __init__(self):
        self.redis_client = get_redis_client()
    
    async def check_rate_limit(
        self,
        user_id: UUID,
        notification_type: str
    ) -> bool:
        """
        Verifica se usuário não excedeu limite de notificações
        """
        key = f"notification_rate:{user_id}:{notification_type}"
        
        # Limites por tipo
        limits = {
            "job_status_changed": {"count": 10, "window": 3600},  # 10 por hora
            "new_job_match": {"count": 5, "window": 3600},        # 5 por hora
            "daily_reminder": {"count": 1, "window": 86400},      # 1 por dia
        }
        
        limit_config = limits.get(notification_type, {"count": 20, "window": 3600})
        
        current_count = await self.redis_client.get(key)
        if current_count and int(current_count) >= limit_config["count"]:
            return False
        
        # Incrementar contador
        pipe = self.redis_client.pipeline()
        pipe.incr(key)
        pipe.expire(key, limit_config["window"])
        await pipe.execute()
        
        return True
```

## 11. Testes

### 11.1 Testes Unitários

```python
# test_notification_service.py
import pytest
from unittest.mock import AsyncMock, patch

class TestNotificationService:
    """
    Testes para o serviço de notificações
    """
    
    @pytest.fixture
    def notification_service(self):
        return NotificationService()
    
    @pytest.mark.asyncio
    async def test_create_notification_success(self, notification_service):
        """
        Testa criação bem-sucedida de notificação
        """
        user_id = uuid4()
        
        notification = await notification_service.create_notification(
            user_id=user_id,
            notification_type="job_status_changed",
            title="Teste",
            content="Conteúdo de teste",
            channels=["in_app", "email"]
        )
        
        assert notification.user_id == user_id
        assert notification.type == "job_status_changed"
        assert notification.title == "Teste"
        assert "in_app" in notification.channels
        assert "email" in notification.channels
    
    @pytest.mark.asyncio
    async def test_send_notification_respects_preferences(self, notification_service):
        """
        Testa se notificação respeita preferências do usuário
        """
        user_id = uuid4()
        
        # Mock preferências - apenas email habilitado
        with patch.object(
            notification_service.preference_manager,
            'get_user_preferences',
            return_value={
                "job_status_changed": {
                    "in_app_enabled": False,
                    "email_enabled": True,
                    "push_enabled": False
                }
            }
        ):
            notification = await notification_service.create_notification(
                user_id=user_id,
                notification_type="job_status_changed",
                title="Teste",
                content="Conteúdo",
                channels=["in_app", "email", "push"]
            )
            
            result = await notification_service.send_notification(notification.id)
            
            # Verificar que apenas email foi enviado
            assert result["email"] == True
            assert result["in_app"] == False
            assert result["push"] == False
    
    @pytest.mark.asyncio
    async def test_rate_limiting(self, notification_service):
        """
        Testa rate limiting de notificações
        """
        user_id = uuid4()
        
        # Simular múltiplas notificações do mesmo tipo
        for i in range(12):  # Limite é 10 por hora
            result = await notification_service.check_rate_limit(
                user_id,
                "job_status_changed"
            )
            
            if i < 10:
                assert result == True
            else:
                assert result == False
```

### 11.2 Testes de Integração

```python
# test_notification_integration.py
import pytest
from httpx import AsyncClient

class TestNotificationIntegration:
    """
    Testes de integração para APIs de notificação
    """
    
    @pytest.mark.asyncio
    async def test_get_notifications_endpoint(self, client: AsyncClient, auth_headers):
        """
        Testa endpoint de recuperação de notificações
        """
        response = await client.get(
            "/api/v1/notifications",
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "notifications" in data
        assert "total" in data
        assert "unread_count" in data
    
    @pytest.mark.asyncio
    async def test_update_preferences_endpoint(self, client: AsyncClient, auth_headers):
        """
        Testa endpoint de atualização de preferências
        """
        preferences_data = {
            "job_status_changed": {
                "in_app_enabled": True,
                "email_enabled": False,
                "push_enabled": True,
                "frequency": "immediate"
            }
        }
        
        response = await client.put(
            "/api/v1/notifications/preferences",
            json=preferences_data,
            headers=auth_headers
        )
        
        assert response.status_code == 200
        
        # Verificar se preferências foram salvas
        get_response = await client.get(
            "/api/v1/notifications/preferences",
            headers=auth_headers
        )
        
        assert get_response.status_code == 200
        saved_prefs = get_response.json()
        assert saved_prefs["job_status_changed"]["email_enabled"] == False
```

## 12. Deploy e Configuração

### 12.1 Variáveis de Ambiente

```bash
# .env
# Firebase Configuration
FIREBASE_PROJECT_ID=recoloca-ai
FIREBASE_PRIVATE_KEY_ID=your_private_key_id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@recoloca-ai.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=your_client_id
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token

# Email Configuration (Supabase)
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key

# Notification Settings
NOTIFICATION_RATE_LIMIT_REDIS_URL=redis://localhost:6379
NOTIFICATION_BATCH_SIZE=100
NOTIFICATION_RETRY_ATTEMPTS=3
NOTIFICATION_RETRY_DELAY=5

# Template Settings
NOTIFICATION_TEMPLATE_DIR=templates/notifications
DEFAULT_LANGUAGE=pt-BR
```

### 12.2 Docker Configuration

```dockerfile
# Dockerfile.notifications
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/notifications/ ./notifications/
COPY templates/ ./templates/

# Configurar usuário não-root
RUN useradd --create-home --shell /bin/bash app
USER app

# Comando padrão
CMD ["python", "-m", "notifications.worker"]
```

### 12.3 Worker para Processamento Assíncrono

```python
# notification_worker.py
import asyncio
from celery import Celery
from datetime import datetime, timedelta

app = Celery('notifications')
app.config_from_object('celeryconfig')

@app.task
async def send_notification_task(notification_id: str):
    """
    Task assíncrona para envio de notificação
    """
    notification_service = NotificationService()
    await notification_service.send_notification(UUID(notification_id))

@app.task
async def process_scheduled_notifications():
    """
    Processa notificações agendadas
    """
    notification_service = NotificationService()
    
    # Buscar notificações agendadas para agora
    scheduled = await notification_service.get_scheduled_notifications(
        datetime.utcnow()
    )
    
    for notification in scheduled:
        send_notification_task.delay(str(notification.id))

@app.task
async def cleanup_old_notifications():
    """
    Limpa notificações antigas (>90 dias)
    """
    cutoff_date = datetime.utcnow() - timedelta(days=90)
    notification_service = NotificationService()
    await notification_service.cleanup_old_notifications(cutoff_date)

# Configurar tarefas periódicas
app.conf.beat_schedule = {
    'process-scheduled-notifications': {
        'task': 'notifications.worker.process_scheduled_notifications',
        'schedule': 60.0,  # A cada minuto
    },
    'cleanup-old-notifications': {
        'task': 'notifications.worker.cleanup_old_notifications',
        'schedule': 86400.0,  # Diário
    },
}
```

## 13. Roadmap e Evoluções Futuras

### 13.1 Fase 1 - MVP (Should Have)
- ✅ Notificações in-app básicas
- ✅ Notificações por email
- ✅ Notificações push PWA
- ✅ Preferências básicas de usuário
- ✅ Templates essenciais

### 13.2 Fase 2 - Melhorias (Could Have)
- 🔄 Notificações SMS via Twilio
- 🔄 Segmentação avançada de usuários
- 🔄 A/B testing de templates
- 🔄 Analytics avançado de engajamento
- 🔄 Personalização baseada em ML

### 13.3 Fase 3 - Avançado (Won't Have para MVP)
- ⏳ Notificações rich media (imagens, vídeos)
- ⏳ Integração com calendário
- ⏳ Notificações baseadas em localização
- ⏳ Chatbot integrado para notificações
- ⏳ API pública para integrações

## 14. Considerações de Performance

### 14.1 Otimizações

```python
# performance_optimizations.py
class NotificationPerformanceOptimizer:
    """
    Otimizações de performance para sistema de notificações
    """
    
    async def batch_send_notifications(
        self,
        notifications: List[Notification],
        batch_size: int = 100
    ):
        """
        Envia notificações em lotes para melhor performance
        """
        for i in range(0, len(notifications), batch_size):
            batch = notifications[i:i + batch_size]
            await asyncio.gather(*[
                self.send_notification(notification)
                for notification in batch
            ])
    
    async def cache_user_preferences(self, user_id: UUID) -> Dict:
        """
        Cache de preferências do usuário para reduzir consultas ao DB
        """
        cache_key = f"user_preferences:{user_id}"
        
        # Tentar buscar do cache primeiro
        cached = await self.redis_client.get(cache_key)
        if cached:
            return json.loads(cached)
        
        # Buscar do banco e cachear
        preferences = await self.get_user_preferences_from_db(user_id)
        await self.redis_client.setex(
            cache_key,
            3600,  # 1 hora
            json.dumps(preferences)
        )
        
        return preferences
    
    async def preload_templates(self):
        """
        Pré-carrega templates em memória para acesso rápido
        """
        templates = await self.get_all_templates()
        self.template_cache = {
            f"{t.type}_{t.channel}_{t.language}": t
            for t in templates
        }
```

### 14.2 Monitoramento de Performance

```python
# performance_monitoring.py
import time
from functools import wraps

def monitor_performance(func):
    """
    Decorator para monitorar performance de funções
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        
        try:
            result = await func(*args, **kwargs)
            execution_time = time.time() - start_time
            
            # Log métricas
            logger.info(f"{func.__name__} executado em {execution_time:.2f}s")
            
            # Enviar para sistema de métricas (Prometheus, etc.)
            metrics.histogram(
                'notification_function_duration',
                execution_time,
                tags={'function': func.__name__}
            )
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            logger.error(f"{func.__name__} falhou após {execution_time:.2f}s: {e}")
            
            metrics.counter(
                'notification_function_errors',
                tags={'function': func.__name__, 'error': str(e)}
            )
            
            raise
    
    return wrapper
```

---

## Conclusão

Este LLD define uma arquitetura robusta e escalável para o Sistema de Notificações do Recoloca.ai, utilizando Firebase Cloud Messaging como base para notificações push PWA. O sistema foi projetado para:

- **Maximizar o Engajamento:** Através de notificações personalizadas e oportunas
- **Respeitar Preferências:** Com controle granular pelo usuário
- **Garantir Confiabilidade:** Com retry automático e monitoramento
- **Escalar Eficientemente:** Com processamento assíncrono e cache
- **Manter Segurança:** Com validação, sanitização e rate limiting

A implementação seguirá uma abordagem incremental, começando com as funcionalidades "Should Have" para o MVP e evoluindo conforme feedback dos usuários e necessidades do negócio.

**Próximos Passos:**
1. Implementar modelos de dados no Supabase
2. Configurar Firebase Cloud Messaging
3. Desenvolver handlers básicos (in-app, email, push)
4. Criar templates iniciais
5. Implementar APIs REST
6. Desenvolver interface de configuração no Flutter
7. Configurar monitoramento e analytics
8. Testes e validação com usuários beta

## Documentos Relacionados

- [[docs/01_Guias_Centrais/01_PLANO_MESTRE_RECOLOCA_AI.md]] (v1.1) - Plano mestre do projeto
- [[docs/02_Requisitos/01_ERS.md]] (v1.1) - Especificação de requisitos
- [[docs/03_Arquitetura_e_Design/01_HLD.md]] (v1.1) - Arquitetura de alto nível
- [[docs/04_Agentes_IA/01_AGENTES_IA_MENTORES_OVERVIEW.md]] - Visão geral dos agentes
- [[docs/03_Arquitetura_e_Design/02_ADRs/ADR-001_Ferramentas_Core.md]] (v1.1) - Ferramentas Core

## Considerações de Orquestração Inteligente

### Integração com Metodologia v1.1
- **Agentes Production-Ready**: Sistema de notificações inteligentes via agentes especializados
- **Métricas Contínuas**: Tracking de engajamento e eficácia das notificações
- **RAG Operacional**: Personalização de conteúdo baseada em perfil do usuário
- **Specialized Intelligence**: Otimização de timing e conteúdo via agentes de comunicação

### Critérios de Validação
- ✅ **Entrega**: Taxa de entrega > 95%
- ✅ **Engajamento**: Taxa de abertura > 25%
- ✅ **Performance**: Latência < 500ms
- ✅ **Personalização**: Relevância > 80% (feedback usuário)

## Histórico de Versões

### v1.1 (Junho 2025) - Orquestração Inteligente e Specialized Intelligence
- Atualização de referências para documentos v1.1
- Alinhamento com metodologia de Orquestração Inteligente
- Adição de considerações específicas para agentes Production-Ready
- Integração com métricas de engajamento e personalização

### v1.0 (Junho 2025) - Versão Inicial
- Definição da arquitetura base do sistema de notificações
- Estabelecimento de componentes principais
- Integração inicial com agentes de IA

**Nota:** Este documento (v1.1) está totalmente alinhado com a metodologia de "Orquestração Inteligente" e "Specialized Intelligence" definida no [[docs/01_Guias_Centrais/02_GUIA_AVANCADO.md]] (v1.1), incorporando notificações inteligentes e personalizadas via agentes especializados.

---

**FIM DO DOCUMENTO LLD_Sistema_Notificacoes.md (v1.1)**