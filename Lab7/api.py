import json
import csv
import requests
from prettytable import PrettyTable
from colorama import Fore, Style, init 
from api_classes import NewsAPI, UnitOfWork, History

init(autoreset=True)

class UserInterface:
    def __init__(self, api):
        self.api = api
        self.uow = UnitOfWork()  # Тепер правильно ініціалізуємо UnitOfWork
        self.history = History()  # Тепер правильно ініціалізуємо History
        self.title_color = Fore.WHITE

    def display_articles(self, articles):
        table = PrettyTable()
        table.field_names = ["Title", "Description"]
        for article in articles:
            title = f"{self.title_color}{article.get('title', 'No title')}{Style.RESET_ALL}"
            description = article.get('description', 'No description')
            table.add_row([title, description])
        print(table)

    def save_to_file(self, data, filename, filetype='json'):
        try:
            if filetype == 'json':
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
            elif filetype == 'csv':
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Title", "Description"])
                    for article in data:
                        writer.writerow([
                            article.get('title', 'No title'),
                            article.get('description', 'No description')
                        ])
            else:  # txt format
                with open(filename, 'w', encoding='utf-8') as f:
                    for article in data:
                        f.write(f"Title: {article.get('title', 'No title')}\n")
                        f.write(f"Description: {article.get('description', 'No description')}\n\n")
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def search_news(self):
        keyword = input("Enter a keyword to search for: ")
        try:
            results = self.api.search_news(keyword)
            articles = results.get('articles', [])
            if articles:
                self.display_articles(articles)
                self.uow.repository.add(articles)
                self.uow.commit()
                self.history.add_query(keyword, len(articles))
            else:
                print("No articles found for this keyword.")
            return articles
        except Exception as e:
            print(f"An error occurred while searching news: {e}")
            return []

    def get_top_headlines(self):
        country = input("Enter country code (e.g., 'ua', 'us', 'gb'): ")
        try:
            results = self.api.get_top_headlines(country)
            articles = results.get('articles', [])
            if articles:
                self.display_articles(articles)
                self.uow.repository.add(articles)
                self.uow.commit()
                self.history.add_query(f"Top headlines for {country}", len(articles))
            else:
                print(f"No top headlines found for country code: {country}")
            return articles
        except Exception as e:
            print(f"An error occurred while getting top headlines: {e}")
            return []

    def change_title_color(self):
        print("\nChoose title color:")
        color_options = {
            '1': ('Red', Fore.RED),
            '2': ('Green', Fore.GREEN),
            '3': ('Yellow', Fore.YELLOW),
            '4': ('Blue', Fore.BLUE),
            '5': ('Magenta', Fore.MAGENTA),
            '6': ('Cyan', Fore.CYAN),
            '7': ('White', Fore.WHITE)
        }
        
        for key, (color_name, _) in color_options.items():
            print(f"{key}. {color_name}")
        
        choice = input("\nEnter your choice (1-7): ")
        if choice in color_options:
            self.title_color = color_options[choice][1]
            print(f"Title color changed to {color_options[choice][0]}.")
        else:
            print("Invalid choice. Color remains unchanged.")

    def run(self):
        print("\nWelcome to the News API Interface!")
        while True:
            try:
                print("\nMenu:")
                print("1. Search news")
                print("2. Get top headlines")
                print("3. View search history")
                print("4. Save last results")
                print("5. Change title color")
                print("6. Exit")
                
                choice = input("\nEnter your choice (1-6): ")

                if choice == '1':
                    self.search_news()
                elif choice == '2':
                    self.get_top_headlines()
                elif choice == '3':
                    self.history.display()
                elif choice == '4':
                    all_results = self.uow.repository.get_all()
                    if not all_results:
                        print("No results to save. Please perform a search first.")
                    else:
                        filetype = input("Enter file type to save (json/csv/txt): ").lower()
                        if filetype in ['json', 'csv', 'txt']:
                            self.save_to_file(all_results[-1], f"news_results.{filetype}", filetype)
                        else:
                            print("Invalid file type. Please choose json, csv, or txt.")
                elif choice == '5':
                    self.change_title_color()
                elif choice == '6':
                    print("Thank you for using the News API Interface. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Please try again.")

if __name__ == "__main__":
    API_KEY = "3b51eb9e98f24ee79b98ffcc873ebfc9"  # Замініть на свій API ключ
    news_api = NewsAPI(API_KEY)
    ui = UserInterface(news_api)
    ui.run()