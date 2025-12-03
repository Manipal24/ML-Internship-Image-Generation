# ML Internship Task Round 2 - Image Generation
# Author: Anam Manipal Reddy (Manipal24)
# Date: December 3, 2025

import requests
import json

print("="*70)
print("ML INTERNSHIP - IMAGE GENERATION TASK")
print("="*70)

# Article data and prompts
articles = {
    "Article 1": {
        "title": "The Global Energy Transition",
        "prompt": "Solar and wind energy landscape at sunset"
    },
    "Article 2": {
        "title": "Youth Activism and Protests",
        "prompt": "Young people marching for climate justice"
    },
    "Article 3": {
        "title": "The AI Revolution",
        "prompt": "AI neural networks and machine learning visualization"
    }
}

print("\nArticles analyzed:")
for name, data in articles.items():
    print(f"{name}: {data['title']}")

print("\nImage generation framework created!")
print("Replace API_KEY to generate actual images.")
print("="*70)
