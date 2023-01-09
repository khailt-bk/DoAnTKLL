/*
 * Line_Dection.h
 *
 *  Created on: Dec 17, 2022
 *      Author: ASUS
 */

#ifndef INC_LINE_DECTION_H_
#define INC_LINE_DECTION_H_

#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Image_Input.h>
#include "UART_Data.h"

#define	height	50
#define	width	100
#define a   45
#define r   112
#define threshold   15
#define pi 3.14159265359

extern int Vote_Matrix[a][2*r+1];
extern int Line_Matrix[height][width];
extern int Image_Matrix[height][width];
extern int Time_Counter;
extern int timer_flag;

void HoughTransform();

void Reset_Image();

void Get_ImageLine();

void Create_LineMatrix();

void Create_VoteTable();

void Vote_Threshold();
#endif /* INC_LINE_DECTION_H_ */
