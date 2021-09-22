int incomingByte = 0;
int ledPin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

int counter = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() == 0 and counter == 0)
  {
    Serial.print("Ping");
    delay(10);
    counter++;
  }
  else
  {
    incomingByte = Serial.read();

    // say what you got:
    if (incomingByte == 49) { // ASCII printable characters: 49 means number 1
      digitalWrite(ledPin, HIGH);
    } else if (incomingByte == 48) { // ASCII printable characters: 48 means number 0
      digitalWrite(ledPin, LOW);
    }
    delay(10);
    if (counter < 100)
    {
      counter ++;
    }
    else
    {
      counter = 0;
    }
  }
}
