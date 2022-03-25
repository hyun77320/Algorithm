#include <stdio.h>

int main(){
	int n = 0;
	scanf("%d", &n);
	
	int count = 0;
	int i;
	for(i = 1; i <= n; i++){
		if(i%10 == 3 && i/10 == 3){
			count += 1;
		}
		else if(i%10 == 6 && i/10 == 6){
			count += 1;
		}
		else if(i%10 == 9 && i/10 == 9){
			count += 1;
		}
		else if(i%10 == 3){
			count += 1;
		}
		else if(i%10 == 9){
			count += 1;
		}
		else if(i%10 == 6){
			count += 1;
		}
		else if(i/10 == 3){
			count += 1;
		}
		else if(i/10 == 6){
			count += 1;
		}
		else if(i/10 == 9){
			count += 1;
		}
	}
	printf("%d", count);
}
