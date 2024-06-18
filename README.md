# Learn Xpaths for Selenium

## Introduction
This repository contains a collection of Xpath examples for Selenium. The examples are written in Python and use the Selenium WebDriver.

## Installation
To run the examples, you need to have Python and the Selenium WebDriver installed. You can install the Selenium WebDriver using pip:
```pip install selenium```

Next, download the appropriate WebDriver for your browser:
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Usage
To run the examples, clone the repository and run the Python scripts. You can run the scripts from the command line:
```python main.py```

## Theory of Xpath
Xpath is a query language for selecting nodes from an XML document. It is used in Selenium to locate elements on a web page. Xpath expressions can be used to select elements based on their tag name, attributes, text content, and more.

## Practice from here

Learn from [here](https://www.youtube.com/watch?v=NhG__BL8zFo) and practice on the below demo pages:

1. [Demo Page 1](https://theautomationzone.blogspot.com/2020/07/xpath-practice.html)
2. [Demo Page 2](https://theautomationzone.blogspot.com/2020/07/sample-webtable-3.html)

## Format of Xpath:
```//*[@Attribute='value']```

```//tagname[@Attribute='value']```

```//tagname[@Attribute='value' and @Attribute='value']```

```//tagname[@Attribute='value' or @Attribute='value']```

```//tagname[(@Attribute='value' and @Attribute='value') or (@Attribute='value' and @Attribute='value')]```

```//tagname[@Attribute='value']/tagname[@Attribute='value']```

```//tagname[@Attribute='value']/tagname[@Attribute='value']/tagname[@Attribute='value']```

## Explanation of Xpath Formats using Attributes:

1. `//*[@Attribute='value']`: This Xpath expression selects all elements (`*`) in the document where the attribute `Attribute` has the value `'value'`.

2. `//tagname[@Attribute='value']`: This Xpath expression selects all elements with the tag name `tagname` in the document where the attribute `Attribute` has the value `'value'`.

3. `//tagname[@Attribute='value' and @Attribute='value']`: This Xpath expression selects all elements with the tag name `tagname` in the document where both conditions are true: the attribute `Attribute` has the value `'value'` and another attribute `Attribute` also has the value `'value'`.

4. `//tagname[@Attribute='value' or @Attribute='value']`: This Xpath expression selects all elements with the tag name `tagname` in the document where either of the conditions is true: the attribute `Attribute` has the value `'value'` or another attribute `Attribute` also has the value `'value'`.

5. `//tagname[(@Attribute='value' and @Attribute='value') or (@Attribute='value' and @Attribute='value')]`: This Xpath expression selects all elements with the tag name `tagname` in the document where either of the conditions is true: the attributes `Attribute` and `Attribute` have the values `'value'` and `'value'`, or the attributes `Attribute` and `Attribute` have the values `'value'` and `'value'.

6. `//tagname1[@Attribute='value']/tagname2[@Attribute='value']`: This Xpath expression selects all elements with the tag name `tagname2` that are children of elements with the tag name `tagname1` and the attribute `Attribute` equal to `'value'`.

7. `//tagname1[@Attribute='value']/tagname2[@Attribute='value']/tagname3[@Attribute='value']`: This Xpath expression selects all elements with the tag name `tagname3` that are children of elements with the tag name `tagname2` that are children of elements with the tag name `tagname1` and the attribute `Attribute` equal to `'value'`.

Remember, in Xpath, `//` means to select nodes in the document from the current node that match the selection no matter where they are, and `@` is used to select attributes.


## More Xpath Examples
For more examples of Xpath expressions, check out the [W3Schools Xpath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp).

1. `//tagname`: Selects all elements with the tag name `tagname`.
2. `//tagname[@Attribute]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute`.
3. `//tagname[@Attribute='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'`.
4. `//tagname[@Attribute!='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value not equal to `'value'`.
5. `//tagname[@Attribute>value]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value greater than `value`.
6. `//tagname[@Attribute<value]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value less than `value`.
7. `//tagname[@Attribute>=value]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value greater than or equal to `value`.
8. `//tagname[@Attribute<=value]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value less than or equal to `value`.
9. `//tagname[@Attribute='value' and @Attribute='value']`: Selects all elements with the tag name `tagname` that have both attributes `Attribute` and `Attribute` with the values `'value'` and `'value'`.
10. `//tagname[@Attribute='value' or @Attribute='value']`: Selects all elements with the tag name `tagname` that have either attribute `Attribute` with the value `'value'` or attribute `Attribute` with the value `'value'`.
11. `//tagname[@Attribute='value']/..`: Selects the parent element of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
12. `//tagname1[@Attribute='value']//tagname2[@Attribute='value']`: Selects all elements with the tag name `tagname2` that are descendants of elements with the tag name `tagname1` and the attribute `Attribute` with the value `'value'`.
13. `//tagname1[@Attribute='value']/tagname2[@Attribute='value']`: Selects all elements with the tag name `tagname2` that are children of elements with the tag name `tagname1` and the attribute `Attribute` with the value `'value'`.
14. `//tagname1[@Attribute='value']/tagname2[@Attribute='value']/tagname3[@Attribute='value']`: Selects all elements with the tag name `tagname3` that are children of elements with the tag name `tagname2` that are children of elements with the tag name `tagname1` and the attribute `Attribute` with the value `'value'`.
15. `//tagname[@Attribute='value'][1]`: Selects the first element with the tag name `tagname` that has the attribute `Attribute` with the value `'value'`.
16. `(//tagname[@Attribute='value'])[1]`: Selects the first element with the tag name `tagname` that has the attribute `Attribute` with the value `'value'`.
17. `//tagname[ tagname2[@Attribute='value'] ]`: Selects all elements with the tag name `tagname` that have children elements with the tag name `tagname2` and the attribute `Attribute` with the value `'value'`.
18. `//tagname[ .//tagname2[@Attribute='value'] ]`: Selects all elements with the tag name `tagname` that have descendant elements with the tag name `tagname2` and the attribute `Attribute` with the value `'value'`.

## Using Functions Examples
- `//tagname[text()='value']`: Selects all elements with the tag name `tagname` that have the text content `'value'`.
- `//tagname[contains(@Attribute, 'value')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` containing the value `'value'`.
- `//tagname[starts-with(@Attribute, 'value')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` starting with the value `'value'`.
- `//tagname[ends-with(@Attribute, 'value')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` ending with the value `'value'`.
- `//tagname[ count(.//tagname2[@Attribute='value']) > 1 ]`: Selects all elements with the tag name `tagname` that have more than one descendant element with the tag name `tagname2` and the attribute `Attribute` with the value `'value'`.
- `//tagname[not(@Attribute='value')]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` with the value `'value'`.
- `//tagname[string-length(@Attribute)>5]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value longer than 5 characters.
- `//tagname[round(@Attribute)>5]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value rounded to the nearest whole number greater than 5.
- `//tagname[floor(@Attribute)>5]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value rounded down to the nearest whole number greater than 5.
- `//tagname[ceiling(@Attribute)>5]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with a value rounded up to the nearest whole number greater than 5.
- `//tagname[sum(.//tagname2[@Attribute])>5]`: Selects all elements with the tag name `tagname` that have the sum of the values of descendant elements with the tag name `tagname2` and the attribute `Attribute` greater than 5.
- `//tagname[avg(.//tagname2[@Attribute])>5]`: Selects all elements with the tag name `tagname` that have the average of the values of descendant elements with the tag name `tagname2` and the attribute `Attribute` greater than 5.
- `//tagname[min(.//tagname2[@Attribute])>5]`: Selects all elements with the tag name `tagname` that have the minimum value of descendant elements with the tag name `tagname2` and the attribute `Attribute` greater than 5.
- `//tagname[max(.//tagname2[@Attribute])>5]`: Selects all elements with the tag name `tagname` that have the maximum value of descendant elements with the tag name `tagname2` and the attribute `Attribute` greater than 5.
- `//tagname[normalize-space(@Attribute)='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` after removing leading and trailing white spaces and collapsing multiple white spaces into a single space.
- `//tagname[translate(@Attribute, 'AB', 'ab')='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` after converting all occurrences of the characters `'A'` and `'B'` to `'a'` and `'b'`.
- `//tagname[translate(@Attribute, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` after converting all uppercase letters to lowercase letters.
- `//tagname[normalize-space(translate(@Attribute, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'))='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` after converting all uppercase letters to lowercase letters and removing leading and trailing white spaces and collapsing multiple white spaces into a single space. (IgnoreCase + IgnoreSpace)
- `//tagname[substring(@Attribute, 1, 5)='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` starting from the first character and ending at the fifth character.
- `//tagname[substring-after(@Attribute, 'value')='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` after the substring `'value'`.
- `//tagname[substring-before(@Attribute, 'value')='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` before the substring `'value'`.
- `//tagname[substring-index(@Attribute, 'value')='value']`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` at the index of the substring `'value'`.
- `//tagname[matches(@Attribute, 'value')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'`.
- `//tagname[matches(@Attribute, 'value', 'i')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` case-insensitively.
- `//tagname[matches(@Attribute, 'value', 'm')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in multi-line mode.
- `//tagname[matches(@Attribute, 'value', 's')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in single-line mode.
- `//tagname[matches(@Attribute, 'value', 'x')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in free-spacing mode.
- `//tagname[matches(@Attribute, 'value', 'n')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in non-capturing mode.
- `//tagname[matches(@Attribute, 'value', 'U')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'iU')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` case-insensitively and in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'mU')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in multi-line mode and in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'sU')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in single-line mode and in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'xU')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in free-spacing mode and in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'nU')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` in non-capturing mode and in ungreedy mode.
- `//tagname[matches(@Attribute, 'value', 'isxnu')]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` matching the regular expression `'value'` case-insensitively, in single-line mode, in free-spacing mode, in non-capturing mode, and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'`.
- `//tagname[not(matches(@Attribute, 'value', 'i'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` case-insensitively.
- `//tagname[not(matches(@Attribute, 'value', 'm'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in multi-line mode.
- `//tagname[not(matches(@Attribute, 'value', 's'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in single-line mode.
- `//tagname[not(matches(@Attribute, 'value', 'x'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in free-spacing mode.
- `//tagname[not(matches(@Attribute, 'value', 'n'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in non-capturing mode.
- `//tagname[not(matches(@Attribute, 'value', 'U'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'iU'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` case-insensitively and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'mU'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in multi-line mode and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'sU'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in single-line mode and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'xU'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in free-spacing mode and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'nU'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` in non-capturing mode and in ungreedy mode.
- `//tagname[not(matches(@Attribute, 'value', 'isxnu'))]`: Selects all elements with the tag name `tagname` that do not have the attribute `Attribute` matching the regular expression `'value'` case-insensitively, in single-line mode, in free-spacing mode, in non-capturing mode, and in ungreedy mode.
- `//tagname[position()=1]`: Selects the first element with the tag name `tagname`.
- `//tagname[position()>1]`: Selects all elements with the tag name `tagname` except the first one.
- `//tagname[last()]`: Selects the last element with the tag name `tagname`.
- `//tagname[last()-1]`: Selects the second-to-last element with the tag name `tagname`.
- `//tagname[@Attribute='value'][2]`: Selects the second element with the tag name `tagname` that has the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value'][last()]`: Selects the last element with the tag name `tagname` that has the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value'][position()<3]`: Selects the first two elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value'][position()>1]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` except the first one.
- `//tagname[@Attribute='value'][position()<last()]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` except the last one.
- `//tagname[@Attribute='value'][position()>1 and position()<last()]`: Selects all elements with the tag name `tagname` that have the attribute `Attribute` with the value `'value'` except the first and last ones.
- `//tagname[@Attribute='value']/following-sibling::tagname`: Selects all sibling elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding-sibling::tagname`: Selects all sibling elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/parent::tagname`: Selects the parent element with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/ancestor::tagname`: Selects all ancestor elements with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/child::tagname`: Selects all child elements with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/descendant::tagname`: Selects all descendant elements with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/self::tagname`: Selects the element with the tag name `tagname` that has the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/descendant-or-self::tagname`: Selects all descendant elements with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`, including the elements themselves.
- `//tagname[@Attribute='value']/ancestor-or-self::tagname`: Selects all ancestor elements with the tag name `tagname` of elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`, including the elements themselves.
- `//tagname[@Attribute='value']/following::tagname`: Selects all elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding::tagname`: Selects all elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following-sibling::tagname[position()<3]`: Selects the first two sibling elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding-sibling::tagname[position()<3]`: Selects the first two sibling elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following::tagname[position()<3]`: Selects the first two elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding::tagname[position()<3]`: Selects the first two elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following::tagname[@Attribute='value']`: Selects all elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding::tagname[@Attribute='value']`: Selects all elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following::tagname[@Attribute='value'][position()<3]`: Selects the first two elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding::tagname[@Attribute='value'][position()<3]`: Selects the first two elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following-sibling::tagname[@Attribute='value']`: Selects all sibling elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding-sibling::tagname[@Attribute='value']`: Selects all sibling elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/following-sibling::tagname[@Attribute='value'][position()<3]`: Selects the first two sibling elements with the tag name `tagname` that follow elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.
- `//tagname[@Attribute='value']/preceding-sibling::tagname[@Attribute='value'][position()<3]`: Selects the first two sibling elements with the tag name `tagname` that precede elements with the tag name `tagname` and the attribute `Attribute` with the value `'value'`.

> Note: The above examples are just a few of the many Xpath expressions that can be used to select elements on a web page. For more examples and information, refer to the [W3Schools Xpath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp).

> Note: Do not use Absolute Xpath as it is not recommended. It is not reliable and can break easily if the structure of the web page changes. Always prefer using Relative Xpath.
