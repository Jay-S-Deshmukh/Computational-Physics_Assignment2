#include <iostream>
#include <cmath>

using namespace std;

double f(double t, double y){
    
    return y - t*t + 1;
}

double f_true(double t){
    
    return (t+1)*(t+1) - 0.5*exp(t);
}

int main(){
    
    double h = 0.2;
    int N = int(2/h) + 1;
    double t;
    double y[N], err[N], err_bound[N];    
    
    y[0] = 0.5;
    double M = 0.5*exp(2)-2;
    for(int i=0;i<N;i++)
    {
        t = h*(i);
        err[i] = 0.1*M*(exp(t)-1);
        
        if(i<N-1)
            y[i+1] = y[i] + h*f(t,y[i]);
        
    }
    
    for(int j=0;j<N;j++)
    {
        cout << "Euler:  " << y[j] << "  True:  "<< f_true(h*j) <<endl;
        cout << "Error:  " << err[j] <<endl;
    }
    
    return 0;
}
