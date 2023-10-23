#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Endereço do display I2C (pode variar)

const uint8_t analogPin = A0;
const uint8_t intervalo_leitura = 1;  // Intervalo de amostragem em segundos (1 segundo)
const uint16_t intervalo_gravacao = 1 * 10;  // Intervalo de gravação em segundos (1 minutos)

uint32_t ultima_leitura = 0;
uint32_t valor_total_quarto = 0;
uint32_t valor_total_sala = 0;
uint16_t contador_leitura = 0;

void setup() {
  Serial.begin(9600);
  delay(10);

  pinMode(D3, OUTPUT); // SALA1
  pinMode(D4, OUTPUT); // SALA2

  pinMode(D5, OUTPUT); // QUARTO1
  pinMode(D6, OUTPUT); // QUARTO2

  digitalWrite(D3, LOW); // SALA1
  digitalWrite(D4, LOW); // SALA2

  digitalWrite(D5, LOW); // QUARTO1
  digitalWrite(D6, LOW); // QUARTO2

  lcd.init();                      // Inicializa o display
  lcd.backlight();                 // Liga o backlight

  lcd.setCursor(0, 0);
  lcd.print("SALA      QUARTO");

  delay(10);
}

void loop() {
  uint32_t tempo_atual = millis();

  if (tempo_atual - ultima_leitura >= (intervalo_leitura*1000)) {
    digitalWrite(D6, HIGH); // QUARTO2
    delay(50);
    int quarto = analogRead(analogPin);
    valor_total_quarto += quarto;
    
    digitalWrite(D6, LOW); // QUARTO2
    
    digitalWrite(D4, HIGH); // SALA2
    delay(50);
    int sala = analogRead(analogPin);
    valor_total_sala += sala;
    
    digitalWrite(D4, LOW); // SALA2
    
    contador_leitura++;
    lcd.setCursor(0, 1);
    lcd.print("                "); // Limpa a linha
    lcd.setCursor(0, 1);
    lcd.print(String(sala * 20/1023) + " KWh    " + String(quarto * 20/1023) + " KWh");
    ultima_leitura = tempo_atual;
  }

  if (contador_leitura >= (intervalo_gravacao / (intervalo_leitura))) {
      Serial.println("Quarto " + String((valor_total_quarto / contador_leitura) * 20/1023) + " KWh");
      delay(100);
      Serial.println("Sala   " + String((valor_total_sala / contador_leitura) * 20/1023) + " KWh");
      // Reinicializa as variáveis para a próxima hora
      valor_total_quarto = 0;
      valor_total_sala = 0;
      contador_leitura = 0;
  }
}