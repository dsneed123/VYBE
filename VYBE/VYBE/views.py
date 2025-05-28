from django.shortcuts import render
from datetime import datetime

def index(request):
    stocks = [
        {
            'ticker': 'AAPL',
            'status': 'free',
            'chart': [150.12, 152.34, 151.89, 153.45, 155.10],
            'analysis': "Strong buy. Insider activity indicates continued confidence in growth."
        },
        {
            'ticker': 'TSLA',
            'status': 'locked',
            'chart': [620.56, 618.22, 625.90, 630.75, 635.00],
            'analysis': "Neutral. Mixed insider signals; consider waiting for further confirmation."
        },
        {
            'ticker': 'NVDA',
            'status': 'locked',
            'chart': [390.30, 392.00, 388.75, 395.40, 397.80],
            'analysis': "Buy alert. Recent executive purchases align with earnings momentum."
        }
    ]

    return render(request, 'index.html', {
        'latest_update': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'stocks': stocks
    })
