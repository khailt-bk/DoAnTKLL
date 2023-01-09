/*
 * UART_Data.c
 *
 *  Created on: Dec 29, 2022
 *      Author: ASUS
 */
#include "UART_Data.h"

uint8_t Light_Point[]= "1:";
uint8_t Dark_Point[]= "0:";
uint8_t Start[]= "!";
uint8_t End[]= "#";
uint8_t New_Line[]= "\r\n";
uint8_t timeStart_H[]= "=";
uint8_t timeEnd_H[]= "<";
uint8_t timeStart_GL[]= "%";
uint8_t timeEnd_GL[]= ">";
UART_HandleTypeDef huart2;

void UART_data(){
	HAL_UART_Transmit (& huart2 , Start ,sizeof(Start), 100);
	HAL_Delay(1);
	for(int i= 0; i< 50;i++){
		for(int j= 0; j< 100 ;j++){
			if(Line_Matrix[i][j] == 1){
				HAL_UART_Transmit (& huart2 , Light_Point ,sizeof(Light_Point), 100);
				HAL_Delay(1);
				}
			else{
				HAL_UART_Transmit (& huart2 , Dark_Point ,sizeof(Dark_Point), 100);
				HAL_Delay(1);
			}
			}
		}
	HAL_UART_Transmit (& huart2 , End ,sizeof(End), 100);
	HAL_Delay(1);
}
void UART_Time(){
	if(timer_flag == 1){
		HAL_UART_Transmit (& huart2 , timeStart_H ,sizeof(timeStart_H), 100);
		HAL_Delay(1);
	}
	if(timer_flag ==2){
		HAL_UART_Transmit (& huart2 , timeEnd_H ,sizeof(timeEnd_H), 100);
		HAL_Delay(1);
	}
	if(timer_flag ==3){
		HAL_UART_Transmit (& huart2 , timeStart_GL ,sizeof(timeStart_GL), 100);
		HAL_Delay(1);
	}
	if(timer_flag ==4){
		HAL_UART_Transmit (& huart2 , timeEnd_GL ,sizeof(timeEnd_GL), 100);
		HAL_Delay(1);
	}
}

