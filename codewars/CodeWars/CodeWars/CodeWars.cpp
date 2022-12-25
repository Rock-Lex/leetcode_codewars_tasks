#include "CodeWars.h"

using namespace std;


unsigned adde(unsigned x, unsigned y)
{

	string a = to_string(x);
	string b = to_string(y);

	int len = a.length();

	if (b.length() > len)
		len = b.length();

	vector<int> answ;

	for (int i = len - 1; i != -1; --i)
	{
		answ.insert(answ.begin(), (int)a[i] - 48 + (int)b[i] - 48);
	}

	string answer;

	for (int i : answ)
	{
		answer += to_string(i);
	}

	cout << answer << endl;

	return 0;
}

int main()
{
	cout << adde(26, 39) << endl;

	return 0;
}

	