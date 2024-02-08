Feature: Employee want promotion but manager doesn't. so Manager decide to busy employee whenever he ask any questions

#  Scenario Outline: Employee - Kya sir promotion to de do.
#     Given Tu pehle chrome browser open kar
#      When ye wali website open kar "<website>"
#      When usme apna naam aur aaj tak tune kya kya kam kiya wo fill kar
#      Then uske bad agar aaj tu fir wapas aaya to aur ek kam dunga
#    Examples:
#      | website |
#      | https://ultimateqa.com/filling-out-forms/ |

  Scenario Outline: ye website me se koi b 5 cheej agar tune automate kar di to tera promotion pakka
     Given Tu pehle chrome browser open kar
      When ye wali website open kar "<website>"
      When Koi b 5 cheej automate kar
      Then laptop band kar k tu ghar ja tera promotion letter mail karta hu
    Examples:
      | website |
      | http://the-internet.herokuapp.com |