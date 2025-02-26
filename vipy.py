import requests
from bs4 import BeautifulSoup

class CustomAI:
    def __init__(self):
        self.name = "CustomAI"
        self.version = "1.0"
        self.author = "taha185"
    
    def greet(self):
        return f"Hello! I am {self.name} version {self.version}. How can I assist you today?"

    def respond(self, input_text):
        if "fetch" in input_text.lower():
            return self.fetch_web_data(input_text)
        elif "help" in input_text.lower():
            return self.provide_help()
        elif input_text.lower() in ["hello", "hi", "hey"]:
            return "Hi there! How can I help you?"
        elif input_text.lower() == "bye":
            return "Goodbye! Have a great day!"
        else:
            return "Sorry, I don't quite understand that. Could you please clarify?"
    
    def fetch_web_data(self, input_text):
        # Check if the user wants to fetch a URL
        if "http" in input_text.lower() or "www" in input_text.lower():
            url = input_text.split('fetch ')[-1].strip()  # Extract URL after 'fetch '
            return self.scrape_website(url)
        else:
            return "Please provide a valid URL to fetch data from."

    def scrape_website(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Scraping the title and any visible text from the webpage
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string if soup.title else "No title found"
                paragraphs = soup.find_all("p")
                text_content = "\n".join([para.get_text() for para in paragraphs[:5]])  # Get first 5 paragraphs of text
                
                return f"Website Title: {title}\n\nText Snippet (First 5 paragraphs):\n{text_content}"
            else:
                return f"Failed to retrieve data from {url}. Status code: {response.status_code}"
        except Exception as e:
            return f"An error occurred while fetching data: {str(e)}"
    
    def provide_help(self):
        return """
        You can ask me to fetch information from the web by:
        - Asking me to 'fetch [URL]' and I will try to scrape the data from that website.
        - Type 'help' to get this message.
        - Type 'bye' to exit.
        """
    
    def show_disclaimer(self):
        disclaimer = """
        Disclaimer:
        This AI is designed for educational purposes only. The responses generated by the AI
        should not be interpreted as professional advice. The creator, taha185, is not responsible
        for any consequences resulting from the use of this AI. Use at your own discretion.
        """
        return disclaimer

# Main function to interact with the AI
def main():
    ai = CustomAI()
    print(ai.greet())
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Exiting... Have a nice day!")
            break
        elif "fetch" in user_input.lower():
            print(f"{ai.name}: {ai.fetch_web_data(user_input)}")
        else:
            response = ai.respond(user_input)
            print(f"{ai.name}: {response}")
    
    print(ai.show_disclaimer())

# Run the AI program
if __name__ == "__main__":
    main()
