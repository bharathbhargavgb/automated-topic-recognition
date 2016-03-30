#include <bits/stdc++.h>
using namespace std;
int isTuple(string);
int main() {
	string brr;
	char ch;
	//char arr[1000];
//	string arr;
	char arr[1000];
	string subcat("subcat");
	string slash("\\n");
	int i = 0;
	bool start = false;
	int open = 0;
	int var = 0;
	int flag = 0;
	while((ch = getchar()) != EOF) {
//		cout << ch;

		if(ch == '(') {
			start = true;
		} else if(ch == ')' and start == true) {
			
			arr[i] = '\0';
			string brr(arr);
			if(isTuple(brr)) {// and (brr.find("file") != string::npos || brr.find(subcat) != string::npos || brr.find("page") != string::npos) ) {
				size_t pos = brr.find(slash);	
				if(pos != string::npos) {
					//cout << "Found at " << pos << endl;
					size_t quote = pos;
					while(!(brr[quote] == '\'' && brr[quote-1] == ',')) {
						quote--;
					}
					brr.erase(quote+1, pos - quote + 1); 
				}
				if(brr.find("subcat") != string::npos || brr.find("page") != string::npos) {
					//cout << "INSERT INTO categorylinks VALUES ";
					brr.erase(0, 1);
					cout << brr  << endl;
				}

				i=0;

				start = false;
			}
		}
		if(start == true) {
			arr[i] = ch;
			i++;
		}
		if(i>1110){
			arr[i]='\0';
			string brr(arr);
			cout << arr <<endl;
		}
	}
	return 0;
}
int isTuple(string brr){
	int inQuotes=0;
	int commas=0;
	int quotes=0;
	if(brr[0] != '(')
		return 0;
	for(int i=0; i<brr.length() ; i++){
		if((brr[i] == '\'' and inQuotes == 0 and brr[i-1] != '\\') || (brr[i] == '\'' and inQuotes == 0 and brr[i-1] == '\\' and brr[i-2] == '\\')){
			inQuotes = 1;
			quotes++;
		}
		else if((brr[i] == '\'' and inQuotes == 1 and brr[i-1] != '\\') || (brr[i] == '\'' and inQuotes == 1 and brr[i-1] == '\\' and brr[i-2] == '\\')){ 
			inQuotes = 0;
			quotes++;
		}
		else if(brr[i] == ',' and inQuotes ==0)
			commas++;
	}
	
		//cout << commas << " " << quotes << endl;
	if(commas != 6)
		return 0;
	return 1;
}
		
