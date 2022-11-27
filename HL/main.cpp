#include<iostream>
#include "HoughLine.cpp"
#include "HoughLine.h"
#include<fstream>
using namespace std;

int main(){
    int Binary_Image[h][w];
    int Vote_Table[a][2*r+ 1];
    int Line_Image[h][w];

    ifstream file;
    file.open("testcase1.txt");
    for(int i = 0; i< h ; i++){
        for(int j = 0; j< w ; j++){
            file >> Binary_Image[i][j];
        }
    }
    file.close();

    ofstream ofs2("Binary.txt");
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            ofs2 << Binary_Image[i][j] << ' ';
            
        }
        ofs2 << endl;
    }
    ofs2.close();
    // for(int i = 0; i< h ; i++){
    //     for(int j = 0; j< w ; j++){
    //         cout<< Binary_Image[i][j]<< " ";
    //     }
    // }
    //  Vote table
    for(int i = 0; i< 180 ; i++){
        for(int j = 0; j< 2*r + 1 ; j++){
            Vote_Table[i][j] = 0 ; 
        }
    }
    
    // Output Matrix
    for(int i = 0; i< h ; i++){
        for(int j = 0; j< w ; j++){
            Line_Image[i][j] = 0;
        }
    }

    // int count = 0;
    // for(int x = 0 ; x < w ; x++ ){
    //     for(int y = 0 ; y < h ; y++){
    //         if( Binary_Image[y][x] == 0){
    //             count++;
    //         }
    //     }
    // }
    // cout<<count;

    HoughTransform(h , w , Binary_Image , Vote_Table);

    // for(int i = 0; i< 180 ; i++){
    //     for(int j = 0; j< 2*r+1 ; j++){
    //         cout<< Vote_Table[i][j]<< " "; 
    //     }
    // }

    ofstream ofs1("Vote_table.txt");
    for (int i = 0; i < 180; i++){
        for (int j = 0; j < 2*r + 1 ; j++){
            ofs1 << Vote_Table[i][j] << ' ';          
        }
        ofs1 << endl;
    }
    ofs1.close();


    Return_Line(h , w , Vote_Table , Line_Image, Binary_Image);
    // for(int c = 0; c< h ; c++){
    //     for(int d = 0; d< w ; d++){
    //         cout << Line_Image[c][d] << " ";
    //         if(c == d-1){
    //             cout<<endl;
    //         }
    //     }
    // }

    ofstream ofs("Output.txt");

    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            ofs << Line_Image[i][j] << ' ';
            
        }
        ofs << endl;
    }
    ofs.close();

}
