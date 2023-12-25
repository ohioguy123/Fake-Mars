ascii_art = """
   _____                       
  /     \ _____ _______  ______
 /  \ /  \\__  \\_  __ \/  ___/
/    Y    \/ __ \|  | \/\___ \ 
\____|__  (____  /__|  /____  >
        \/     \/           \/ 
"""

# Print the custom ASCII art banner
print(ascii_art)

# Get user input for redirect URL and custom text
redirect_url = input("Enter the redirect URL (with https://): ")
custom_text = input("enter fake link (this must be without https):")

# Format and print the result
formatted_text = f"[{custom_text}]({redirect_url})"
print("fake link (send in discord):", formatted_text)
