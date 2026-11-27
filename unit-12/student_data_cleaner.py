raw_name = "   Dhikrullah suliaman   "
raw_email = "   dhikrullah.sulaiman@GMAIL.com   "
raw_phone = "   +234-801-234-5678   "

clean_name = raw_name.strip().title()
clean_email = raw_email.strip().lower()
clean_phone = raw_phone.strip().replace("-", "")

print(f"Name: {clean_name}")
print(f"Email: {clean_email}")
print(f"Phone: {clean_phone}")

print(f"Name length valid: {len(clean_name) > 3}")
print(f"Email contains @: {'@' in clean_email}")
