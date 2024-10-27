#include <iostream>

// Macros
#define putStar std::cout << "*"
#define CLEAR "\033[2J\033[1;1H"
#define GREEN "\033[32m"
#define RESET "\033[0m"

void pyramid(bool inversed, int n);

// Only positive intigers are accepted
int main() {

  int n;
  do {
    std::cout << CLEAR;
    std::cout << "Enter n: ";
    std::cin >> n;

    // Watch for integers only; if not, print error message and ask again
    if (std::cin.fail()) {
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      continue;
    }
  } while (n <= 0);

  // Print the regular n-th triangle
  pyramid(false, n);

  // Print the inverted n-th triangle
  pyramid(true, n);
  std::cout << RESET; // Base case

  return 0;
}

void pyramid(bool inversed, int n) {
  if (inversed) {
    for (int i = n; i >= 1; i--) {
      if (i % 2 == 0) {
        std::cout << GREEN;
      } else {
        std::cout << RESET;
      }
      for (int j = 1; j <= i; j++) {
        putStar;
      }
      std::cout << std::endl;
    }
  } else {
    for (int i = 1; i <= n; i++) {
      if (i % 2 == 0) {
        std::cout << GREEN;
      } else {
        std::cout << RESET;
      }
      for (int j = 1; j <= i; j++) {
        putStar;
      }
      std::cout << std::endl;
    }
  }
}

