// Problem Statement
//An ATMEGA* (any atmega) code which takes in the potentiometer value as an ADC input and whenever the voltage level reaches Vcc/2 
//(half of the supply voltage),transmit the string "Level crossed" to your computer using serial interface. Also
//If the level is crossed from (Vcc/2 +) to (Vcc/2 -) transmit the string "Level crossed - neg edge detected"
//Else if If the level is crossed from (Vcc/2 -) to (Vcc/2 +) transmit the string "Level crossed - pos edge detected"

#include <avr/io.h>
#include "../../../../../../Program Files (x86)/Atmel/Atmel Studio 6.0/extensions/Atmel/AVRGCC/3.4.0.65/AVRToolchain/avr/include/avr/iom48.h"
#include <util/delay.h>
#include <stdlib.h>
//#define F_CPU 1843200 // Clock Speed
#define BAUD 9600
#define MYUBRR F_CPU/16/BAUD-1


void adc_init(void);
uint16_t adc_read(void);
void USART_Init( unsigned int);
void USART_Transmit( unsigned int );
void USART_Transmit_string (char*);

void adc_init(void)
{
    // AREF = AVcc
    // to feed ADC with vcc
    ADMUX = (1<<REFS0);
    
    // ADC Enable and pre scaler of 128
    ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
    // selecting channel 0 for conversion output
    ADMUX = (ADMUX & 0xD8);
    // start single conversion
    // write ’1′ to ADSC
    ADCSRA |= (1<<ADSC);
}

uint16_t adc_read(void)
{


    
    // wait for conversion to complete
    // ADSC becomes ’0′ again
    // till then, run loop continuously
    while(ADCSRA & (1<<ADSC));
    
    return ADC;
}

// to initialize the usart
void USART_Init( unsigned int ubrr)
{
    /*Set baud rate */
    UBRR0H = (unsigned char)(ubrr>>8);
    UBRR0L = (unsigned char)ubrr;
    //Enable receiver and transmitter
    UCSR0B = (1<<RXEN0)|(1<<TXEN0);
    /* Set frame format: 8data, 2stop bit */
    UCSR0C = (1<<USBS0)|(3<<UCSZ00);
}

// to put character on serial port

void USART_Transmit( char data )
{
    /* Wait for empty transmit buffer */
    while ( !( UCSR0A & (1<<UDRE0)));
    /* Copy 9th bit to TXB8 */
    UCSR0B &= ~(1<<TXB80);
    if ( data & 0x0100 )
    UCSR0B |= (1<<TXB80);
    /* Put data into buffer, sends the data */
    UDR0 = data;
}

// to put string on serial port
void USART_Transmit_string (char* stringptr)
{
    while(*stringptr != 0x00)
    {
        USART_Transmit(*stringptr);
        stringptr ++;
    }
}

int main(void)
{
    uint16_t adc_value;
    uint16_t p_adc_value;
    USART_Init(MYUBRR);
    adc_value = adc_read();
    if (adc_value < 512)
        {
            USART_Transmit_string("Level crossed\n");
        }
    while (1)
    {
        p_adc_value = adc_value;
        adc_value = adc_read();
        if (adc_value < 512)
        {
            USART_Transmit_string("Level crossed\n");
        }
        if ((p_adc_value > 512) & (adc_value < 512))
        {
            USART_Transmit_string("Level crossed - neg edge detected\n");
        }
        else if ((p_adc_value < 512) & (adc_value > 512))
        {
            USART_Transmit_string("Level crossed - pos edge detected\n");
        }
    }
    return 0;
}
