# Global Exchange Rate Calculator

A Django-based web application for real-time currency conversion using live exchange rates from exchangerate-api.com.

## Features

- 🌍 Real-time exchange rates for all major world currencies
- 💱 Easy-to-use web interface with attractive design
- 📱 Responsive design that works on all devices
- ⚡ Fast conversions with AJAX requests
- 🎨 Modern UI with gradient backgrounds and smooth animations

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS)
- **API**: exchangerate-api.com for live exchange rates
- **Styling**: Custom CSS with Google Fonts

## Installation

1. **Clone or download the project**
   ```bash
   cd exchange_rate_calculator
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django requests
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser and visit** `http://127.0.0.1:8000/`

## Usage

1. Enter the amount you want to convert
2. Select the source currency from the dropdown
3. Select the target currency
4. Click "Convert Currency"
5. View the real-time conversion result

## API Integration

This project uses the free tier of exchangerate-api.com. The API provides:
- Real-time exchange rates
- Support for 160+ currencies
- No API key required for basic usage

## Project Structure

```
exchange_rate_calculator/
├── exchange_calculator/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── calculator/                   # Main app
│   ├── views.py                  # Conversion logic and API calls
│   ├── urls.py                   # App URL patterns
│   └── ...
├── templates/
│   └── calculator/
│       └── home.html             # Main template with UI
├── static/                       # Static files (CSS, JS, images)
└── manage.py
```

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
