#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "*****";
const char* password = "*****";

const char* serverUrl = "http://192.168.1.45:5000/api/access";

void setup() {

  Serial.begin(115200);

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

    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"uid\":\"A1B2C3D4\"}";

    int httpCode = http.POST(jsonData);

    Serial.print("Code HTTP : ");
    Serial.println(httpCode);

    String response = http.getString();

    Serial.println("Réponse du serveur :");
    Serial.println(response);

    http.end();
  }

  delay(5000);
}