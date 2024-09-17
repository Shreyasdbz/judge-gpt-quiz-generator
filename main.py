'''
Project oveview:
This app generates news articles (and headlines) in various languages using different news
outlets styles via a combination of GPT-4o and various other LLMs. Each article is also
translated into all 4 supported languages.
News headline generation is handled by ChatGPT-4o and content generation is handled by the
respective LLMs. These include GPT-4, GPT-4o, Phi-3-medium-4k-instruct, Llama-2,
Meta-Llama-3.1, Mistral-large, etc.
'''

from models.article import supported_locales
from generation.headline_generation import generate_multiple_headlines
from generation.content_generation import generate_content_with_gpt_4o


# def initialize():
#     """ Initialize the application """
#     print("Initializing application...")

# def process_data():
#     """ Process the data """
#     print("Processing data...")

# def cleanup():
#     """ Clean up the application """
#     print("Cleaning up...")

def main():
    """ main """
    
    generated_headlines_file_path = "data/generated_headlines.json"
    
    # Step 1: Headline generation
    # generate_multiple_headlines(
    #     generate_limit=10,
    #     make_fake_choices=[True, False],
    #     locales_to_use=supported_locales,
    #     generated_headlines_file_path=generated_headlines_file_path
    # )    
    
    # Step 2: Content generation
    content_response = generate_content_with_gpt_4o(
        origin_locale="en",
        style="Financial Times",
        headline="Major Economies Unite to Combat Cybersecurity Threats in Digital Age",
        context="In light of increasing cyberattacks affecting international financial systems, leaders from major economies gathered to discuss collaborative measures for enhancing cybersecurity. The summit aims to strengthen regulations and share intelligence to protect critical infrastructure and maintain economic stability in an interlinked world.",
        is_fake=False
    )
    print(content_response)

if __name__ == "__main__":
    main()
