"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all('tbody')  # Collect everything in "tbody".
        for tag in tags:  # Manipulate to desire form.
            words = tag.text
            word = words.strip()
            word1 = word.split('\n')
            total_number1 = 0
            total_number2 = 0
            for i in range(400):  # Loop over the list.
                if i % 2 != 0:
                    word2 = word1[i].split(' ')
                    number1 = number_process(word2[1])
                    total_number1 += number1  # Calculate the total number.
                    number2 = number_process(word2[3])
                    total_number2 += number2  # Calculate the total number.
            print('Male Number: ' + str(total_number1))
            print('Female Number: ' + str(total_number2))


def number_process(number_string):  # Process the string with "," to a int.
    if len(number_string) <= 7:
        number = 0
        count = 0
        for i in range(len(number_string)):
            if number_string[i] != ',':
                number += int(number_string[i]) * 10 ** (len(number_string)-2-count)
                count += 1
    return number



if __name__ == '__main__':
    main()
