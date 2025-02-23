from django.shortcuts import render

# Create your views here.

def home(request):
    data = [
        {
            "title": "Total Users",
            "subtitle": "Active accounts",
            "count": 150,
            "icon": "fa-users",
            "trend": 12,
            "trend_direction": "up",
            "is_currency": False,
            "card_type": "users",
            "footer_text": "10 new users today"
        },
        {
            "title": "Orders",
            "subtitle": "Last 30 days",
            "count": 320,
            "icon": "fa-shopping-cart",
            "trend": 5,
            "trend_direction": "up",
            "is_currency": False,
            "card_type": "orders",
            "footer_text": "85% completion rate"
        },
        {
            "title": "Revenue",
            "subtitle": "This month",
            "count": "12450",
            "icon": "fa-dollar-sign",
            "trend": 8,
            "trend_direction": "down",
            "is_currency": True,
            "card_type": "revenue",
            "footer_text": "Average $405/day"
        },
        {
            "title": "Visitors",
            "subtitle": "Online now",
            "count": "1240",
            "icon": "fa-chart-line",
            "trend": 15,
            "trend_direction": "up",
            "is_currency": False,
            "card_type": "visitors",
            "footer_text": "Peak hours: 2-4 PM"
        }
    ]
    return render(request, 'myApp/home.html', {'data': data})

def reports(request):
    report_data = [
        {
            "report_name": "Sales Report",
            "period": "March 2024",
            "total_sales": "45000",
            "status": "Completed"
        },
        {
            "report_name": "User Activity",
            "period": "Q1 2024",
            "total_users": "1200",
            "status": "Pending"
        },
        {
            "report_name": "Inventory Status",
            "period": "Current",
            "items_low": "15",
            "status": "Warning"
        }
    ]
    return render(request, 'myApp/reports.html', {'reports': report_data})

def settings(request):
    settings_data = {
        'general': [
            {'name': 'Site Name', 'value': 'My Dashboard'},
            {'name': 'Email Notifications', 'value': True},
            {'name': 'Dark Mode', 'value': False}
        ],
        'security': [
            {'name': 'Two-Factor Auth', 'value': False},
            {'name': 'Session Timeout', 'value': '30 minutes'}
        ]
    }
    return render(request, 'myApp/settings.html', {'settings': settings_data})
