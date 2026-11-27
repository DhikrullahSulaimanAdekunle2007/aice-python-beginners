raw_name = "   DHIKRULLAH sulaiman   "
raw_country = "   NiGeRiA   "

clean_name = raw_name.strip().title()
clean_country = raw_country.strip().lower()

clean_name = clean_name.replace("Sulaiman", "Adekunle")

print(f"Original name: '{raw_name}'")
print(f"Cleaned name: '{clean_name}'")

print(f"Original country: '{raw_country}'")
print(f"Cleaned country: '{clean_country}'")
