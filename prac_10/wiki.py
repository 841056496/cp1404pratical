import wikipedia

def main():
    print("Wikipedia Search Tool")
    user_input = input("Enter a page title or search phrase (or leave blank to exit): ")

    while user_input:
        try:
            page = wikipedia.page(user_input, autosuggest=False)
            print("\nTitle:", page.title)
            print("\nSummary:", page.summary)
            print("\nURL:", page.url)
        except wikipedia.DisambiguationError as e:
            print("The term you searched for has multiple meanings on Wikipedia. Here are some options:")
            for option in e.options:
                print(option)
            print("Please refine your search.")
        except wikipedia.PageError:
            print(f"Sorry, there's no exact match for '{user_input}' on Wikipedia. Please try again with a different term.")
        except Exception as e:
            print(f"An error occurred: {e}")

        user_input = input("\nEnter a page title or search phrase (or leave blank to exit): ")

    print("Thank you for using the Wikipedia Search Tool!")

if __name__ == '__main__':
    main()
