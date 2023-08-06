#include "checkit.h"
#include "task1.h"

void test1() {
   char input[] = "Hello THERE";
   char result[15];
   char *expected = "hello there";

   str_lower(input, result);

   checkit_string(result, expected);
}

void test2() {
	char input[] = "SPRU IS SO WEIRD";
	char result[20];
	char *expected = "spru is so weird";

	str_lower(input, result); // compare
	checkit_string(result, expected);
}

void test3() {
	char input[] = "HELLO IT IS A BEAUTIFUL DAY";
	char *expected = "hello it is a beautiful day";

	str_lower_mutate(input);

	checkit_string(input, expected);
}

int main(void) {
 //  test1();
   //test2();
   test3();
   return 0;
}
