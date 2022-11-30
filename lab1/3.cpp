#include <iostream>

using namespace std;

int main(){
	int n;
	cin >> n;
	int res = (n % 2 == 0) ? n + 2 : n + 1;
	cout << res;
	return 0;
}