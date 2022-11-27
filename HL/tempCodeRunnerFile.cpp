    for(int c = 0; c< h ; c++){
        for(int d = 0; d< w ; d++){
            cout << Line_Image[c][d] << " ";
            if(c == d-1){
                cout<<endl;
            }
        }
    }