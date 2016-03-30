#include <bits/stdc++.h>
using namespace std;

int main() {
	char ch;
	//char arr[1000];
//	string arr;
	char arr[1000];
	string subcat("subcat");
	string slash("\\n");
	int i = 0;
	bool start = false;
	while((ch = getchar()) != EOF) {
//		cout << ch;
		if(ch == '(') {
			start = true;
		} else if(ch == ')') {
			start = false;
			arr[i++] = ')';
			arr[i] = '\0';
			string brr(arr);
			if(brr.find(subcat) != string::npos) {
				size_t pos = brr.find(slash);	
				if(pos != string::npos) {
					//cout << "Found at " << pos << endl;
					size_t quote = pos;
					while(!(brr[quote] == '\'' && brr[quote-1] == ',')) {
						quote--;
					}
					brr.erase(quote+1, pos - quote + 1); 
				}
				cout << "INSERT INTO categorylinks VALUES ";
				cout << brr << ";" << endl;
			}
			i = 0;
		}
		if(start == true) {
			arr[i] = ch;
			i++;
		}
	}
	return 0;
}
