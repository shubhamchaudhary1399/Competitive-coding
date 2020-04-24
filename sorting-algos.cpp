#include<bits/stdc++.h>
using namespace std;

int* bubbleSort(int arr[], int size){
	int temp;
	bool noSwaps = true;
	for(int i=0; i<size-1; i++){
		for(int j=0; j<size-i-1; j++){
			if(arr[j] >arr[j+1]){
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
				noSwaps = false;
			}
			if(noSwaps == true)
				break;
		}
	}
	
	return arr;
}

int* insertionSort(int arr[], int size){
	int key;
	for(int i=1; i<size; i++){
		key = arr[i];
		int j = i-1;
		while(j>=0 && arr[j]>key){
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
	
	return arr;
}

int* selectionSort(int arr[], int size){
	int lowest,temp;
	for(int i=0; i<size; i++){
		lowest = i;
		for(int j=i+1; j<size; j++){
			if(arr[j] < arr[lowest])
				lowest = j;
		}
		temp = arr[i];
		arr[i] = arr[lowest];
		arr[lowest] = temp;
	}
	
	return arr;
}
void merge(int arr[], int start, int mid, int end){
	int n = end-start+1;
	int temp[n];
	
	int i = start;
	int j = mid+1;
	int k = 0;
	
	while(i <= mid && j <= end){
		if(arr[i] <= arr[j]){
			temp[k] = arr[i];
			i++;
		}
		else{
			temp[k] = arr[j];
			j++;
		}
		k++;
	}
	
	while(i <= mid){
		temp[k] = arr[i];
		i++;
		k++;
	}
	
	while(j <= end){
		temp[k] = arr[j];
		j++;
		k++;
	}
	
	int pos = 0;
	for(int x = start; x<=end; x++){
		arr[x] = temp[pos];
		pos++;
	}
}

void mergeSort(int arr[], int start, int end){
	if(start >= end)
		return;
		
	int mid = (start+end)/2;
	mergeSort(arr, start, mid);
	mergeSort(arr, mid+1, end);
	merge(arr, start, mid, end);
}

void printArray(int arr[], int size){
	for(int i=0; i<size; i++){
		cout<<arr[i]<<" ";
	}
}

int main(){
	int arr[] = {5,4,3,2,1};
	int size = sizeof(arr)/sizeof(arr[0]);
	mergeSort(arr, 0, size-1);
	printArray(arr, size);
	
	int *sortedArray = bubbleSort(arr,size);
	return 0;
}
