#include <cstdio>
#include <boost/array.hpp>
#include <boost/regex.hpp>
#include <string>
#include <iostream>

void test_regex()
{
	std::string line;
	boost::regex pat("^Subject: (Re: |Aw: )*(.*)");

	//while (std::cin)
	//{
	//	std::getline(std::cin, line);
	//	boost::smatch matches;
	//	if (boost::regex_match(line, matches, pat))
	//		std::cout << matches[2] << std::endl;
	//}
}

void test_array()
{
	boost::array<int, 4> arr = { { 2,2,3,4, } };
	printf("boost_array! %d\n", arr[0]);
}

int main()
{

    printf("hello from boost_test!\n");
	test_array();
	test_regex();
    return 0;
}