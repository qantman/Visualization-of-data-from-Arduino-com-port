#include <Adafruit_ADS1X15.h>

Adafruit_ADS1115 ads;

void setup(void)
{
  ads.setGain(GAIN_TWOTHIRDS);
  Serial.begin(9600);
/*                                                                                                                      
  ads.setGain(GAIN_TWOTHIRDS); 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  ads.setGain(GAIN_ONE);       1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  ads.setGain(GAIN_TWO);       2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  ads.setGain(GAIN_FOUR);      4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  ads.setGain(GAIN_EIGHT);     8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  ads.setGain(GAIN_SIXTEEN);   16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV
*/
  if (!ads.begin()) {
    Serial.println("Failed to initialize ADS.");
    while (1);
  }}

void loop(void)
{
  int16_t results;  
  float multiplier = 0.1875F;
  results = ads.readADC_Differential_0_1();
  Serial.print(results * multiplier);
  delay(100);
}
