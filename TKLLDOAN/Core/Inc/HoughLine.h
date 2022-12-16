/*
 * HoughLine.h
 *
 *  Created on: Dec 16, 2022
 *      Author: ASUS
 */

#ifndef INC_HOUGHLINE_H_
#define INC_HOUGHLINE_H_

#include<math.h>
#include<stdlib.h>
#include<stdint.h>
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

#define	h	100
#define	w	200
#define a   180
#define r   224
#define threshold   30
#define pi 3.14159265359

extern int Binary_Matrix[h][w];
extern int Vote_Matrix[a][2*r+1];
extern int Line_Matrix[h][w];
extern FILE *Output;
extern int Line;
extern int Writed_Line[];

void HoughTransform(int height, int weight,  int Binary_Matrix[h][w] ,  int Vote_Matrix[a][2*r+1]);

void Return_Line(int height, int weight,  int Vote_Matrix[a][2*r+1], int Line_Matrix[h][w], int Binary_Matrix[h][w]);

void Read_File();
void Vote_Table();
void Line_Output();
void Write_File();

#endif /* INC_HOUGHLINE_H_ */
