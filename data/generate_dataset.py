import pandas as pd
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "social_media_privacy_assessments.csv")

def generate_synthetic_data(num_records=1000):
    os.makedirs(BASE_DIR, exist_ok=True)
    data = []
    
    for i in range(num_records):
        profile = random.randint(10, 90)
        pii = random.randint(20, 100)
        location = random.randint(10, 90)
        content = random.randint(10, 80)
        connections = random.randint(20, 100)
        tagging = random.randint(0, 80)
        security = random.randint(30, 100)
        third_party = random.randint(0, 90)
        social_eng = random.randint(20, 90)
        footprint = random.randint(10, 90)
        
        overall_score = int(
            (profile * 0.10) + (pii * 0.15) + (location * 0.15) + 
            (content * 0.10) + (connections * 0.10) + (tagging * 0.05) + 
            (security * 0.15) + (third_party * 0.05) + 
            (social_eng * 0.10) + (footprint * 0.05)
        )
        
        if overall_score <= 20: level = "LOW"
        elif overall_score <= 40: level = "MODERATE"
        elif overall_score <= 70: level = "HIGH"
        else: level = "CRITICAL"
            
        data.append({
            "assessment_id": f"ASM-{1000+i}",
            "Profile Visibility": profile, 
            "Personal Information": pii, 
            "Location Privacy": location,
            "Posts & Content": content, 
            "Connections": connections, 
            "Tagging": tagging,
            "Account Security": security, 
            "Third-Party Apps": third_party, 
            "Social Engineering": social_eng, 
            "Digital Footprint": footprint,
            "overall_score": overall_score,
            "risk_level": level
        })
        
    df = pd.DataFrame(data)
    df.to_csv(CSV_PATH, index=False)
    print(f"Successfully generated synthetic dataset at {CSV_PATH}")

if __name__ == "__main__":
    generate_synthetic_data()