/*
 * Line_Dection.h
 *
 *  Created on: Dec 17, 2022
 *      Author: ASUS
 */

#ifndef INC_LINE_DECTION_H_
#define INC_LINE_DECTION_H_

#include<math.h>
#include<stdlib.h>
#include<stdint.h>
#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Image_Input.h>

#define	h	50
#define	w	100
#define a   45
#define r   112
#define threshold   10
#define pi 3.14159265359

extern int Vote_Matrix[a][2*r+1];
extern int Line_Matrix[h][w];
extern int Image_Matrix[h][w];

void HoughTransform();

void Reset_Image();

void Get_ImageLine();

void Create_LineMatrix();

#endif /* INC_LINE_DECTION_H_ */
