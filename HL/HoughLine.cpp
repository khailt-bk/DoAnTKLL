#include"HoughLine.h"

void HoughTransform(int height, int weight,  int Binary_Matrix[h][w] ,  int Vote_Matrix[a][2*r+1]){
    for(int x = 0 ; x < weight ; x++ ){
        for(int y = 0 ; y < height ; y++){
            if( Binary_Matrix[y][x] == 1){
                for(int i = 0; i < 180 ; i++){
                    // theta 
                    float Angle = i*pi/180;
                    // p
                    float Distance = (float (x))*cos(Angle) + (float (y))*sin(Angle);
                    // round 
                    int j = ceilf(Distance)+ r ;
                    Vote_Matrix[i][j]++;
                }
            }
        }
    }
}

void Return_Line(int height, int weight,int Vote_Matrix[a][2*r+1], int Line_Matrix[h][w], int Binary_Matrix[h][w]){
    for(int x = 0 ; x < weight ; x++ ){
        for(int y = 0 ; y < height ; y++){
            if( Binary_Matrix[y][x] == 1){
                for(int i = 0; i < 180 ; i++){
                    // theta 
                    float Angle = i*pi/180;
                    // p
                    float Distance = (float (x))*cos(Angle) + (float (y))*sin(Angle);
                    // round 
                    int j = ceilf(Distance)+ r ;
                    if(Vote_Matrix[i][j] > threshold){
                        Line_Matrix[y][x] = 1;
                    }
                }
            }
        }
    }
}