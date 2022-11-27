#include<math.h>
#include<stdlib.h>
#include<iostream>

#define	h	161 
#define	w	475
#define a   180
#define r   502
#define threshold   20
#define pi 3.14159265359

void HoughTransform(int height, int weight,  int Binary_Matrix[h][w] ,  int Vote_Matrix[a][2*r+1]);

void Return_Line(int height, int weight,  int Vote_Matrix[a][2*r+1], int Line_Matrix[h][w], int Binary_Matrix[h][w]);