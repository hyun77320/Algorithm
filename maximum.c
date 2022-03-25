#include <stdio.h>

int a[1000000] = {};

int main(){
	
	int n = 0;
	scanf("%d", &n);
	int i, j = 0;
	int max = 0;
	int min = 0;
	
	for(i = 0; i < n; i++){
		scanf("%d", &a[i]);
	}
	
	max = a[0];
	min = a[0];
	
	for(j = 0; j < n; j++){
		if(max < a[j]){
			max = a[j];
		}
		if(min > a[j]){
			min = a[j];
		}
	}
	
	printf("%d ", min);
	printf("%d", max);
	
}
