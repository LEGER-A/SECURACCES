#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5  //ESP32 pin GPIO5 
#define RST_PIN 27 //ESP32 pin GPIO27 

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  
  SPI.begin(); //Démarrage du bus SPI
  rfid.PCD_Init(); //initialisation du lecteur RFID

  Serial.println("Tap an RFID/NFC tag on the RFID-RC522 reader"); //Affiche un message d’attente
}

void loop() {
  if (rfid.PICC_IsNewCardPresent()) { //Savoir si une nouvelle carte est détectée
    if (rfid.PICC_ReadCardSerial()) { //Lire son numéro
      MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak); //Afficher le nom du type de carte
      Serial.print("RFID/NFC Tag Type: ");//Affiche RFID/NFC Tag Type: 
      Serial.println(rfid.PICC_GetTypeName(piccType)); //Affiche le nom de la carte et retour a la ligne

      //Affiche l'UID de la carte dans le moniteur serie
      Serial.print("UID:"); //Affiche "UID"
      for (int i = 0; i < rfid.uid.size; i++) { //Permet d'obtenir le nombre d'octets de l'UID
        Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "); 
        Serial.print(rfid.uid.uidByte[i], HEX); //Affiche l'octet en hexadécimal
      }
      Serial.println(); //Retour à la ligne

      rfid.PICC_HaltA(); //Arrêt de la communication avec la carte
      rfid.PCD_StopCrypto1(); //Arrête les algorithmes de chiffrement sur le lecteur
    }
  }
}
