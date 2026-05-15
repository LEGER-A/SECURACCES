#define LED_VERTE 26 //Associe LED_VERT à la broche 26
#define LED_ROUGE 25 //Associe LED_ROUGE à la broche 25
#define BUZZER 33 //Associe BUZZER à la broche 33

void setup() {
  // Configure les trois broches comme sorties
  pinMode(LED_VERTE, OUTPUT);
  pinMode(LED_ROUGE, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void loop() {

  digitalWrite(LED_VERTE, HIGH); // Allume le LED vert

  tone(BUZZER, 2000); // Son du BUZZER à 200 Hz
  delay(1000); // Attend 1 seconde

  noTone(BUZZER); // Arrête le son du BUZZER
  delay(1000); // Attend 1 seconde

  digitalWrite(LED_VERTE, LOW); // Éteint la LED
  delay(500); // Attend 1/2 seconde

  
  digitalWrite(LED_ROUGE, HIGH); // Allume le LED rouge

  tone(BUZZER, 2000); // Son du BUZZER à 200 Hz
  delay(1000); // Attend 1 seconde

  noTone(BUZZER); // Arrête le son du BUZZER
  delay(1000); // Attend 1 seconde

  digitalWrite(LED_ROUGE, LOW); // Éteint la LED
  delay(500); // Attend 1/2 seconde
}