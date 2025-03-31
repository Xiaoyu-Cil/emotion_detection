import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return {"error": "Request failed", "status_code": response.status_code}

    result = json.loads(response.text)
    emotions = result["emotionPredictions"][0]["emotion"]
    
    dominant_emotion = "anger"
    for emotion in emotions:
        if emotions[emotion] > emotions[dominant_emotion]:
            dominant_emotion = emotion
    
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
