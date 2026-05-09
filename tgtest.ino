#include <DHT.h>

#define DHTPIN 2          //пин DHT11
#define DHTTYPE DHT11     //тип датчика
#define beep 6          
#define LED_PIN 13
#define LED_blue 5
#define LED_red 4
#define LED_green 3

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {//svet
      digitalWrite(LED_PIN, HIGH);      //вкл выкл светодиод
      Serial.println("LED:ON");
    }
    else if (command == '0') {
      digitalWrite(LED_PIN, LOW);
      Serial.println("LED:OFF");
    }//svet

    else if (command == 'd') {          //beep
      Serial.println("beep!!!!!!!!!!!");
      tone(beep, 294);  // Ре (D4)
      delay(50);
      noTone(beep);         //beep
    }
    
  
    else if (command == 'b') {          //rgb
      digitalWrite(LED_blue, HIGH);
      Serial.println("LED:On");
    }
    else if (command == 'r') {          //rgb
      digitalWrite(LED_red, HIGH);
      Serial.println("LED:On");
    }
    else if (command == 'g') {          //rgb
      digitalWrite(LED_green, HIGH);
      Serial.println("LED:On");
    }
        else if (command == 'q') {          //rgb
      digitalWrite(LED_blue, LOW);
      Serial.println("LED:On");
    }
    else if (command == 'w') {          //rgb
      digitalWrite(LED_red, LOW);
      Serial.println("LED:On");
    }
    else if (command == 'e') {          //rgb
      digitalWrite(LED_green, LOW);
      Serial.println("LED:On");
    }
    else if (command == 'f') {          //rgb
      digitalWrite(LED_green, LOW);
      digitalWrite(LED_blue, LOW);
      digitalWrite(LED_red, LOW);
      Serial.println("LED:On");
    }
    else if (command == 'o') {          //rgb
      digitalWrite(LED_green, HIGH);
      digitalWrite(LED_blue, HIGH);
      digitalWrite(LED_red, HIGH);
      Serial.println("LED:On");
    }

    
    else if (command == 't') {    // температура dht11
      float h = dht.readHumidity();
      float t = dht.readTemperature();

      if (isnan(h) || isnan(t)) {
        Serial.println("ERR:Sensor read failed");
        return;
      }

      // Формат: TEMP:23.5|HUM:60.2
      Serial.print("TEMP:");
      Serial.print(t, 1);
      Serial.print("|HUM:");
      Serial.print(h, 1);
      Serial.println();
    }
  }
  delay(100);
}
