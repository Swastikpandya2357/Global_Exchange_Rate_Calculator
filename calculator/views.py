import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# API endpoint for exchange rates (using exchangerate-api.com)
API_URL = 'https://api.exchangerate-api.com/v4/latest/'

def get_exchange_rates(base_currency='USD'):
    """Fetch real-time exchange rates from the API."""
    try:
        response = requests.get(f"{API_URL}{base_currency}")
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Currency data with country names, flag emojis, and flag image URLs
currency_data = {
    'USD': {'country': 'United States', 'flag': '🇺🇸', 'image': 'https://flagcdn.com/w40/us.png'},
    'EUR': {'country': 'European Union', 'flag': '🇪🇺', 'image': 'https://flagcdn.com/w40/eu.png'},
    'GBP': {'country': 'United Kingdom', 'flag': '🇬🇧', 'image': 'https://flagcdn.com/w40/gb.png'},
    'JPY': {'country': 'Japan', 'flag': '🇯🇵', 'image': 'https://flagcdn.com/w40/jp.png'},
    'CAD': {'country': 'Canada', 'flag': '🇨🇦', 'image': 'https://flagcdn.com/w40/ca.png'},
    'AUD': {'country': 'Australia', 'flag': '🇦🇺', 'image': 'https://flagcdn.com/w40/au.png'},
    'CHF': {'country': 'Switzerland', 'flag': '🇨🇭', 'image': 'https://flagcdn.com/w40/ch.png'},
    'CNY': {'country': 'China', 'flag': '🇨🇳', 'image': 'https://flagcdn.com/w40/cn.png'},
    'SEK': {'country': 'Sweden', 'flag': '🇸🇪', 'image': 'https://flagcdn.com/w40/se.png'},
    'NZD': {'country': 'New Zealand', 'flag': '🇳🇿', 'image': 'https://flagcdn.com/w40/nz.png'},
    'MXN': {'country': 'Mexico', 'flag': '🇲🇽', 'image': 'https://flagcdn.com/w40/mx.png'},
    'SGD': {'country': 'Singapore', 'flag': '🇸🇬', 'image': 'https://flagcdn.com/w40/sg.png'},
    'HKD': {'country': 'Hong Kong', 'flag': '🇭🇰', 'image': 'https://flagcdn.com/w40/hk.png'},
    'NOK': {'country': 'Norway', 'flag': '🇳🇴', 'image': 'https://flagcdn.com/w40/no.png'},
    'KRW': {'country': 'South Korea', 'flag': '🇰🇷', 'image': 'https://flagcdn.com/w40/kr.png'},
    'TRY': {'country': 'Turkey', 'flag': '🇹🇷', 'image': 'https://flagcdn.com/w40/tr.png'},
    'RUB': {'country': 'Russia', 'flag': '🇷🇺', 'image': 'https://flagcdn.com/w40/ru.png'},
    'INR': {'country': 'India', 'flag': '🇮🇳', 'image': 'https://flagcdn.com/w40/in.png'},
    'BRL': {'country': 'Brazil', 'flag': '🇧🇷', 'image': 'https://flagcdn.com/w40/br.png'},
    'ZAR': {'country': 'South Africa', 'flag': '🇿🇦', 'image': 'https://flagcdn.com/w40/za.png'},
    'AED': {'country': 'United Arab Emirates', 'flag': '🇦🇪', 'image': 'https://flagcdn.com/w40/ae.png'},
    'SAR': {'country': 'Saudi Arabia', 'flag': '🇸🇦', 'image': 'https://flagcdn.com/w40/sa.png'},
    'THB': {'country': 'Thailand', 'flag': '🇹🇭', 'image': 'https://flagcdn.com/w40/th.png'},
    'MYR': {'country': 'Malaysia', 'flag': '🇲🇾', 'image': 'https://flagcdn.com/w40/my.png'},
    'IDR': {'country': 'Indonesia', 'flag': '🇮🇩', 'image': 'https://flagcdn.com/w40/id.png'},
    'PHP': {'country': 'Philippines', 'flag': '🇵🇭', 'image': 'https://flagcdn.com/w40/ph.png'},
    'VND': {'country': 'Vietnam', 'flag': '🇻🇳', 'image': 'https://flagcdn.com/w40/vn.png'},
    'EGP': {'country': 'Egypt', 'flag': '🇪🇬', 'image': 'https://flagcdn.com/w40/eg.png'},
    'PKR': {'country': 'Pakistan', 'flag': '🇵🇰', 'image': 'https://flagcdn.com/w40/pk.png'},
    'BDT': {'country': 'Bangladesh', 'flag': '🇧🇩', 'image': 'https://flagcdn.com/w40/bd.png'},
    'LKR': {'country': 'Sri Lanka', 'flag': '🇱🇰', 'image': 'https://flagcdn.com/w40/lk.png'},
    'NGN': {'country': 'Nigeria', 'flag': '🇳🇬', 'image': 'https://flagcdn.com/w40/ng.png'},
    'KES': {'country': 'Kenya', 'flag': '🇰🇪', 'image': 'https://flagcdn.com/w40/ke.png'},
    'GHS': {'country': 'Ghana', 'flag': '🇬🇭', 'image': 'https://flagcdn.com/w40/gh.png'},
    'UGX': {'country': 'Uganda', 'flag': '🇺🇬', 'image': 'https://flagcdn.com/w40/ug.png'},
    'TZS': {'country': 'Tanzania', 'flag': '🇹🇿', 'image': 'https://flagcdn.com/w40/tz.png'},
    'MAD': {'country': 'Morocco', 'flag': '🇲🇦', 'image': 'https://flagcdn.com/w40/ma.png'},
    'DZD': {'country': 'Algeria', 'flag': '🇩🇿', 'image': 'https://flagcdn.com/w40/dz.png'},
    'TND': {'country': 'Tunisia', 'flag': '🇹🇳', 'image': 'https://flagcdn.com/w40/tn.png'},
    'XAF': {'country': 'Central African CFA Franc', 'flag': '🇨🇫', 'image': 'https://flagcdn.com/w40/cf.png'},
    'XOF': {'country': 'West African CFA Franc', 'flag': '🇸🇳', 'image': 'https://flagcdn.com/w40/sn.png'},
    'BIF': {'country': 'Burundi', 'flag': '🇧🇮', 'image': 'https://flagcdn.com/w40/bi.png'},
    'RWF': {'country': 'Rwanda', 'flag': '🇷🇼', 'image': 'https://flagcdn.com/w40/rw.png'},
    'ETB': {'country': 'Ethiopia', 'flag': '🇪🇹', 'image': 'https://flagcdn.com/w40/et.png'},
    'SOS': {'country': 'Somalia', 'flag': '🇸🇴', 'image': 'https://flagcdn.com/w40/so.png'},
    'DJF': {'country': 'Djibouti', 'flag': '🇩🇯', 'image': 'https://flagcdn.com/w40/dj.png'},
    'KMF': {'country': 'Comoros', 'flag': '🇰🇲', 'image': 'https://flagcdn.com/w40/km.png'},
    'MUR': {'country': 'Mauritius', 'flag': '🇲🇺', 'image': 'https://flagcdn.com/w40/mu.png'},
    'SCR': {'country': 'Seychelles', 'flag': '🇸🇨', 'image': 'https://flagcdn.com/w40/sc.png'},
    'MGA': {'country': 'Madagascar', 'flag': '🇲🇬', 'image': 'https://flagcdn.com/w40/mg.png'},
    'MWK': {'country': 'Malawi', 'flag': '🇲🇼', 'image': 'https://flagcdn.com/w40/mw.png'},
    'ZMW': {'country': 'Zambia', 'flag': '🇿🇲', 'image': 'https://flagcdn.com/w40/zm.png'},
    'BWP': {'country': 'Botswana', 'flag': '🇧🇼', 'image': 'https://flagcdn.com/w40/bw.png'},
    'NAD': {'country': 'Namibia', 'flag': '🇳🇦', 'image': 'https://flagcdn.com/w40/na.png'},
    'SZL': {'country': 'Eswatini', 'flag': '🇸🇿', 'image': 'https://flagcdn.com/w40/sz.png'},
    'LSL': {'country': 'Lesotho', 'flag': '🇱🇸', 'image': 'https://flagcdn.com/w40/ls.png'},
    'ZWL': {'country': 'Zimbabwe', 'flag': '🇿🇼', 'image': 'https://flagcdn.com/w40/zw.png'},
    'CVE': {'country': 'Cape Verde', 'flag': '🇨🇻', 'image': 'https://flagcdn.com/w40/cv.png'},
    'STN': {'country': 'São Tomé and Príncipe', 'flag': '🇸🇹', 'image': 'https://flagcdn.com/w40/st.png'},
    'XCD': {'country': 'Eastern Caribbean Dollar', 'flag': '🇦🇬', 'image': 'https://flagcdn.com/w40/ag.png'},
    'BSD': {'country': 'Bahamas', 'flag': '🇧🇸', 'image': 'https://flagcdn.com/w40/bs.png'},
    'BBD': {'country': 'Barbados', 'flag': '🇧🇧', 'image': 'https://flagcdn.com/w40/bb.png'},
    'JMD': {'country': 'Jamaica', 'flag': '🇯🇲', 'image': 'https://flagcdn.com/w40/jm.png'},
    'TTD': {'country': 'Trinidad and Tobago', 'flag': '🇹🇹', 'image': 'https://flagcdn.com/w40/tt.png'},
    'GYD': {'country': 'Guyana', 'flag': '🇬🇾', 'image': 'https://flagcdn.com/w40/gy.png'},
    'SRD': {'country': 'Suriname', 'flag': '🇸🇷', 'image': 'https://flagcdn.com/w40/sr.png'},
    'AWG': {'country': 'Aruba', 'flag': '🇦🇼', 'image': 'https://flagcdn.com/w40/aw.png'},
    'ANG': {'country': 'Netherlands Antilles', 'flag': '🇳🇱', 'image': 'https://flagcdn.com/w40/nl.png'},
    'BMD': {'country': 'Bermuda', 'flag': '🇧🇲', 'image': 'https://flagcdn.com/w40/bm.png'},
    'KYD': {'country': 'Cayman Islands', 'flag': '🇰🇾', 'image': 'https://flagcdn.com/w40/ky.png'},
    'FJD': {'country': 'Fiji', 'flag': '🇫🇯', 'image': 'https://flagcdn.com/w40/fj.png'},
    'SBD': {'country': 'Solomon Islands', 'flag': '🇸🇧', 'image': 'https://flagcdn.com/w40/sb.png'},
    'TOP': {'country': 'Tonga', 'flag': '🇹🇴', 'image': 'https://flagcdn.com/w40/to.png'},
    'WST': {'country': 'Samoa', 'flag': '🇼🇸', 'image': 'https://flagcdn.com/w40/ws.png'},
    'VUV': {'country': 'Vanuatu', 'flag': '🇻🇺', 'image': 'https://flagcdn.com/w40/vu.png'},
    'XPF': {'country': 'French Polynesia', 'flag': '🇵🇫', 'image': 'https://flagcdn.com/w40/pf.png'},
    'KWD': {'country': 'Kuwait', 'flag': '🇰🇼', 'image': 'https://flagcdn.com/w40/kw.png'},
    'BHD': {'country': 'Bahrain', 'flag': '🇧🇭', 'image': 'https://flagcdn.com/w40/bh.png'},
    'OMR': {'country': 'Oman', 'flag': '🇴🇲', 'image': 'https://flagcdn.com/w40/om.png'},
    'QAR': {'country': 'Qatar', 'flag': '🇶🇦', 'image': 'https://flagcdn.com/w40/qa.png'},
    'YER': {'country': 'Yemen', 'flag': '🇾🇪', 'image': 'https://flagcdn.com/w40/ye.png'},
    'IQD': {'country': 'Iraq', 'flag': '🇮🇶', 'image': 'https://flagcdn.com/w40/iq.png'},
    'JOD': {'country': 'Jordan', 'flag': '🇯🇴', 'image': 'https://flagcdn.com/w40/jo.png'},
    'LBP': {'country': 'Lebanon', 'flag': '🇱🇧', 'image': 'https://flagcdn.com/w40/lb.png'},
    'SYP': {'country': 'Syria', 'flag': '🇸🇾', 'image': 'https://flagcdn.com/w40/sy.png'},
    'AFN': {'country': 'Afghanistan', 'flag': '🇦🇫', 'image': 'https://flagcdn.com/w40/af.png'},
    'TJS': {'country': 'Tajikistan', 'flag': '🇹🇯', 'image': 'https://flagcdn.com/w40/tj.png'},
    'TMT': {'country': 'Turkmenistan', 'flag': '🇹🇲', 'image': 'https://flagcdn.com/w40/tm.png'},
    'UZS': {'country': 'Uzbekistan', 'flag': '🇺🇿', 'image': 'https://flagcdn.com/w40/uz.png'},
    'KGS': {'country': 'Kyrgyzstan', 'flag': '🇰🇬', 'image': 'https://flagcdn.com/w40/kg.png'},
    'MNT': {'country': 'Mongolia', 'flag': '🇲🇳', 'image': 'https://flagcdn.com/w40/mn.png'},
    'KPW': {'country': 'North Korea', 'flag': '🇰🇵', 'image': 'https://flagcdn.com/w40/kp.png'},
    'MMK': {'country': 'Myanmar', 'flag': '🇲🇲', 'image': 'https://flagcdn.com/w40/mm.png'},
    'LAK': {'country': 'Laos', 'flag': '🇱🇦', 'image': 'https://flagcdn.com/w40/la.png'},
    'KHR': {'country': 'Cambodia', 'flag': '🇰🇭', 'image': 'https://flagcdn.com/w40/kh.png'},
    'BND': {'country': 'Brunei', 'flag': '🇧🇳', 'image': 'https://flagcdn.com/w40/bn.png'},
    'PGK': {'country': 'Papua New Guinea', 'flag': '🇵🇬', 'image': 'https://flagcdn.com/w40/pg.png'},
    'SHP': {'country': 'Saint Helena', 'flag': '🇸🇭', 'image': 'https://flagcdn.com/w40/sh.png'},
    'FKP': {'country': 'Falkland Islands', 'flag': '🇫🇰', 'image': 'https://flagcdn.com/w40/fk.png'},
    'GIP': {'country': 'Gibraltar', 'flag': '🇬🇮', 'image': 'https://flagcdn.com/w40/gi.png'},
    'GGP': {'country': 'Guernsey', 'flag': '🇬🇬', 'image': 'https://flagcdn.com/w40/gg.png'},
    'IMP': {'country': 'Isle of Man', 'flag': '🇮🇲', 'image': 'https://flagcdn.com/w40/im.png'},
    'JEP': {'country': 'Jersey', 'flag': '🇯🇪', 'image': 'https://flagcdn.com/w40/je.png'},
    'SPL': {'country': 'Seborga', 'flag': '🇮🇹', 'image': 'https://flagcdn.com/w40/it.png'},
    'CHE': {'country': 'Switzerland (WIR Euro)', 'flag': '🇨🇭', 'image': 'https://flagcdn.com/w40/ch.png'},
    'CHW': {'country': 'Switzerland (WIR Franc)', 'flag': '🇨🇭', 'image': 'https://flagcdn.com/w40/ch.png'},
    'CLF': {'country': 'Chile (Unidad de Fomento)', 'flag': '🇨🇱', 'image': 'https://flagcdn.com/w40/cl.png'},
    'COU': {'country': 'Colombia (Unidad de Valor Real)', 'flag': '🇨🇴', 'image': 'https://flagcdn.com/w40/co.png'},
    'UYI': {'country': 'Uruguay (Unidad Indexada)', 'flag': '🇺🇾', 'image': 'https://flagcdn.com/w40/uy.png'},
    'UYU': {'country': 'Uruguay', 'flag': '🇺🇾', 'image': 'https://flagcdn.com/w40/uy.png'},
    'CUC': {'country': 'Cuba (Convertible Peso)', 'flag': '🇨🇺', 'image': 'https://flagcdn.com/w40/cu.png'},
    'CUP': {'country': 'Cuba', 'flag': '🇨🇺', 'image': 'https://flagcdn.com/w40/cu.png'},
    'DOP': {'country': 'Dominican Republic', 'flag': '🇩🇴', 'image': 'https://flagcdn.com/w40/do.png'},
    'HTG': {'country': 'Haiti', 'flag': '🇭🇹', 'image': 'https://flagcdn.com/w40/ht.png'},
    'PYG': {'country': 'Paraguay', 'flag': '🇵🇾', 'image': 'https://flagcdn.com/w40/py.png'},
    'PEN': {'country': 'Peru', 'flag': '🇵🇪', 'image': 'https://flagcdn.com/w40/pe.png'},
    'BOB': {'country': 'Bolivia', 'flag': '🇧🇴', 'image': 'https://flagcdn.com/w40/bo.png'},
    'VEF': {'country': 'Venezuela', 'flag': '🇻🇪', 'image': 'https://flagcdn.com/w40/ve.png'},
    'VES': {'country': 'Venezuela', 'flag': '🇻🇪', 'image': 'https://flagcdn.com/w40/ve.png'},
    'ARS': {'country': 'Argentina', 'flag': '🇦🇷', 'image': 'https://flagcdn.com/w40/ar.png'},
    'CLP': {'country': 'Chile', 'flag': '🇨🇱', 'image': 'https://flagcdn.com/w40/cl.png'},
    'COP': {'country': 'Colombia', 'flag': '🇨🇴', 'image': 'https://flagcdn.com/w40/co.png'},
    'PAB': {'country': 'Panama', 'flag': '🇵🇦', 'image': 'https://flagcdn.com/w40/pa.png'},
    'NIO': {'country': 'Nicaragua', 'flag': '🇳🇮', 'image': 'https://flagcdn.com/w40/ni.png'},
    'CRC': {'country': 'Costa Rica', 'flag': '🇨🇷', 'image': 'https://flagcdn.com/w40/cr.png'},
    'SVC': {'country': 'El Salvador', 'flag': '🇸🇻', 'image': 'https://flagcdn.com/w40/sv.png'},
    'GTQ': {'country': 'Guatemala', 'flag': '🇬🇹', 'image': 'https://flagcdn.com/w40/gt.png'},
    'HNL': {'country': 'Honduras', 'flag': '🇭🇳', 'image': 'https://flagcdn.com/w40/hn.png'},
    'BZD': {'country': 'Belize', 'flag': '🇧🇿', 'image': 'https://flagcdn.com/w40/bz.png'},
    'BTN': {'country': 'Bhutan', 'flag': '🇧🇹', 'image': 'https://flagcdn.com/w40/bt.png'},
    'NPR': {'country': 'Nepal', 'flag': '🇳🇵', 'image': 'https://flagcdn.com/w40/np.png'},
    'MVR': {'country': 'Maldives', 'flag': '🇲🇻', 'image': 'https://flagcdn.com/w40/mv.png'},
}

def home(request):
    """Render the home page with the calculator form."""
    currencies = [{'code': k, 'country': v['country'], 'flag': v['flag'], 'image': v['image']} for k, v in currency_data.items()]
    json_currency_data = json.dumps(currency_data)
    return render(request, 'calculator/home.html', {'currencies': currencies, 'json_currency_data': json_currency_data})

@csrf_exempt
def convert(request):
    """Handle the currency conversion request."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = float(data.get('amount', 0))
            from_currency = data.get('from_currency', 'USD')
            to_currency = data.get('to_currency', 'EUR')

            rates = get_exchange_rates(from_currency)
            if rates and to_currency in rates:
                converted_amount = amount * rates[to_currency]
                return JsonResponse({
                    'success': True,
                    'converted_amount': round(converted_amount, 2),
                    'rate': rates[to_currency]
                })
            else:
                return JsonResponse({'success': False, 'error': 'Unable to fetch exchange rates'})
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({'success': False, 'error': 'Invalid input'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
