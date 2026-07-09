# TODO List for Adding Country Names, Flags, and Images to Currency Calculator

## Steps to Complete:
- [ ] Step 1: In `calculator/views.py`, create a `currency_data` dictionary mapping each currency code to its country name, flag emoji, and flag image URL (using flagcdn.com).
- [ ] Step 2: Update the `home` view in `calculator/views.py` to pass `currency_data` to the template instead of just the currency list.
- [ ] Step 3: In `templates/calculator/home.html`, modify the `<option>` elements in the dropdowns to display flag emoji, country name, and currency code (e.g., "🇺🇸 United States - USD").
- [ ] Step 4: Update the JavaScript in `templates/calculator/home.html` to include small flag images next to the currencies in the conversion result output.
- [ ] Step 5: Run the Django server and test the calculator to ensure flags and country names appear in dropdowns and results. Verify image loading.
