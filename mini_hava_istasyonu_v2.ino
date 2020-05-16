#include <DHT.h>
#include <DHT_U.h>

#include<SPI.h>
#include<RF24.h>
#include<DHT.h>
#include <Wire.h>
#include <SFE_BMP180.h>



int ortalama_ruzgar =0;

RF24 radio(9,10);
SFE_BMP180 bmp180;

#define DHTPIN 2 //DHT22'nin veri pinini Arduino'daki hangi pine bağladığımızı belirtiyoruz.
#define DHTTYPE DHT22 //Hangi DHT sensörünü kullandığımızı belirtiyoruz.
#define ALTITUDE 75.0


DHT dht(DHTPIN, DHTTYPE); //Belirttiğimiz değişkenleri kaydettiriyoruz.

void setup() {
Serial.begin(9600);
dht.begin(); //DHT22 ısı ve nem sensörünü ölçümlere başlattırıyoruz.
bmp180.begin();
radio.begin();
radio.setPALevel(RF24_PA_MAX);
radio.setChannel(0x76);
radio.openWritingPipe(0xF0F0F0F0E1LL);
radio.enableDynamicPayloads();
radio.powerUp();


}

void loop() {
  
 for (int i=0; i < 10; i++) {
 ortalama_ruzgar = ortalama_ruzgar + analogRead(A3);
 }
 ortalama_ruzgar = ortalama_ruzgar/10;

int nem = dht.readHumidity();
int sicaklik = dht.readTemperature();
int basinc = readPressure();


char buffer [20];
sprintf (buffer, "%d %d %d %d", nem, sicaklik, basinc, ortalama_ruzgar);
Serial.println(buffer);
radio.write(&buffer, sizeof("2000000000000"));
delay(5000);

}


float readPressure()
{
  char status;
  double T,P,p0,a;

  status = bmp180.startTemperature();
  if (status != 0)
  {
    delay(status);
    status = bmp180.getTemperature(T);
    if (status != 0)
    { 
      status = bmp180.startPressure(3);
      if (status != 0)
      {
        delay(status);
        status = bmp180.getPressure(P,T);
        if (status != 0)
        {
          p0 = bmp180.sealevel(P,ALTITUDE);       
          return p0;
        }
      }
    }
  }
}
