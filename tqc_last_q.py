sum=0
max=0
string=input()
a=list(string)
print(a)
print(a[1])
"""
for i in range()(int i=0;i<4;i++){
        for(int j=0;j<5;j++){
            scanf("%d", &a[i][j]);
        }
    }
     
    for(int i=0;i<4;i++){
        for(int j=0;j<5;j++){
            if(a[i][j]!=0){
                int z1=j;
                sum=a[i][j];
                while(a[i][z1+1]!=0){
                    sum+=a[i][z1+1];
                    z1++;
                }
                if(sum>max)
                     max=sum;
                sum=0;
                int k=i+1;
                int m=j;
                while(a[k][m]!=0){
                    while(a[k][m+1]!=0 && m+1<=z1){
                        m++;
                    }
                    if(m<z1)
                     z1=m;
                  
                    for(int l=i;l<=k;l++){
                        for(int p=j;p<=m;p++){
                            sum+=a[l][p];
                        }
                    }
                    if(sum>max)
                        max=sum;
                    sum=0;
                    k++;
                }
            }
        }
    }
    printf("%d\n", max);
"""