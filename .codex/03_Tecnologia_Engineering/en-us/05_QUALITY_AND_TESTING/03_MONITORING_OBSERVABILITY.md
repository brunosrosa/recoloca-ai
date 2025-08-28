---
title: "Monitoring and Observability for Recoloca.ai Platform"
doc_id: "MONITORING-OBSERVABILITY-RECOLOCA-AI"
version: "1.0"
last_updated: "2025-01-20"
status: "Active"
owner: "@DevOpsTeam"
tags: [monitoring, observability, metrics, logging, alerting, performance]
description: "Comprehensive monitoring and observability strategy covering metrics collection, logging, tracing, alerting, and dashboards for the Recoloca.ai platform."
---

# 📊 Monitoring and Observability - Recoloca.ai Platform

## 📋 Overview

This document outlines the comprehensive monitoring and observability strategy for the Recoloca.ai platform, implementing the three pillars of observability: metrics, logs, and traces.

### Objectives

- **Proactive Monitoring**: Detect issues before they impact users
- **Performance Optimization**: Identify and resolve performance bottlenecks
- **Reliability**: Ensure high availability and quick incident response
- **User Experience**: Monitor and improve user journey metrics
- **Business Intelligence**: Track key business metrics and KPIs
- **Compliance**: Meet regulatory and audit requirements

---

## 🏗️ Observability Architecture

### Three Pillars of Observability

#### 1. Metrics (What is happening?)
- **Application Metrics**: Response times, throughput, error rates
- **Infrastructure Metrics**: CPU, memory, disk, network usage
- **Business Metrics**: User registrations, CV analyses, subscriptions
- **Custom Metrics**: Feature usage, conversion rates, user engagement

#### 2. Logs (What happened?)
- **Application Logs**: Structured application events and errors
- **Access Logs**: HTTP requests and API calls
- **Security Logs**: Authentication, authorization, and security events
- **Audit Logs**: Data changes and compliance tracking

#### 3. Traces (How did it happen?)
- **Distributed Tracing**: Request flow across microservices
- **Performance Tracing**: Detailed timing of operations
- **Error Tracing**: Root cause analysis for failures
- **User Journey Tracing**: End-to-end user experience tracking

---

## 📈 Metrics Collection and Storage

### Prometheus Configuration

```yaml
# prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - "alert_rules.yml"
  - "recording_rules.yml"

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - alertmanager:9093

scrape_configs:
  # Application metrics
  - job_name: 'recoloca-backend'
    static_configs:
      - targets: ['backend:8000']
    metrics_path: '/metrics'
    scrape_interval: 10s
    scrape_timeout: 5s

  - job_name: 'recoloca-frontend'
    static_configs:
      - targets: ['frontend:3000']
    metrics_path: '/api/metrics'
    scrape_interval: 30s

  # Infrastructure metrics
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'postgres-exporter'
    static_configs:
      - targets: ['postgres-exporter:9187']

  - job_name: 'redis-exporter'
    static_configs:
      - targets: ['redis-exporter:9121']

  # Container metrics
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
```

### Application Metrics Implementation

#### Backend Metrics (Python/FastAPI)
```python
# src/monitoring/metrics.py
from prometheus_client import Counter, Histogram, Gauge, generate_latest
from fastapi import Request, Response
import time
from typing import Callable

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_DURATION = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

ACTIVE_CONNECTIONS = Gauge(
    'active_connections',
    'Number of active connections'
)

CV_ANALYSES_TOTAL = Counter(
    'cv_analyses_total',
    'Total number of CV analyses',
    ['status', 'user_type']
)

CV_ANALYSIS_DURATION = Histogram(
    'cv_analysis_duration_seconds',
    'CV analysis processing time in seconds',
    buckets=[0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0]
)

USER_REGISTRATIONS = Counter(
    'user_registrations_total',
    'Total user registrations',
    ['source', 'plan_type']
)

SUBSCRIPTION_EVENTS = Counter(
    'subscription_events_total',
    'Subscription events',
    ['event_type', 'plan_type']
)

DATABASE_CONNECTIONS = Gauge(
    'database_connections_active',
    'Active database connections'
)

REDIS_OPERATIONS = Counter(
    'redis_operations_total',
    'Redis operations',
    ['operation', 'status']
)

# Middleware for automatic metrics collection
async def metrics_middleware(request: Request, call_next: Callable) -> Response:
    start_time = time.time()
    
    # Increment active connections
    ACTIVE_CONNECTIONS.inc()
    
    try:
        response = await call_next(request)
        
        # Record metrics
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status_code=response.status_code
        ).inc()
        
        REQUEST_DURATION.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(time.time() - start_time)
        
        return response
    
    finally:
        ACTIVE_CONNECTIONS.dec()

# Custom metrics for business logic
class MetricsCollector:
    @staticmethod
    def record_cv_analysis(duration: float, status: str, user_type: str):
        CV_ANALYSES_TOTAL.labels(status=status, user_type=user_type).inc()
        CV_ANALYSIS_DURATION.observe(duration)
    
    @staticmethod
    def record_user_registration(source: str, plan_type: str):
        USER_REGISTRATIONS.labels(source=source, plan_type=plan_type).inc()
    
    @staticmethod
    def record_subscription_event(event_type: str, plan_type: str):
        SUBSCRIPTION_EVENTS.labels(event_type=event_type, plan_type=plan_type).inc()
    
    @staticmethod
    def update_database_connections(count: int):
        DATABASE_CONNECTIONS.set(count)
    
    @staticmethod
    def record_redis_operation(operation: str, status: str):
        REDIS_OPERATIONS.labels(operation=operation, status=status).inc()

# Metrics endpoint
@app.get("/metrics")
async def get_metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
```

#### Frontend Metrics (React/TypeScript)
```typescript
// src/monitoring/metrics.ts
interface MetricData {
  name: string;
  value: number;
  labels?: Record<string, string>;
  timestamp?: number;
}

class MetricsCollector {
  private metrics: MetricData[] = [];
  private endpoint = '/api/metrics';
  private batchSize = 10;
  private flushInterval = 30000; // 30 seconds

  constructor() {
    this.startPeriodicFlush();
    this.setupPerformanceObserver();
    this.setupErrorTracking();
  }

  // Record custom metrics
  recordMetric(name: string, value: number, labels?: Record<string, string>) {
    this.metrics.push({
      name,
      value,
      labels,
      timestamp: Date.now()
    });

    if (this.metrics.length >= this.batchSize) {
      this.flush();
    }
  }

  // Track page views
  trackPageView(page: string, userId?: string) {
    this.recordMetric('page_views_total', 1, {
      page,
      user_id: userId || 'anonymous'
    });
  }

  // Track user interactions
  trackUserAction(action: string, component: string, userId?: string) {
    this.recordMetric('user_actions_total', 1, {
      action,
      component,
      user_id: userId || 'anonymous'
    });
  }

  // Track API calls
  trackApiCall(endpoint: string, method: string, status: number, duration: number) {
    this.recordMetric('api_calls_total', 1, {
      endpoint,
      method,
      status: status.toString()
    });

    this.recordMetric('api_call_duration_ms', duration, {
      endpoint,
      method
    });
  }

  // Track errors
  trackError(error: Error, component?: string, userId?: string) {
    this.recordMetric('frontend_errors_total', 1, {
      error_type: error.name,
      component: component || 'unknown',
      user_id: userId || 'anonymous'
    });
  }

  // Setup performance observer
  private setupPerformanceObserver() {
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        list.getEntries().forEach((entry) => {
          if (entry.entryType === 'navigation') {
            const navEntry = entry as PerformanceNavigationTiming;
            this.recordMetric('page_load_time_ms', navEntry.loadEventEnd - navEntry.fetchStart);
            this.recordMetric('dom_content_loaded_ms', navEntry.domContentLoadedEventEnd - navEntry.fetchStart);
          }

          if (entry.entryType === 'largest-contentful-paint') {
            this.recordMetric('largest_contentful_paint_ms', entry.startTime);
          }

          if (entry.entryType === 'first-input') {
            const fidEntry = entry as PerformanceEventTiming;
            this.recordMetric('first_input_delay_ms', fidEntry.processingStart - fidEntry.startTime);
          }
        });
      });

      observer.observe({ entryTypes: ['navigation', 'largest-contentful-paint', 'first-input'] });
    }
  }

  // Setup error tracking
  private setupErrorTracking() {
    window.addEventListener('error', (event) => {
      this.trackError(event.error, 'global');
    });

    window.addEventListener('unhandledrejection', (event) => {
      this.trackError(new Error(event.reason), 'promise');
    });
  }

  // Flush metrics to backend
  private async flush() {
    if (this.metrics.length === 0) return;

    const metricsToSend = [...this.metrics];
    this.metrics = [];

    try {
      await fetch(this.endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ metrics: metricsToSend })
      });
    } catch (error) {
      console.error('Failed to send metrics:', error);
      // Re-add metrics to queue for retry
      this.metrics.unshift(...metricsToSend);
    }
  }

  // Start periodic flush
  private startPeriodicFlush() {
    setInterval(() => {
      this.flush();
    }, this.flushInterval);
  }
}

// Export singleton instance
export const metricsCollector = new MetricsCollector();

// React hook for tracking component metrics
export const useMetrics = () => {
  const trackPageView = useCallback((page: string) => {
    metricsCollector.trackPageView(page);
  }, []);

  const trackUserAction = useCallback((action: string, component: string) => {
    metricsCollector.trackUserAction(action, component);
  }, []);

  const trackError = useCallback((error: Error, component?: string) => {
    metricsCollector.trackError(error, component);
  }, []);

  return {
    trackPageView,
    trackUserAction,
    trackError
  };
};
```

---

## 📝 Structured Logging

### Backend Logging (Python)
```python
# src/logging/config.py
import logging
import json
from datetime import datetime
from typing import Any, Dict
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]):
        super().add_fields(log_record, record, message_dict)
        
        # Add standard fields
        log_record['timestamp'] = datetime.utcnow().isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['service'] = 'recoloca-backend'
        log_record['version'] = '1.0.0'
        
        # Add request context if available
        if hasattr(record, 'request_id'):
            log_record['request_id'] = record.request_id
        if hasattr(record, 'user_id'):
            log_record['user_id'] = record.user_id
        if hasattr(record, 'trace_id'):
            log_record['trace_id'] = record.trace_id

# Configure logging
def setup_logging():
    formatter = CustomJsonFormatter(
        '%(timestamp)s %(level)s %(logger)s %(message)s'
    )
    
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    
    # Application loggers
    app_logger = logging.getLogger('recoloca')
    app_logger.setLevel(logging.DEBUG)
    
    # Third-party loggers
    logging.getLogger('uvicorn').setLevel(logging.INFO)
    logging.getLogger('sqlalchemy').setLevel(logging.WARNING)

# Structured logging utilities
class StructuredLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
    
    def info(self, message: str, **kwargs):
        extra = self._build_extra(**kwargs)
        self.logger.info(message, extra=extra)
    
    def warning(self, message: str, **kwargs):
        extra = self._build_extra(**kwargs)
        self.logger.warning(message, extra=extra)
    
    def error(self, message: str, error: Exception = None, **kwargs):
        extra = self._build_extra(**kwargs)
        if error:
            extra['error_type'] = type(error).__name__
            extra['error_message'] = str(error)
        self.logger.error(message, extra=extra, exc_info=error)
    
    def debug(self, message: str, **kwargs):
        extra = self._build_extra(**kwargs)
        self.logger.debug(message, extra=extra)
    
    def _build_extra(self, **kwargs) -> Dict[str, Any]:
        return {k: v for k, v in kwargs.items() if v is not None}

# Usage examples
logger = StructuredLogger('recoloca.cv_analysis')

# Log CV analysis start
logger.info(
    "CV analysis started",
    user_id="user123",
    analysis_id="analysis456",
    file_size=1024000,
    file_type="pdf"
)

# Log successful analysis
logger.info(
    "CV analysis completed successfully",
    user_id="user123",
    analysis_id="analysis456",
    score=85,
    processing_time_ms=2500,
    suggestions_count=5
)

# Log error
try:
    # Some operation
    pass
except Exception as e:
    logger.error(
        "CV analysis failed",
        user_id="user123",
        analysis_id="analysis456",
        error=e,
        retry_count=2
    )
```

### Frontend Logging (TypeScript)
```typescript
// src/logging/logger.ts
interface LogEntry {
  timestamp: string;
  level: 'debug' | 'info' | 'warn' | 'error';
  message: string;
  service: string;
  version: string;
  context?: Record<string, any>;
  error?: {
    name: string;
    message: string;
    stack?: string;
  };
  user_id?: string;
  session_id?: string;
  request_id?: string;
}

class Logger {
  private service = 'recoloca-frontend';
  private version = '1.0.0';
  private logEndpoint = '/api/logs';
  private logBuffer: LogEntry[] = [];
  private maxBufferSize = 50;
  private flushInterval = 10000; // 10 seconds

  constructor() {
    this.startPeriodicFlush();
  }

  debug(message: string, context?: Record<string, any>) {
    this.log('debug', message, context);
  }

  info(message: string, context?: Record<string, any>) {
    this.log('info', message, context);
  }

  warn(message: string, context?: Record<string, any>) {
    this.log('warn', message, context);
  }

  error(message: string, error?: Error, context?: Record<string, any>) {
    const errorInfo = error ? {
      name: error.name,
      message: error.message,
      stack: error.stack
    } : undefined;

    this.log('error', message, context, errorInfo);
  }

  private log(
    level: LogEntry['level'],
    message: string,
    context?: Record<string, any>,
    error?: LogEntry['error']
  ) {
    const entry: LogEntry = {
      timestamp: new Date().toISOString(),
      level,
      message,
      service: this.service,
      version: this.version,
      context,
      error,
      user_id: this.getCurrentUserId(),
      session_id: this.getSessionId(),
      request_id: this.getCurrentRequestId()
    };

    // Console output for development
    if (process.env.NODE_ENV === 'development') {
      console[level](message, context, error);
    }

    // Add to buffer for remote logging
    this.logBuffer.push(entry);

    if (this.logBuffer.length >= this.maxBufferSize) {
      this.flush();
    }
  }

  private async flush() {
    if (this.logBuffer.length === 0) return;

    const logsToSend = [...this.logBuffer];
    this.logBuffer = [];

    try {
      await fetch(this.logEndpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ logs: logsToSend })
      });
    } catch (error) {
      console.error('Failed to send logs:', error);
      // Re-add logs to buffer for retry
      this.logBuffer.unshift(...logsToSend);
    }
  }

  private startPeriodicFlush() {
    setInterval(() => {
      this.flush();
    }, this.flushInterval);
  }

  private getCurrentUserId(): string | undefined {
    // Get from auth context or local storage
    return localStorage.getItem('user_id') || undefined;
  }

  private getSessionId(): string | undefined {
    // Get or generate session ID
    let sessionId = sessionStorage.getItem('session_id');
    if (!sessionId) {
      sessionId = crypto.randomUUID();
      sessionStorage.setItem('session_id', sessionId);
    }
    return sessionId;
  }

  private getCurrentRequestId(): string | undefined {
    // Get from current request context if available
    return undefined;
  }
}

// Export singleton instance
export const logger = new Logger();

// React hook for component logging
export const useLogger = (componentName: string) => {
  const logWithContext = useCallback((level: 'debug' | 'info' | 'warn' | 'error', message: string, context?: Record<string, any>, error?: Error) => {
    const fullContext = {
      component: componentName,
      ...context
    };

    if (level === 'error') {
      logger.error(message, error, fullContext);
    } else {
      logger[level](message, fullContext);
    }
  }, [componentName]);

  return {
    debug: (message: string, context?: Record<string, any>) => logWithContext('debug', message, context),
    info: (message: string, context?: Record<string, any>) => logWithContext('info', message, context),
    warn: (message: string, context?: Record<string, any>) => logWithContext('warn', message, context),
    error: (message: string, error?: Error, context?: Record<string, any>) => logWithContext('error', message, context, error)
  };
};
```

---

## 🔍 Distributed Tracing

### OpenTelemetry Configuration
```python
# src/tracing/config.py
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

def setup_tracing(app):
    # Configure tracer provider
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    
    # Configure Jaeger exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name="jaeger",
        agent_port=6831,
    )
    
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)
    
    # Instrument FastAPI
    FastAPIInstrumentor.instrument_app(app)
    
    # Instrument database
    SQLAlchemyInstrumentor().instrument()
    
    # Instrument Redis
    RedisInstrumentor().instrument()
    
    # Instrument HTTP requests
    RequestsInstrumentor().instrument()
    
    return tracer

# Custom tracing utilities
class TracingUtils:
    def __init__(self, tracer):
        self.tracer = tracer
    
    def trace_cv_analysis(self, user_id: str, analysis_id: str):
        return self.tracer.start_as_current_span(
            "cv_analysis",
            attributes={
                "user.id": user_id,
                "analysis.id": analysis_id,
                "service.name": "cv-analyzer"
            }
        )
    
    def trace_ai_interaction(self, user_id: str, session_id: str, message_type: str):
        return self.tracer.start_as_current_span(
            "ai_interaction",
            attributes={
                "user.id": user_id,
                "session.id": session_id,
                "message.type": message_type,
                "service.name": "ai-coach"
            }
        )
    
    def trace_payment_processing(self, user_id: str, payment_id: str, amount: float):
        return self.tracer.start_as_current_span(
            "payment_processing",
            attributes={
                "user.id": user_id,
                "payment.id": payment_id,
                "payment.amount": amount,
                "service.name": "payment-processor"
            }
        )
```

---

## 🚨 Alerting and Incident Response

### Alertmanager Configuration
```yaml
# alertmanager/alertmanager.yml
global:
  smtp_smarthost: 'smtp.gmail.com:587'
  smtp_from: 'alerts@recoloca.ai'
  smtp_auth_username: 'alerts@recoloca.ai'
  smtp_auth_password: '${SMTP_PASSWORD}'

route:
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 1h
  receiver: 'default'
  routes:
    - match:
        severity: critical
      receiver: 'critical-alerts'
    - match:
        severity: warning
      receiver: 'warning-alerts'

receivers:
  - name: 'default'
    email_configs:
      - to: 'devops@recoloca.ai'
        subject: '[Recoloca.ai] {{ .GroupLabels.alertname }}'
        body: |
          {{ range .Alerts }}
          Alert: {{ .Annotations.summary }}
          Description: {{ .Annotations.description }}
          Labels: {{ .Labels }}
          {{ end }}

  - name: 'critical-alerts'
    email_configs:
      - to: 'devops@recoloca.ai,cto@recoloca.ai'
        subject: '[CRITICAL] {{ .GroupLabels.alertname }}'
        body: |
          CRITICAL ALERT
          
          {{ range .Alerts }}
          Alert: {{ .Annotations.summary }}
          Description: {{ .Annotations.description }}
          Severity: {{ .Labels.severity }}
          Service: {{ .Labels.service }}
          Instance: {{ .Labels.instance }}
          
          Runbook: {{ .Annotations.runbook_url }}
          {{ end }}
    slack_configs:
      - api_url: '${SLACK_WEBHOOK_URL}'
        channel: '#alerts-critical'
        title: 'Critical Alert: {{ .GroupLabels.alertname }}'
        text: |
          {{ range .Alerts }}
          *Alert:* {{ .Annotations.summary }}
          *Description:* {{ .Annotations.description }}
          *Severity:* {{ .Labels.severity }}
          *Service:* {{ .Labels.service }}
          {{ end }}

  - name: 'warning-alerts'
    email_configs:
      - to: 'devops@recoloca.ai'
        subject: '[WARNING] {{ .GroupLabels.alertname }}'
    slack_configs:
      - api_url: '${SLACK_WEBHOOK_URL}'
        channel: '#alerts-warning'
        title: 'Warning: {{ .GroupLabels.alertname }}'
```

### Alert Rules
```yaml
# prometheus/alert_rules.yml
groups:
  - name: recoloca-backend
    rules:
      # High error rate
      - alert: HighErrorRate
        expr: |
          (
            sum(rate(http_requests_total{status_code=~"5.."}[5m])) by (service)
            /
            sum(rate(http_requests_total[5m])) by (service)
          ) > 0.05
        for: 2m
        labels:
          severity: critical
          service: backend
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }} for service {{ $labels.service }}"
          runbook_url: "https://runbooks.recoloca.ai/high-error-rate"

      # High response time
      - alert: HighResponseTime
        expr: |
          histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)) > 2
        for: 5m
        labels:
          severity: warning
          service: backend
        annotations:
          summary: "High response time detected"
          description: "95th percentile response time is {{ $value }}s for service {{ $labels.service }}"

      # Database connection issues
      - alert: DatabaseConnectionHigh
        expr: database_connections_active > 80
        for: 2m
        labels:
          severity: warning
          service: database
        annotations:
          summary: "High database connection count"
          description: "Database has {{ $value }} active connections"

      # CV analysis queue backup
      - alert: CVAnalysisQueueBackup
        expr: cv_analysis_queue_size > 100
        for: 5m
        labels:
          severity: warning
          service: cv-analyzer
        annotations:
          summary: "CV analysis queue backup"
          description: "CV analysis queue has {{ $value }} pending items"

      # Payment processing failures
      - alert: PaymentProcessingFailures
        expr: |
          sum(rate(payment_processing_total{status="failed"}[5m])) > 0.1
        for: 1m
        labels:
          severity: critical
          service: payments
        annotations:
          summary: "Payment processing failures detected"
          description: "Payment failure rate is {{ $value }} per second"

  - name: infrastructure
    rules:
      # High CPU usage
      - alert: HighCPUUsage
        expr: 100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage"
          description: "CPU usage is {{ $value }}% on {{ $labels.instance }}"

      # High memory usage
      - alert: HighMemoryUsage
        expr: |
          (
            node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes
          ) / node_memory_MemTotal_bytes * 100 > 85
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High memory usage"
          description: "Memory usage is {{ $value }}% on {{ $labels.instance }}"

      # Disk space low
      - alert: DiskSpaceLow
        expr: |
          (
            node_filesystem_avail_bytes{fstype!="tmpfs"} / node_filesystem_size_bytes{fstype!="tmpfs"}
          ) * 100 < 10
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "Low disk space"
          description: "Disk space is {{ $value }}% full on {{ $labels.instance }}"

      # Service down
      - alert: ServiceDown
        expr: up == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Service is down"
          description: "{{ $labels.job }} service is down on {{ $labels.instance }}"
```

---

## 📊 Dashboards and Visualization

### Grafana Dashboard Configuration
```json
{
  "dashboard": {
    "id": null,
    "title": "Recoloca.ai - Application Overview",
    "tags": ["recoloca", "overview"],
    "timezone": "browser",
    "panels": [
      {
        "id": 1,
        "title": "Request Rate",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m]))",
            "legendFormat": "Requests/sec"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "unit": "reqps",
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {"color": "green", "value": null},
                {"color": "yellow", "value": 100},
                {"color": "red", "value": 500}
              ]
            }
          }
        }
      },
      {
        "id": 2,
        "title": "Error Rate",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{status_code=~\"5..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100",
            "legendFormat": "Error Rate %"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "unit": "percent",
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {"color": "green", "value": null},
                {"color": "yellow", "value": 1},
                {"color": "red", "value": 5}
              ]
            }
          }
        }
      },
      {
        "id": 3,
        "title": "Response Time (95th percentile)",
        "type": "timeseries",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, endpoint))",
            "legendFormat": "{{ endpoint }}"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "unit": "s"
          }
        }
      },
      {
        "id": 4,
        "title": "CV Analyses per Hour",
        "type": "timeseries",
        "targets": [
          {
            "expr": "sum(rate(cv_analyses_total[1h])) * 3600",
            "legendFormat": "Analyses/hour"
          }
        ]
      },
      {
        "id": 5,
        "title": "Active Users",
        "type": "stat",
        "targets": [
          {
            "expr": "count(count by (user_id) (http_requests_total{user_id!=\"\"}))",
            "legendFormat": "Active Users"
          }
        ]
      },
      {
        "id": 6,
        "title": "Database Performance",
        "type": "timeseries",
        "targets": [
          {
            "expr": "database_connections_active",
            "legendFormat": "Active Connections"
          },
          {
            "expr": "rate(database_queries_total[5m])",
            "legendFormat": "Queries/sec"
          }
        ]
      }
    ],
    "time": {
      "from": "now-1h",
      "to": "now"
    },
    "refresh": "30s"
  }
}
```

---

## 🔧 Log Aggregation and Analysis

### ELK Stack Configuration
```yaml
# docker-compose.elk.yml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.11.0
    ports:
      - "5044:5044"
      - "9600:9600"
    volumes:
      - ./logstash/config:/usr/share/logstash/pipeline
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    ports:
      - "5601:5601"
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    depends_on:
      - elasticsearch

  filebeat:
    image: docker.elastic.co/beats/filebeat:8.11.0
    user: root
    volumes:
      - ./filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    depends_on:
      - logstash

volumes:
  elasticsearch_data:
```

### Logstash Pipeline Configuration
```ruby
# logstash/config/logstash.conf
input {
  beats {
    port => 5044
  }
}

filter {
  if [fields][service] == "recoloca-backend" {
    json {
      source => "message"
    }
    
    date {
      match => [ "timestamp", "ISO8601" ]
    }
    
    mutate {
      add_field => { "service_type" => "backend" }
    }
  }
  
  if [fields][service] == "recoloca-frontend" {
    json {
      source => "message"
    }
    
    mutate {
      add_field => { "service_type" => "frontend" }
    }
  }
  
  # Parse nginx access logs
  if [fields][service] == "nginx" {
    grok {
      match => { 
        "message" => "%{NGINXACCESS}"
      }
    }
    
    mutate {
      convert => { "response" => "integer" }
      convert => { "bytes" => "integer" }
      convert => { "responsetime" => "float" }
    }
  }
  
  # Add geolocation for IP addresses
  if [clientip] {
    geoip {
      source => "clientip"
      target => "geoip"
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "recoloca-logs-%{+YYYY.MM.dd}"
  }
  
  # Debug output
  stdout {
    codec => rubydebug
  }
}
```

---

## 📈 Performance Monitoring

### Application Performance Monitoring (APM)
```python
# src/monitoring/apm.py
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from elasticapm import capture_span, capture_message
import time
from typing import Callable

# Configure Elastic APM
apm_config = {
    'SERVICE_NAME': 'recoloca-backend',
    'SERVER_URL': 'http://apm-server:8200',
    'ENVIRONMENT': 'production',
    'DEBUG': False,
    'CAPTURE_BODY': 'all',
    'TRANSACTION_SAMPLE_RATE': 1.0,
    'CENTRAL_CONFIG': False,
}

apm = make_apm_client(apm_config)

# Performance monitoring decorators
def monitor_performance(operation_name: str):
    def decorator(func: Callable):
        async def wrapper(*args, **kwargs):
            with capture_span(operation_name):
                start_time = time.time()
                try:
                    result = await func(*args, **kwargs)
                    duration = time.time() - start_time
                    
                    # Log performance metrics
                    capture_message(
                        f"{operation_name} completed",
                        level='info',
                        custom={
                            'duration_ms': duration * 1000,
                            'operation': operation_name,
                            'status': 'success'
                        }
                    )
                    
                    return result
                except Exception as e:
                    duration = time.time() - start_time
                    capture_message(
                        f"{operation_name} failed",
                        level='error',
                        custom={
                            'duration_ms': duration * 1000,
                            'operation': operation_name,
                            'status': 'error',
                            'error': str(e)
                        }
                    )
                    raise
        return wrapper
    return decorator

# Usage example
@monitor_performance("cv_analysis")
async def analyze_cv(cv_content: str, user_id: str):
    # CV analysis logic
    pass
```

---

## 🎯 SLA and SLO Monitoring

### Service Level Objectives
```yaml
# slo/objectives.yml
slos:
  - name: "API Availability"
    description: "API should be available 99.9% of the time"
    target: 99.9
    time_window: "30d"
    query: |
      sum(rate(http_requests_total{status_code!~"5.."}[5m])) /
      sum(rate(http_requests_total[5m]))
    
  - name: "API Response Time"
    description: "95% of API requests should complete within 500ms"
    target: 95
    time_window: "7d"
    query: |
      histogram_quantile(0.95, 
        sum(rate(http_request_duration_seconds_bucket[5m])) by (le)
      ) < 0.5
    
  - name: "CV Analysis Success Rate"
    description: "CV analysis should succeed 99% of the time"
    target: 99
    time_window: "7d"
    query: |
      sum(rate(cv_analyses_total{status="success"}[5m])) /
      sum(rate(cv_analyses_total[5m]))
    
  - name: "Payment Processing Success Rate"
    description: "Payment processing should succeed 99.5% of the time"
    target: 99.5
    time_window: "30d"
    query: |
      sum(rate(payment_processing_total{status="success"}[5m])) /
      sum(rate(payment_processing_total[5m]))
```

---

## 📚 Related Documents

- [Testing Strategy](./01_TESTING_STRATEGY.md)
- [CI/CD Pipeline](../04_DEVOPS_AND_INFRASTRUCTURE/02_CI_CD_PIPELINE.md)
- [Infrastructure as Code](../04_DEVOPS_AND_INFRASTRUCTURE/03_INFRASTRUCTURE_AS_CODE.md)
- [Security Guidelines](../02_STANDARDS_AND_BEST_PRACTICES/02_SECURITY_GUIDELINES.md)
- [API Specifications](../03_SPECIFICATIONS_AND_CONTRACTS/01_API_SPECIFICATIONS.md)

---

**Document Information:**
- **Created**: 2025-01-20
- **Last Updated**: 2025-01-20
- **Version**: 1.0
- **Status**: Active
- **Owner**: @DevOpsTeam