#include <WiFi.h>
#include <HTTPClient.h>

#define LED_VERTE 26
#define LED_ROUGE 25
#define BUZZER 33

const char* ssid = "*****";
const char* password = "*****";

const char* serverUrl = "http://192.168.1.45:5000/api/access";

void setup() {

  Serial.begin(115200);

  pinMode(LED_VERTE, OUTPUT);
  pinMode(LED_ROUGE, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  WiFi.begin(ssid, password);

  Serial.print("Connexion au Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi connecté");
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(serverUrl);
    http.setTimeout(5000);

    http.addHeader("Content-Type", "application/json");
    http.addHeader("Authorization", "Bearer SECURACCES_CIEL_E6");

    String jsonData = "{\"uid\":\"A1B2C3D4\"}";

    
    int httpCode = http.POST(jsonData);

    if (httpCode > 0){

    Serial.print("Code HTTP : ");
    Serial.println(httpCode);

    String response = http.getString();
    Serial.println(response);

      if (httpCode == 200) {

          if (response.indexOf("allow") > 0 ) {
            digitalWrite(LED_VERTE, HIGH);
            tone(BUZZER, 2000);
            delay(1000);
            noTone(BUZZER);
            delay(1000);
            digitalWrite(LED_VERTE, LOW);
          }
          else{
            digitalWrite(LED_ROUGE, HIGH);
            tone(BUZZER, 800);
            delay(1000);
            noTone(BUZZER);
            delay(1000);
            digitalWrite(LED_ROUGE, LOW);
          }
      }
      else {

      Serial.println("timeout");
      digitalWrite(LED_ROUGE, HIGH);
      tone(BUZZER, 500);
      delay(2000);
      noTone(BUZZER);
      digitalWrite(LED_ROUGE, LOW);

      }

    }

    Serial.println("Réponse du serveur :");
 
    http.end();
  }

  delay(2000);
}