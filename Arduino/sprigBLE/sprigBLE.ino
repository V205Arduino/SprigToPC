/*
  TITLE
  By V205
*/

#include <Keyboard.h>                           
#include <KeyboardBLE.h>


/*
TODO: write something else here
Well this half works.
I do need to figure out how to write code better
*/

// Define pin numbers for the buttons
const int wButtonPin = 5;
const int aButtonPin = 6;
const int sButtonPin = 7;
const int dButtonPin = 8;
const int iButtonPin = 12;
const int jButtonPin = 13;
const int kButtonPin = 14;
const int lButtonPin = 15;




void setup() 
{


  //uhhhh I really do need to make arrays next time
  pinMode(wButtonPin, INPUT_PULLUP);
  pinMode(aButtonPin, INPUT_PULLUP);
  pinMode(sButtonPin, INPUT_PULLUP);
  pinMode(dButtonPin, INPUT_PULLUP);
  pinMode(iButtonPin, INPUT_PULLUP);
  pinMode(jButtonPin, INPUT_PULLUP);
  pinMode(kButtonPin, INPUT_PULLUP);
  pinMode(lButtonPin, INPUT_PULLUP);
  // put your setup code here, to run once:
  Serial.begin(115200); // begin serial comunication.
  delay(1000);
  Serial.println(F("STARTING " __FILE__ " from " __DATE__ __TIME__));
  Serial.println("test2");
  //KeyboardBLE.begin();
  KeyboardBLE.begin();

  Serial.println("test");

}




void loop() {
  checkAndSendKey(wButtonPin, 'w');
  checkAndSendKey(aButtonPin, 'a');
  checkAndSendKey(sButtonPin, 's');
  checkAndSendKey(dButtonPin, 'd');
  checkAndSendKey(iButtonPin, 'i');
  checkAndSendKey(jButtonPin, 'j');
  checkAndSendKey(kButtonPin, 'k');
  checkAndSendKey(lButtonPin, 'l');
}

void checkAndSendKey(int pin, char key) {
  //static unsigned long lastKeyPressTime = 0; // Track the time of last key press
  if (digitalRead(pin) == LOW) {
    KeyboardBLE.press(key);
    Serial.println(key);
    /*
    unsigned long currentTime = millis();
    if (currentTime - lastKeyPressTime > timeBetweenKeystrokes) {
      Keyboard.press(key);
      delay(100); // Short delay to simulate a key press
      Keyboard.release(key);
      lastKeyPressTime = currentTime;
      Serial.print("Button pressed: ");
      Serial.println(key);
    }
    */
  }else{

    KeyboardBLE.release(key);
  }
}